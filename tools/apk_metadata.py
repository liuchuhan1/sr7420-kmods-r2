#!/usr/bin/env python3
"""Read APK v3 metadata without executing any target program."""
import hashlib, re, subprocess


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def parse_adbdump(text):
    match = re.search(r'^info:\n((?:[ \t].*\n|\n)*)', text, re.M)
    assert match, 'Missing APK info block'
    info = match[1]
    result = {}
    for key in ('name', 'version', 'arch'):
        values = re.findall(r'^  ' + key + r': ([^\s]+)$', info, re.M)
        assert len(values) == 1, 'Missing or ambiguous APK ' + key
        result[key] = values[0]
    assert re.fullmatch(r'[a-z0-9][a-z0-9+_.-]*', result['name']), 'Invalid package name'
    block = re.search(r'^  depends:[^\n]*\n((?:    .*\n)*)', info, re.M)
    dependencies = re.findall(r'^    - ([^\s]+)$', block[1], re.M) if block else []
    result['kernel_dependencies'] = [d[len('kernel='):] for d in dependencies if d.startswith('kernel=')]
    return result


def read_apk(apk, path):
    output = subprocess.run([str(apk), 'adbdump', str(path)], check=True,
                            capture_output=True, text=True).stdout
    result = parse_adbdump(output)
    assert path.name.startswith(result['name'] + '-'), 'APK filename disagrees with metadata'
    return result


def collect_kmods(topdir, kernel, selected):
    apk = topdir / 'staging_dir/host/bin/apk'
    directory = topdir / 'bin/targets/zte/zx279133/packages'
    release = (kernel / 'include/config/kernel.release').read_text().strip()
    vermagic = (kernel / '.vermagic').read_text().strip()
    assert re.fullmatch(r'[0-9a-f]{32}', vermagic), 'Missing generated OpenWrt ABI hash'
    candidates, ignored, invalid = {}, [], []
    for path in sorted(directory.glob('*.apk')):
        if not path.name.startswith(('kernel-', 'kmod-')):
            continue
        relative = path.relative_to(topdir / 'bin').as_posix()
        try:
            meta = read_apk(apk, path)
        except (AssertionError, subprocess.CalledProcessError) as error:
            invalid.append({'file': relative, 'error': str(error)})
            continue
        if meta['name'] != 'kernel':
            continue
        if meta['version'].startswith(release + '~' + vermagic + '-'):
            candidates.setdefault('kernel', []).append((path, meta))
        else:
            ignored.append({'file': relative, 'reason': 'different_kernel_abi'})
    kernels = candidates.get('kernel', [])
    assert len(kernels) == 1, 'Expected exactly one kernel APK for generated ABI'
    abi = kernels[0][1]['version']
    arch = kernels[0][1]['arch']
    for path in sorted(directory.glob('kmod-*.apk')):
        relative = path.relative_to(topdir / 'bin').as_posix()
        try:
            meta = read_apk(apk, path)
        except (AssertionError, subprocess.CalledProcessError):
            continue  # Already recorded by the first pass.
        if meta['name'] not in selected:
            ignored.append({'file': relative, 'reason': 'not_selected'})
        elif meta['kernel_dependencies'] != [abi] or meta['arch'] != arch:
            ignored.append({'file': relative, 'reason': 'different_kernel_abi_or_arch'})
        else:
            candidates.setdefault(meta['name'], []).append((path, meta))
    ambiguous = sorted(name for name, items in candidates.items() if len(items) != 1)
    records = []
    for name, items in sorted(candidates.items()):
        if len(items) != 1:
            continue
        path, meta = items[0]
        records.append({**meta, 'file': path.relative_to(topdir / 'bin').as_posix(),
                        'bytes': path.stat().st_size, 'sha256': sha256(path)})
    return {'kernel_abi': abi, 'arch': arch, 'package_records': records,
            'ignored_apks': ignored, 'invalid_apks': invalid, 'ambiguous_packages': ambiguous}
