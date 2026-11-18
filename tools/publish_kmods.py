#!/usr/bin/env python3
"""Create a signed APK repository from one successful, isolated build."""
import argparse,hashlib,json,re,shutil,subprocess
from pathlib import Path
from apk_metadata import read_apk, sha256
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--topdir',type=Path,required=True)
p.add_argument('--output',type=Path,required=True)
p.add_argument('--private-key',type=Path,required=True)
p.add_argument('--public-key',type=Path,required=True)
p.add_argument('--selection-report',type=Path,required=True)
a=p.parse_args();s=a.topdir.resolve();out=a.output.resolve()
assert not out.exists(), 'Use a new output directory'
selection=json.loads(a.selection_report.read_text())
assert selection.get('compiled') and not selection.get('selected_without_apk'), 'Full selected kmod build must be complete before publishing'
apk=s/'staging_dir/host/bin/apk';assert apk.is_file()
abi=selection['kernel_abi'];arch=selection['arch']
expected=set(selection['selected'])|{'kernel'}
records_in=selection['package_records']
assert len(records_in)==len(expected) and {x['name'] for x in records_in}==expected
assert len(expected)>100, 'All-kmods feed requires the complete selected set'
packages=[]
for record in records_in:
    f=(s/'bin'/record['file']).resolve()
    assert f.is_relative_to(s/'bin') and f.is_file() and not (s/'bin'/record['file']).is_symlink()
    assert f.stat().st_size==record['bytes'] and sha256(f)==record['sha256'], 'Artifact changed after audit'
    meta=read_apk(apk,f)
    assert all(meta[k]==record[k] for k in ['name','version','arch','kernel_dependencies'])
    assert meta['arch']==arch
    assert (meta['version']==abi if meta['name']=='kernel' else meta['kernel_dependencies']==[abi])
    packages.append(f)
keys=out/'keys';keys.mkdir(parents=True);shutil.copy2(a.public_key,keys/a.public_key.name)
def run(args):
    result=subprocess.run([str(x) for x in args],capture_output=True,text=True)
    if result.returncode:
        raise RuntimeError('APK command failed: '+result.stderr[-3000:])
    return result
records=[]
feed=out/'aarch64_cortex-a53'/abi;feed.mkdir(parents=True)
for f in packages:
    q=feed/f.name;shutil.copy2(f,q)
    # Normalize signatures with the same project key used by the matching image.
    run([apk,'--allow-untrusted','adbsign','--sign-key',a.private_key,q])
    run([apk,'--keys-dir',keys,'verify',q])
    records.append({'file':q.name,'bytes':q.stat().st_size,'sha256':hashlib.sha256(q.read_bytes()).hexdigest()})
run([apk,'--keys-dir',keys,'mkndx','--sign-key',a.private_key,'--description','SR7420 '+abi,'--output',feed/'packages.adb',*sorted(feed.glob('*.apk'))])
run([apk,'--keys-dir',keys,'verify',feed/'packages.adb'])
(feed/'manifest.json').write_text(json.dumps({'kernel_abi':abi,'packages':records,'all_signatures_verified':True},indent=2)+'\n')
print(json.dumps({'kernel_abi':abi,'package_count':len(records)}))
