# SR7420 模块构建结果

日期：2026-11-18。内核 ABI：`6.18.60~2b497291254683b6ce56b38338fafb7e-r1`。

请求 1512 项，目标依赖求解选中 1109 项，全部产生 APK，缺包 0；403 项未选中。这不是“所有平台的每个驱动都支持 SR7420”。

实际 1109 个 APK 内共有 1442 个 `.ko`；896 个 in-tree KernelPackage 的 FILES 检查和全局模块依赖、架构、vermagic 检查通过。没有逐一做各安装组合或硬件功能测试。

## 此前缺失的模块

| 包 | 功能 | 本次结果 |
| --- | --- | --- |
| `kmod-inet-diag` | TCP/UDP socket 诊断，供 ss 等工具使用 | 已构建并签名 |
| `kmod-netlink-diag` | Netlink socket 诊断 | 已构建并签名 |
| `kmod-nf-conntrack-netlink` | 通过 Netlink 查询和管理连接跟踪 | 已构建并签名 |
| `kmod-nft-tproxy` | nftables 透明代理 | 已构建并签名 |
| `kmod-nft-socket` | nftables socket 匹配 | 已构建并签名 |
| `kmod-tun` | 用户态 TUN/TAP 虚拟网络设备 | 已构建并签名 |

`librt` 是用户态库包名，不是 kmod。本模块仓库不提供同名包；musl 应用的依赖应使用该目标的工具链重新求解，不能以空包伪造安装成功。

## 没有独立 .ko 的已选包

以下包属于固件、元包、功能开关或内建依赖，不能将其说成独立可加载模块。最终 Linux `=m` / `=y` 和内建文件清单见 JSON 报告。

`kmod-crypto-acompress`, `kmod-crypto-aead`, `kmod-crypto-ecb`, `kmod-crypto-gf128`, `kmod-crypto-hash`, `kmod-crypto-kpp`, `kmod-crypto-lib-chacha20`, `kmod-crypto-manager`, `kmod-dma-buf`, `kmod-fixed-phy`, `kmod-fs-exportfs`, `kmod-fs-squashfs`, `kmod-lib-crc32c`, `kmod-lib-xxhash`, `kmod-lib-zlib-deflate`, `kmod-lib-zlib-inflate`, `kmod-mdio-devres`, `kmod-mt76`, `kmod-mt7615-firmware`, `kmod-mt7622-firmware`, `kmod-mt7663-firmware-ap`, `kmod-mt7663-firmware-sta`, `kmod-mt7915-firmware`, `kmod-mt7916-firmware`, `kmod-mt7921-firmware`, `kmod-mt7922-firmware`, `kmod-mt7925-firmware`, `kmod-mt7990-firmware`, `kmod-mt7992-23-firmware`, `kmod-mt7992-firmware`, `kmod-mt7996-233-firmware`, `kmod-mt7996-firmware`, `kmod-mt7996-firmware-common`, `kmod-net-selftests`, `kmod-nf-conntrack6`, `kmod-nf-log6`, `kmod-nf-nat6`, `kmod-nf-nathelper-extra`, `kmod-nft-arp`, `kmod-nls-base`, `kmod-of-mdio`, `kmod-phylink`, `kmod-random-core`, `kmod-regmap-core`, `kmod-regmap-mmio`, `kmod-sound-dynamic-minors`, `kmod-sound-midi2-seq`, `kmod-sound-midi2-usb`, `kmod-thermal`, `kmod-usb-common`

## 未选中项及功能

下表保留每项的功能标题与实际依赖表达式。`未由 Kconfig 选中` 仅说明本目标未满足依赖或存在互斥，不能据此推断对应代码本身有问题。有明确内核限制的项目另列出原因。

| 软件包 | 功能 | 依赖或明确限制 |
| --- | --- | --- |
| `kmod-9pvirtio` | Plan 9 Virtio Support | VIRTIO_SUPPORT |
| `kmod-acpi-mdio` | ACPI MDIO support | !((TARGET_armsr\|\|TARGET_bcm27xx_bcm2708\|\|TARGET_loongarch64\|\|TARGET_malta\|\|TARGET_tegra)) \|\| !TARGET_x86；TARGET_armsr |
| `kmod-acpi-video` | kmod-acpi-video | DISPLAY_SUPPORT；TARGET_x86\|\|TARGET_loongarch64 |
| `kmod-ag71xx` | Atheros AR7XXX/AR9XXX ethernet mac support | !((TARGET_armsr\|\|TARGET_bcm27xx_bcm2708\|\|TARGET_loongarch64\|\|TARGET_malta\|\|TARGET_tegra)) \|\| !TARGET_x86；TARGET_ath79 |
| `kmod-ag71xx-legacy` | Downstream Atheros AR7XXX/AR9XXX ethernet mac support | !((TARGET_armsr\|\|TARGET_bcm27xx_bcm2708\|\|TARGET_loongarch64\|\|TARGET_malta\|\|TARGET_tegra)) \|\| !TARGET_x86；TARGET_ath79 |
| `kmod-ahci-qoriq` | Freescale QorIQ AHCI SATA support | PCI_SUPPORT\|\|TARGET_sunxi；TARGET_ipq806x\|\|TARGET_layerscape\|\|TARGET_rockchip\|\|TARGET_sunxi；TARGET_layerscape |
| `kmod-amazon-ena` | Elastic Network Adapter (for Amazon AWS) | TARGET_x86_64\|\|TARGET_armsr |
| `kmod-amd-xgbe` | AMD Ethernet on SoC support | !((TARGET_armsr\|\|TARGET_bcm27xx_bcm2708\|\|TARGET_loongarch64\|\|TARGET_malta\|\|TARGET_tegra)) \|\| !TARGET_x86；PCI_SUPPORT；TARGET_x86_64 |
| `kmod-asn1-encoder` | kmod-asn1-encoder | 未由 Kconfig 选中 |
| `kmod-at91-adc` | ADC on atmel SoC | TARGET_at91 |
| `kmod-at91-i2c` | I2C (TWI) master driver for Atmel AT91 | TARGET_at91 |
| `kmod-at91-udc` | USB Device Controller on atmel SoC | (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；TARGET_at91；USB_GADGET_SUPPORT |
| `kmod-ata-ahci-dwc` | Synopsys DWC AHCI SATA | PCI_SUPPORT\|\|TARGET_sunxi；TARGET_ipq806x\|\|TARGET_layerscape\|\|TARGET_rockchip\|\|TARGET_sunxi；TARGET_rockchip |
| `kmod-ata-ahci-mtk` | Mediatek AHCI Serial ATA support | (TARGET_mediatek_mt7622\|\|TARGET_mediatek_mt7623)；PCI_SUPPORT\|\|TARGET_sunxi |
| `kmod-ata-ahci-platform` | AHCI Serial ATA Platform support | PCI_SUPPORT\|\|TARGET_sunxi；TARGET_ipq806x\|\|TARGET_layerscape\|\|TARGET_rockchip\|\|TARGET_sunxi |
| `kmod-ata-dwc` | DesignWare Cores SATA support | PCI_SUPPORT\|\|TARGET_sunxi；TARGET_apm821xx |
| `kmod-ata-marvell-sata` | Marvell Serial ATA support | PCI_SUPPORT\|\|TARGET_sunxi；TARGET_kirkwood |
| `kmod-ata-sunxi` | AllWinner sunXi AHCI SATA support | PCI_SUPPORT\|\|TARGET_sunxi；TARGET_ipq806x\|\|TARGET_layerscape\|\|TARGET_rockchip\|\|TARGET_sunxi；TARGET_sunxi |
| `kmod-ath11k-ahb` | Qualcomm 802.11ax AHB wireless chipset support | PCI_SUPPORT\|\|USB_SUPPORT\|\|TARGET_ath79；TARGET_qualcommax |
| `kmod-atmel-usba-udc` | High-speed USB Device Controller on atmel SoC | (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；TARGET_at91；USB_GADGET_SUPPORT |
| `kmod-backlight` | kmod-backlight | DISPLAY_SUPPORT |
| `kmod-backlight-pwm` | PWM Backlight support | DISPLAY_SUPPORT；PWM_SUPPORT |
| `kmod-bcmgenet` | Broadcom GENET internal MAC (Raspberry Pi 4) | !TARGET_x86；TARGET_armsr |
| `kmod-bgmac` | Broadcom bgmac driver | !TARGET_bcm47xx_legacy；TARGET_bcm47xx |
| `kmod-btmtkuart` | MediaTek HCI UART driver | !(USB_SUPPORT && USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；TARGET_mediatek_mt7622 |
| `kmod-bxcan` | STM32 Basic Extended CAN (bxCAN) devices | PACKAGE_kmod-can；TARGET_stm32 |
| `kmod-camera-bcm2835` | BCM2835 Camera | PACKAGE_kmod-video-core；TARGET_bcm27xx |
| `kmod-can-flexcan` | Support for Freescale FLEXCAN based chips | PACKAGE_kmod-can；TARGET_imx |
| `kmod-can-xilinx-can` | Xilinx CAN IP | PACKAGE_kmod-can；TARGET_zynq |
| `kmod-codec-bcm2835` | BCM2835 Video Codec | PACKAGE_kmod-video-core；TARGET_bcm27xx |
| `kmod-crypto-engine` | kmod-crypto-engine | 未由 Kconfig 选中 |
| `kmod-crypto-hw-ccp` | AMD Cryptographic Coprocessor | TARGET_x86 |
| `kmod-crypto-hw-eip93` | MTK EIP93 crypto module | TARGET_ramips_mt7621 |
| `kmod-crypto-hw-geode` | AMD Geode hardware crypto module | TARGET_x86_geode |
| `kmod-crypto-hw-hifn-795x` | HIFN 795x crypto accelerator | The kernel requires !ARCH_DMA_ADDR_T_64BIT; incompatible with this ARM64 target. |
| `kmod-crypto-hw-ixp4xx` | Intel IXP4xx crypto accelerator | TARGET_ixp4xx |
| `kmod-crypto-hw-padlock` | VIA PadLock ACE with AES/SHA hw crypto module | The kernel requires X86; unavailable on this ARM64 target. |
| `kmod-crypto-hw-safexcel` | MVEBU SafeXcel Crypto Engine module | (TARGET_mvebu_cortexa53\|\|TARGET_mvebu_cortexa72\|\|TARGET_mediatek_filogic\|\|TARGET_mediatek_mt7623) |
| `kmod-crypto-hw-talitos` | Freescale integrated security engine (SEC) driver | (TARGET_mpc85xx\|\|TARGET_layerscape) |
| `kmod-crypto-rsa` | kmod-crypto-rsa | 未由 Kconfig 选中 |
| `kmod-crypto-test` | Test CryptoAPI module | CONFIG_CRYPTO_TEST/tcrypt is absent from the pinned Linux 6.18 source. |
| `kmod-dahdi-echocan-oslec` | DAHDI OSLEC echo canceller support | !TARGET_zte；PACKAGE_kmod-dahdi |
| `kmod-dm9000` | Davicom 9000 Ethernet support | Requires ARM32/MIPS/Coldfire/NIOS2 or COMPILE_TEST; not an ARM64 runtime driver. |
| `kmod-dma-ralink` | Ralink GDMA Engine | !TARGET_ramips_rt288x；TARGET_ramips |
| `kmod-drm` | kmod-drm | !(PACKAGE_kmod-backlight) \|\| DISPLAY_SUPPORT；DISPLAY_SUPPORT |
| `kmod-drm-amdgpu` | AMDGPU DRM support | DISPLAY_SUPPORT；TARGET_x86\|\|TARGET_loongarch64 |
| `kmod-drm-buddy` | kmod-drm-buddy | DISPLAY_SUPPORT |
| `kmod-drm-display-helper` | kmod-drm-display-helper | DISPLAY_SUPPORT |
| `kmod-drm-dma-helper` | kmod-drm-dma-helper | DISPLAY_SUPPORT |
| `kmod-drm-exec` | kmod-drm-exec | DISPLAY_SUPPORT |
| `kmod-drm-i915` | Intel i915 DRM support | (TARGET_x86_64\|\|TARGET_x86_generic\|\|TARGET_x86_legacy)；DISPLAY_SUPPORT；TARGET_x86\|\|TARGET_loongarch64 |
| `kmod-drm-imx` | Freescale i.MX DRM support | DISPLAY_SUPPORT；TARGET_imx |
| `kmod-drm-imx-hdmi` | Freescale i.MX HDMI DRM support | AUDIO_SUPPORT；DISPLAY_SUPPORT；PACKAGE_kmod-drm-imx |
| `kmod-drm-imx-ldb` | Freescale i.MX LVDS DRM support | (TARGET_imx&&TARGET_imx_cortexa9)；DISPLAY_SUPPORT；PACKAGE_kmod-drm-imx；USES_DEVICETREE；USES_PM |
| `kmod-drm-ivpu` | Intel VPU DRM support | TARGET_x86_64 |
| `kmod-drm-kms-helper` | CRTC helpers for KMS drivers | DISPLAY_SUPPORT |
| `kmod-drm-lima` | Mali-4xx GPU support | !(PACKAGE_kmod-backlight) \|\| DISPLAY_SUPPORT；(TARGET_rockchip\|\|TARGET_sunxi)；DISPLAY_SUPPORT |
| `kmod-drm-mipi-dbi` | kmod-drm-mipi-dbi | DISPLAY_SUPPORT |
| `kmod-drm-panel-mipi-dbi` | Generic MIPI DBI LCD panel | DISPLAY_SUPPORT |
| `kmod-drm-panel-simple` | Simple (non-eDP) TFT panels | DISPLAY_SUPPORT；USES_DEVICETREE；USES_PM |
| `kmod-drm-panel-tc358762` | TC358762 DSI/DPI bridge | DISPLAY_SUPPORT |
| `kmod-drm-panfrost` | DRM support for ARM Mali Midgard/Bifrost GPUs | !(PACKAGE_kmod-backlight) \|\| DISPLAY_SUPPORT；(TARGET_rockchip\|\|TARGET_sunxi)；DISPLAY_SUPPORT |
| `kmod-drm-panthor` | DRM support for ARM Mali CSF-based GPUs | !(PACKAGE_kmod-backlight) \|\| DISPLAY_SUPPORT；DISPLAY_SUPPORT；TARGET_rockchip |
| `kmod-drm-radeon` | Radeon DRM support | DISPLAY_SUPPORT；TARGET_x86；TARGET_x86\|\|TARGET_loongarch64 |
| `kmod-drm-rockchip` | Rockchip DRM support | DISPLAY_SUPPORT；TARGET_rockchip |
| `kmod-drm-rp1-dpi` | RP1 Display Parallel Interface for Video | !(PACKAGE_kmod-backlight) \|\| DISPLAY_SUPPORT；!TARGET_uml；AUDIO_SUPPORT；DISPLAY_SUPPORT；TARGET_bcm27xx；TARGET_bcm27xx_bcm2712 |
| `kmod-drm-rp1-dsi` | RP1 Display Serial Interface for Video | !(PACKAGE_kmod-backlight) \|\| DISPLAY_SUPPORT；!TARGET_uml；AUDIO_SUPPORT；DISPLAY_SUPPORT；TARGET_bcm27xx；TARGET_bcm27xx_bcm2712 |
| `kmod-drm-rp1-vec` | RP1 Display Composite Video | !(PACKAGE_kmod-backlight) \|\| DISPLAY_SUPPORT；!TARGET_uml；AUDIO_SUPPORT；DISPLAY_SUPPORT；TARGET_bcm27xx；TARGET_bcm27xx_bcm2712 |
| `kmod-drm-sched` | kmod-drm-sched | DISPLAY_SUPPORT |
| `kmod-drm-shmem-helper` | kmod-drm-shmem-helper | DISPLAY_SUPPORT |
| `kmod-drm-suballoc-helper` | kmod-drm-suballoc-helper | DISPLAY_SUPPORT |
| `kmod-drm-ttm` | GPU memory management subsystem | DISPLAY_SUPPORT |
| `kmod-drm-ttm-helper` | kmod-drm-ttm-helper | DISPLAY_SUPPORT |
| `kmod-drm-v3d` | Broadcom V3D Graphics | !(PACKAGE_kmod-backlight) \|\| DISPLAY_SUPPORT；DISPLAY_SUPPORT；TARGET_bcm27xx_bcm2711\|\|TARGET_bcm27xx_bcm2712 |
| `kmod-drm-vc4` | Broadcom VC4 Graphics | !(PACKAGE_kmod-backlight) \|\| DISPLAY_SUPPORT；!TARGET_uml；AUDIO_SUPPORT；DISPLAY_SUPPORT；TARGET_bcm27xx |
| `kmod-drm-vram-helper` | kmod-drm-vram-helper | DISPLAY_SUPPORT |
| `kmod-dsa-gswip` | Lantiq xRx200/xRx300/xRx330 switch support | TARGET_lantiq_xrx200\|\|TARGET_lantiq_xrx200_legacy |
| `kmod-dwmac-imx` | NXP i.MX8 Ethernet controller | !((TARGET_armsr\|\|TARGET_bcm27xx_bcm2708\|\|TARGET_loongarch64\|\|TARGET_malta\|\|TARGET_tegra)) \|\| !TARGET_x86；!TARGET_x86；(TARGET_armsr\|\|TARGET_loongarch64\|\|TARGET_x86_64) |
| `kmod-dwmac-intel` | Intel GMAC support | !((TARGET_armsr\|\|TARGET_bcm27xx_bcm2708\|\|TARGET_loongarch64\|\|TARGET_malta\|\|TARGET_tegra)) \|\| !TARGET_x86；(TARGET_armsr\|\|TARGET_loongarch64\|\|TARGET_x86_64)；TARGET_x86_64 |
| `kmod-dwmac-motorcomm` | Motorcomm PCI DWMAC support | !((TARGET_armsr\|\|TARGET_bcm27xx_bcm2708\|\|TARGET_loongarch64\|\|TARGET_malta\|\|TARGET_tegra)) \|\| !TARGET_x86；(TARGET_armsr\|\|TARGET_loongarch64\|\|TARGET_x86_64)；PCI_SUPPORT |
| `kmod-dwmac-rockchip` | Rockchip RK3328/RK3399/RK3568 Ethernet | !((TARGET_armsr\|\|TARGET_bcm27xx_bcm2708\|\|TARGET_loongarch64\|\|TARGET_malta\|\|TARGET_tegra)) \|\| !TARGET_x86；!TARGET_x86；(TARGET_armsr\|\|TARGET_loongarch64\|\|TARGET_x86_64) |
| `kmod-dwmac-sun8i` | Allwinner H3/A83T/A64 (sun8i) Ethernet | !((TARGET_armsr\|\|TARGET_bcm27xx_bcm2708\|\|TARGET_loongarch64\|\|TARGET_malta\|\|TARGET_tegra)) \|\| !TARGET_x86；!TARGET_x86；(TARGET_armsr\|\|TARGET_loongarch64\|\|TARGET_x86_64) |
| `kmod-echo` | Line Echo Canceller | CONFIG_ECHO and the referenced driver are absent from the pinned kernel source. |
| `kmod-econet-eth` | EcoNet EN751221 Ethernet Driver | TARGET_econet |
| `kmod-f71808e-wdt` | Fintek F718xx/F818xx Watchdog Timer | TARGET_x86 |
| `kmod-fb` | Framebuffer and framebuffer console support | DISPLAY_SUPPORT |
| `kmod-fb-cfb-copyarea` | Framebuffer software copy area support | DISPLAY_SUPPORT |
| `kmod-fb-cfb-fillrect` | Framebuffer software rectangle filling support | DISPLAY_SUPPORT |
| `kmod-fb-cfb-imgblt` | Framebuffer software image blit support | DISPLAY_SUPPORT |
| `kmod-fb-io-fops` | kmod-fb-io-fops | 未由 Kconfig 选中 |
| `kmod-fb-sys-fops` | Framebuffer software sys ops support | DISPLAY_SUPPORT |
| `kmod-fb-sys-ram` | Framebuffer in system RAM support | DISPLAY_SUPPORT |
| `kmod-fb-tft` | Support for small TFT LCD display modules | DISPLAY_SUPPORT；GPIO_SUPPORT |
| `kmod-fb-tft-ili9486` | FB driver for the ILI9486 LCD Controller | DISPLAY_SUPPORT；GPIO_SUPPORT |
| `kmod-fs-efivarfs` | efivar filesystem support | (x86_64\|\|x86) |
| `kmod-fs-reiserfs` | ReiserFS filesystem support | ReiserFS support is absent from the pinned Linux 6.18 source. |
| `kmod-fsl-dpaa1-net` | NXP DPAA1 (LS1043/LS1046) Ethernet | !TARGET_x86；TARGET_armsr |
| `kmod-fsl-dpaa2-console` | NXP DPAA2 Debug console | TARGET_armsr |
| `kmod-fsl-dpaa2-net` | NXP DPAA2 Ethernet | !TARGET_x86；TARGET_armsr |
| `kmod-fsl-enetc-net` | :NXP ENETC (LS1028A) Ethernet | !TARGET_x86；TARGET_armsr |
| `kmod-fsl-fec` | NXP (Freescale) FEC Ethernet controller (i.MX) | !TARGET_x86；TARGET_armsr |
| `kmod-fsl-mc-dpio` | kmod-fsl-mc-dpio | 未由 Kconfig 选中 |
| `kmod-fsl-pcs-lynx` | kmod-fsl-pcs-lynx | !TARGET_x86；TARGET_armsr |
| `kmod-fsl-xgmac-mdio` | NXP (Freescale) MDIO bus | !TARGET_x86；TARGET_armsr |
| `kmod-gpio-amd-fch` | kmod-gpio-amd-fch | GPIO_SUPPORT；TARGET_x86 |
| `kmod-gpio-cascade` | Generic GPIO cascade | The downstream CONFIG_GPIO_CASCADE driver is absent from the pinned kernel source. |
| `kmod-gpio-f7188x` | Fintek F718xx/F818xx GPIO Support | GPIO_SUPPORT；TARGET_x86 |
| `kmod-gpio-it87` | GPIO support for IT87xx Super I/O chips | GPIO_SUPPORT；TARGET_x86 |
| `kmod-gpio-nct5104d` | GPIO nct5104d support | GPIO_SUPPORT；TARGET_x86 |
| `kmod-hinic` | Huawei Intelligent PCIE Network Interface Card support | (TARGET_armsr_armv8\|\|TARGET_loongarch64\|\|TARGET_x86)；PCI_SUPPORT |
| `kmod-hsdma-mtk` | MediaTek HSDMA Engine | TARGET_ramips；TARGET_ramips_mt7621 |
| `kmod-hw-crypto-4xx` | Driver AMCC PPC4xx crypto accelerator | TARGET_apm821xx |
| `kmod-hwmon-coretemp` | Intel Core/Core2/Atom temperature sensor | TARGET_x86 |
| `kmod-hwmon-f71882fg` | F71882FG compatible monitoring support | TARGET_x86 |
| `kmod-hwmon-nct6775` | kmod-hwmon-nct6775 | PCI_SUPPORT；TARGET_x86 |
| `kmod-hwmon-pc87360` | PC87360 monitoring support | TARGET_x86 |
| `kmod-hwmon-raspberrypi` | Raspberry Pi voltage monitor | TARGET_bcm27xx |
| `kmod-hwmon-w83627ehf` | kmod-hwmon-w83627ehf | TARGET_x86 |
| `kmod-hwmon-w83627hf` | Winbond W83627HF monitoring support | TARGET_x86 |
| `kmod-i2c-an7581` | Airoha I2C Controller | (TARGET_airoha_an7581) |
| `kmod-i2c-bcm-iproc` | Broadcom iProc I2C controller | TARGET_bcm53xx |
| `kmod-i2c-bcm2835` | Broadcom BCM2835 I2C master controller driver | TARGET_bcm27xx |
| `kmod-i2c-brcmstb` | Broadcom BRCMSTB I2C master controller driver | TARGET_bcm27xx |
| `kmod-i2c-hid` | kmod-i2c-hid | !(PACKAGE_kmod-backlight) \|\| DISPLAY_SUPPORT；DISPLAY_SUPPORT |
| `kmod-i2c-hid-acpi` | HID over I2C transport layer ACPI driver | !(PACKAGE_kmod-backlight) \|\| DISPLAY_SUPPORT；DISPLAY_SUPPORT；TARGET_armsr_armv8\|\|TARGET_loongarch64\|\|TARGET_x86 |
| `kmod-i2c-i801` | Intel I801 and compatible I2C interfaces | !(PACKAGE_kmod-i2c-mux-gpio) \|\| PACKAGE_kmod-i2c-mux-gpio；PCI_SUPPORT；TARGET_x86 |
| `kmod-i2c-lantiq` | Lantiq I2C controller | TARGET_lantiq_falcon |
| `kmod-i2c-mlxcpld` | Mellanox I2C driver | TARGET_x86_64 |
| `kmod-i2c-mt7628` | MT7628/88 I2C Controller | (TARGET_ramips_mt76x8) |
| `kmod-i2c-mux-mlxcpld` | Mellanox CPLD based I2C multiplexer | TARGET_x86_64 |
| `kmod-i2c-piix4` | Intel PIIX4 and compatible I2C interfaces | PCI_SUPPORT；TARGET_x86 |
| `kmod-i2c-pxa` | Intel PXA I2C bus driver | Requires PXA/MMP/MVEBU or 32-bit x86; this target satisfies none of those hardware constraints. |
| `kmod-i2c-ralink` | Ralink I2C Controller | !(TARGET_ramips_mt7621\|\|TARGET_ramips_mt76x8)；TARGET_ramips |
| `kmod-ib700-wdt` | IB700 SBC Watchdog Timer | TARGET_x86 |
| `kmod-igbvf` | Intel(R) 82576 Virtual Function Ethernet support | (TARGET_loongarch64\|\|TARGET_x86)；PCI_SUPPORT |
| `kmod-iio-mt6577-auxadc` | Mediatek AUXADC driver | (TARGET_mediatek_mt7622\|\|TARGET_mediatek_filogic) |
| `kmod-iio-mxs-lradc` | Freescale i.MX23/i.MX28 LRADC ADC driver | TARGET_mxs |
| `kmod-iio-ti-am335x-adc` | TI Sitara AM335x ADC driver | TARGET_omap |
| `kmod-imx2-wdt` | NXP (Freescale) i.MX2+ and Layerscape watchdog driver | TARGET_armsr |
| `kmod-imx7-ulp-wdt` | NXP (Freescale) i.MX7ULP and later watchdog | TARGET_armsr |
| `kmod-industrialio-backend` | kmod-industrialio-backend | 未由 Kconfig 选中 |
| `kmod-intel-lpss` | kmod-intel-lpss | TARGET_x86 |
| `kmod-intel-lpss-acpi` | Intel LPSS ACPI | TARGET_x86 |
| `kmod-intel-lpss-pci` | Intel LPSS PCI | PCI_SUPPORT；TARGET_x86 |
| `kmod-irqbypass` | kmod-irqbypass | 未由 Kconfig 选中 |
| `kmod-isp-bcm2835` | BCM2835 ISP | PACKAGE_kmod-video-core；TARGET_bcm27xx |
| `kmod-it87-wdt` | ITE IT87 Watchdog Timer | TARGET_x86 |
| `kmod-itco-wdt` | Intel iTCO Watchdog Timer | TARGET_x86 |
| `kmod-keyboard-imx` | IMX keypad support | (TARGET_mxs\|\|TARGET_imx) |
| `kmod-keyboard-sx951x` | Semtech SX9512/SX9513 | TARGET_ramips_mt7621 |
| `kmod-kvm-amd` | KVM for AMD processors support | TARGET_x86_generic\|\|TARGET_x86_64 |
| `kmod-kvm-intel` | KVM for Intel processors support | TARGET_x86_generic\|\|TARGET_x86_64 |
| `kmod-kvm-x86` | Kernel-based Virtual Machine (KVM) support | TARGET_x86_generic\|\|TARGET_x86_64 |
| `kmod-leds-apu` | PC Engines APU1 LED support | GPIO_SUPPORT；TARGET_x86 |
| `kmod-leds-bcm6328` | BCM6328 LED support | TARGET_bmips |
| `kmod-leds-bcm6358` | BCM6358 LED support | TARGET_bmips |
| `kmod-leds-gca230718` | GCA230718 LED support (e.g. for D-Link M30) | TARGET_mediatek_filogic |
| `kmod-leds-mlxcpld` | LED support for the Mellanox boards | TARGET_x86 |
| `kmod-leds-reset` | reset controller LED support | TARGET_ath79 |
| `kmod-leds-sercomm-msp430` | Sercomm MSP430G2513 LED support | TARGET_bmips |
| `kmod-leds-turris-omnia` | LED support for CZ.NIC's Turris Omnia | TARGET_mvebu_cortexa9 |
| `kmod-leds-ubnt-ledbar` | Ubiquiti UniFi 6 LR LED support | TARGET_mediatek_mt7622\|\|TARGET_ramips_mt7621 |
| `kmod-leds-ws2812b` | Worldsemi WS2812B (NeoPixel) LED support | TARGET_mediatek_filogic |
| `kmod-lib-objagg` | kmod-lib-objagg | 未由 Kconfig 选中 |
| `kmod-lib-parman` | kmod-lib-parman | 未由 Kconfig 选中 |
| `kmod-libsas` | SAS Domain Transport Attributes | TARGET_x86 |
| `kmod-linkstation-poweroff` | Buffalo LinkStation power off driver | TARGET_mvebu |
| `kmod-ltq-adsl-ar9` | adsl driver for ar9 | TARGET_lantiq_xway |
| `kmod-ltq-adsl-ar9-fw-a` | Firmware Annex-a ar9 | TARGET_lantiq_xway |
| `kmod-ltq-adsl-ar9-fw-b` | Firmware Annex-b ar9 | TARGET_lantiq_xway |
| `kmod-ltq-adsl-ar9-mei` | mei driver for ar9 | TARGET_lantiq_xway |
| `kmod-ltq-adsl-ase` | adsl driver for ase | TARGET_lantiq_ase |
| `kmod-ltq-adsl-ase-fw-a` | Firmware Annex-a ase | TARGET_lantiq_ase |
| `kmod-ltq-adsl-ase-fw-b` | Firmware Annex-b ase | TARGET_lantiq_ase |
| `kmod-ltq-adsl-ase-mei` | mei driver for ase | TARGET_lantiq_ase |
| `kmod-ltq-adsl-danube` | adsl driver for danube | (TARGET_lantiq_xway\|\|TARGET_lantiq_xway_legacy) |
| `kmod-ltq-adsl-danube-fw-a` | Firmware Annex-a danube | (TARGET_lantiq_xway\|\|TARGET_lantiq_xway_legacy) |
| `kmod-ltq-adsl-danube-fw-b` | Firmware Annex-b danube | (TARGET_lantiq_xway\|\|TARGET_lantiq_xway_legacy) |
| `kmod-ltq-adsl-danube-mei` | mei driver for danube | (TARGET_lantiq_xway\|\|TARGET_lantiq_xway_legacy) |
| `kmod-ltq-atm-ar9` | atm driver for ar9 | TARGET_lantiq_xway |
| `kmod-ltq-atm-ase` | atm driver for ase | TARGET_lantiq_ase |
| `kmod-ltq-atm-danube` | atm driver for danube | (TARGET_lantiq_xway\|\|TARGET_lantiq_xway_legacy) |
| `kmod-ltq-atm-vr9` | atm driver for vr9 | (TARGET_lantiq_xrx200\|\|TARGET_lantiq_xrx200_legacy)；(TARGET_lantiq\|\|TARGET_ipq40xx) |
| `kmod-ltq-deu-ar9` | deu driver for ar9 | TARGET_lantiq_xway |
| `kmod-ltq-deu-danube` | deu driver for danube | TARGET_lantiq_xway |
| `kmod-ltq-deu-vr9` | deu driver for vr9 | (TARGET_lantiq_xrx200\|\|TARGET_lantiq_xrx200_legacy) |
| `kmod-ltq-ifxos` | Lantiq OS abstraction library | (TARGET_lantiq\|\|TARGET_ipq40xx) |
| `kmod-ltq-ptm-ar9` | ptm driver for ar9 | TARGET_lantiq_xway |
| `kmod-ltq-ptm-ase` | ptm driver for ase | BROKEN；TARGET_lantiq_ase |
| `kmod-ltq-ptm-danube` | ptm driver for danube | (TARGET_lantiq_xway\|\|TARGET_lantiq_xway_legacy)；TARGET_lantiq_xway |
| `kmod-ltq-ptm-vr9` | ptm driver for vr9 | (TARGET_lantiq_xrx200\|\|TARGET_lantiq_xrx200_legacy)；(TARGET_lantiq\|\|TARGET_ipq40xx) |
| `kmod-ltq-tapi` | Lantiq TAPI subsystem | (TARGET_lantiq_falcon\|\|TARGET_lantiq_xway\|\|TARGET_lantiq_xrx200)；(TARGET_lantiq\|\|TARGET_ipq40xx) |
| `kmod-ltq-vdsl-vr11` | vdsl driver | (TARGET_lantiq\|\|TARGET_ipq40xx)；TARGET_ipq40xx |
| `kmod-ltq-vdsl-vr11-mei` | mei driver for vdsl | (TARGET_lantiq\|\|TARGET_ipq40xx)；TARGET_ipq40xx |
| `kmod-ltq-vdsl-vr9` | vdsl driver | (TARGET_lantiq_xrx200\|\|TARGET_lantiq_xrx200_legacy)；(TARGET_lantiq\|\|TARGET_ipq40xx) |
| `kmod-ltq-vdsl-vr9-mei` | mei driver for vdsl | (TARGET_lantiq_xrx200\|\|TARGET_lantiq_xrx200_legacy)；(TARGET_lantiq\|\|TARGET_ipq40xx) |
| `kmod-ltq-vectoring` | driver for sending vectoring error samples | (TARGET_lantiq_xrx200\|\|TARGET_lantiq_xrx200_legacy) |
| `kmod-ltq-vectoring-test` | driver for testing the vectoring driver | (TARGET_lantiq_xrx200\|\|TARGET_lantiq_xrx200_legacy) |
| `kmod-ltq-vmmc` | TAPI LL driver for Voice Macro | (TARGET_lantiq_falcon\|\|TARGET_lantiq_xway\|\|TARGET_lantiq_xrx200)；(TARGET_lantiq_xway\|\|TARGET_lantiq_xrx200)；(TARGET_lantiq\|\|TARGET_ipq40xx) |
| `kmod-lttng` | Linux Trace Toolkit: next generation (kernel modules) | !TARGET_uml；KERNEL_FTRACE_SYSCALLS；KERNEL_KPROBES |
| `kmod-marvell-mdio` | Marvell Armada platform MDIO driver | !TARGET_x86；TARGET_armsr |
| `kmod-mdio-bcm-unimac` | Broadcom UniMAC MDIO bus controller | !TARGET_x86；TARGET_armsr |
| `kmod-mdio-bus-mux` | kmod-mdio-bus-mux | 未由 Kconfig 选中 |
| `kmod-mdio-thunder` | Marvell (Cavium) Thunder MDIO controller | !TARGET_x86；TARGET_armsr |
| `kmod-meraki-mx100` | Cisco Meraki MX100 Platform Driver | !(USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；(TARGET_ath79_nand\|\|TARGET_bcm53xx\|\|TARGET_x86)；GPIO_SUPPORT；PCI_SUPPORT；TARGET_x86；USB_SUPPORT |
| `kmod-mfd-ac100` | X-Powers AC100 MFD support | TARGET_sunxi |
| `kmod-mlx_wdt` | Mellanox Watchdog | TARGET_x86 |
| `kmod-mlxreg` | Mellanox platform register access | TARGET_x86；TARGET_x86_64 |
| `kmod-mlxreg-lc` | Mellanox line card platform support | PACKAGE_kmod-mlxreg |
| `kmod-mlxreg-sn2201` | Nvidia SN2201 platform support | PACKAGE_kmod-mlxreg |
| `kmod-mlxsw-core` | Mellanox Technologies Switch ASICs support | TARGET_x86_64 |
| `kmod-mlxsw-i2c` | kmod-mlxsw-i2c | TARGET_x86_64 |
| `kmod-mlxsw-minimal` | Mellanox Technologies minimal I2C support | TARGET_x86_64 |
| `kmod-mlxsw-pci` | kmod-mlxsw-pci | PCI_SUPPORT；TARGET_x86_64 |
| `kmod-mlxsw-spectrum` | Mellanox Technologies Spectrum family support | IPV6；PCI_SUPPORT；TARGET_x86_64 |
| `kmod-mmc-at91` | MMC/SD Card Support on AT91 | !TARGET_uml；TARGET_at91 |
| `kmod-mmc-mtk` | MediaTek SD/MMC Card Interface support | !TARGET_uml；(TARGET_ramips_mt7620\|\|TARGET_ramips_mt76x8\|\|TARGET_ramips_mt7621) |
| `kmod-mt7621-qtn-rgmii` | kmod-mt7621-qtn-rgmii | TARGET_ramips_mt7621 |
| `kmod-mt7981-firmware` | MediaTek MT7981 firmware | TARGET_mediatek_filogic |
| `kmod-mt7986-firmware` | MediaTek MT7986 firmware | TARGET_mediatek_filogic |
| `kmod-mvneta` | Marvell Armada 370/38x/XP/37xx network driver | !TARGET_x86；TARGET_armsr |
| `kmod-mvpp2` | Marvell Armada 375/7K/8K network driver | !TARGET_x86；TARGET_armsr |
| `kmod-mvsas` | Marvell 88SE6440 SAS/SATA driver | TARGET_x86 |
| `kmod-mvsdio` | Marvell MMC/SD/SDIO host driver | !TARGET_uml；TARGET_kirkwood |
| `kmod-mwlwifi` | Marvell 88W8864/88W8897/88W8964/88W8997 wireless driver | PCI_SUPPORT；TARGET_mvebu |
| `kmod-nvmem-stm32-romem` | STM32 factory-programmed memory support | TARGET_stm32 |
| `kmod-octeontx2-net` | Marvell (Cavium) ThunderX2 network drivers | !TARGET_x86；TARGET_armsr |
| `kmod-openvswitch-geneve-intree` | kmod-openvswitch-geneve-intree | DEVEL；IPV6 |
| `kmod-openvswitch-gre-intree` | Open vSwitch GRE tunneling support (in tree) | DEVEL；IPV6 |
| `kmod-openvswitch-intree` | Open vSwitch kernel datapath (in tree) | DEVEL；IPV6 |
| `kmod-openvswitch-lisp-intree` | kmod-openvswitch-lisp-intree | DEVEL；IPV6 |
| `kmod-openvswitch-stt-intree` | Open vSwitch STT tunneling support (in tree) | DEVEL；IPV6 |
| `kmod-openvswitch-vxlan-intree` | kmod-openvswitch-vxlan-intree | DEVEL；IPV6 |
| `kmod-pcengines-apuv2` | PC Engines APUv2/3 front button and LEDs driver | GPIO_SUPPORT；TARGET_x86 |
| `kmod-pcmcia-core` | PCMCIA/CardBus support | PCMCIA_SUPPORT |
| `kmod-pcmcia-nozomi` | Option Fusion+ card | PACKAGE_kmod-pcmcia-core |
| `kmod-pcmcia-pd6729` | Cirrus PD6729 compatible bridge support | PACKAGE_kmod-pcmcia-core |
| `kmod-pcmcia-rsrc` | PCMCIA resource support | PACKAGE_kmod-pcmcia-core |
| `kmod-pcmcia-serial` | Serial devices support | !TARGET_uml；PACKAGE_kmod-pcmcia-core |
| `kmod-pcmcia-yenta` | yenta socket driver | PACKAGE_kmod-pcmcia-core |
| `kmod-pcs-qcom-ipq9574` | Qualcomm IPQ9574 PCS driver | TARGET_qualcommbe |
| `kmod-pcs-xpcs` | Synopsis DesignWare PCS driver | !((TARGET_armsr\|\|TARGET_bcm27xx_bcm2708\|\|TARGET_loongarch64\|\|TARGET_malta\|\|TARGET_tegra)) \|\| !TARGET_x86；(TARGET_armsr\|\|TARGET_loongarch64\|\|TARGET_x86_64) |
| `kmod-pcspkr` | PC speaker support | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_x86 |
| `kmod-photonicat-pm` | Photonicat Power Manager | TARGET_rockchip_armv8 |
| `kmod-phy-ath79-usb` | kmod-phy-ath79-usb | !(USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；TARGET_ath79；USB_SUPPORT |
| `kmod-phy-bcm-ns-usb2` | Broadcom Northstar USB 2.0 PHY Driver | TARGET_bcm53xx |
| `kmod-phy-bcm-ns-usb3` | Broadcom Northstar USB 3.0 PHY Driver | TARGET_bcm53xx |
| `kmod-phy-qcom-ipq806x-usb` | Qualcomm IPQ806x DWC3 USB PHY driver | !(USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；TARGET_ipq806x；USB_SUPPORT |
| `kmod-phy-rtl8261n` | Realtek RTL8261N NBASE-T PHY driver | The downstream CONFIG_RTL8261N_PHY implementation is absent from the pinned kernel source. |
| `kmod-phy-sf19a2890-usb` | Siflower SF19A2890 USB 2.0 PHY Driver | TARGET_siflower_sf19a2890 |
| `kmod-phy-sf21-usb` | Siflower SF21 USB 2.0 PHY Driver | TARGET_siflower_sf21 |
| `kmod-phy-stm32-usbphyc` | STM32 USB HS PHY Controller driver | TARGET_stm32 |
| `kmod-ppfe` | Freescale PPFE Driver support | TARGET_layerscape |
| `kmod-ptp-qoriq` | Freescale QorIQ PTP support | (TARGET_mpc85xx\|\|TARGET_qoriq) |
| `kmod-pwm-airoha` | Airoha AN7581 and AN7583 PWM | TARGET_airoha_an7581\|\|TARGET_airoha_an7583 |
| `kmod-pwm-atmel` | PWM on atmel SoC | TARGET_at91 |
| `kmod-pwm-mediatek-ramips` | MT7628 PWM | (TARGET_ramips_mt76x8) |
| `kmod-pwm-pio-rp1` | RP1 PWM support | TARGET_bcm27xx_bcm2712 |
| `kmod-pwm-raspberrypi-poe` | Raspberry Pi Firwmware PoE Hat PWM support | PWM_SUPPORT；TARGET_bcm27xx |
| `kmod-qca-nss-dp` | Qualcom NSS dataplane ethernet driver | (TARGET_qualcommax)；TARGET_qualcommax |
| `kmod-qca-ssdk` | Qualcom SSDK switch driver | (TARGET_qualcommax) |
| `kmod-qcom-ppe` | Qualcomm PPE ethernet controller | TARGET_qualcommbe |
| `kmod-qrtr-smd` | SMD IPC Router channels | TARGET_qualcommax |
| `kmod-renesas-net-avb` | Renesas network drivers | !((TARGET_armsr\|\|TARGET_bcm27xx_bcm2708\|\|TARGET_loongarch64\|\|TARGET_malta\|\|TARGET_tegra)) \|\| !TARGET_x86；GPIO_SUPPORT；TARGET_armsr |
| `kmod-rfkill` | RF switch subsystem support | USE_RFKILL |
| `kmod-rp1` | RP1 firmware | TARGET_bcm27xx_bcm2712 |
| `kmod-rp1-adc` | RP1 ADC and temperature sensor driver | TARGET_bcm27xx_bcm2712 |
| `kmod-rp1-cfe` | RP1 Camera Front-End | TARGET_bcm27xx_bcm2712 |
| `kmod-rp1-mailbox` | RP1 mailbox IPC driver | TARGET_bcm27xx_bcm2712 |
| `kmod-rp1-pio` | RP1 PIO block support | TARGET_bcm27xx_bcm2712 |
| `kmod-rpi-panel-7inch-touchscreen` | Raspberry Pi 7-inch touchscreen panel | !(PACKAGE_kmod-backlight) \|\| DISPLAY_SUPPORT；DISPLAY_SUPPORT；TARGET_bcm27xx |
| `kmod-rpi-panel-attiny-regulator` | kmod-rpi-panel-attiny-regulator | DISPLAY_SUPPORT；TARGET_bcm27xx |
| `kmod-rt2800-soc` | Ralink Drivers for RT2x00 cards (RT28xx/RT3xxx SoC) | (PCI_SUPPORT\|\|TARGET_ramips)；(PCI_SUPPORT\|\|USB_SUPPORT\|\|TARGET_ramips)；(TARGET_ramips_rt288x\|\|TARGET_ramips_rt305x\|\|TARGET_ramips_rt3883\|\|TARGET_ramips_mt7620) |
| `kmod-rtc-ac100` | X-Powers AC100 RTC support | TARGET_sunxi |
| `kmod-rtc-mv` | Marvell SoC RTC support | Requires ARCH_DOVE or ARCH_MVEBU, which is a different SoC family. |
| `kmod-rtc-rv5c386a` | Driver for RTC RV5C386A (used in WL-700gE and WL-HDD) | !IN_SDK；TARGET_bcm47xx |
| `kmod-rtc-sunxi` | Sunxi SoC built-in RTC support | (TARGET_sunxi&&RTC_SUPPORT) |
| `kmod-saradc-rockchip` | Rockchip SARADC support | TARGET_rockchip |
| `kmod-scmi-hwmon` | ARM SCMI Sensors | TARGET_stm32 |
| `kmod-scmi-iio` | IIO SCMI | TARGET_stm32 |
| `kmod-sdhci-mt7620` | MT7620 SDCI | !TARGET_uml；(TARGET_ramips_mt7620\|\|TARGET_ramips_mt76x8\|\|TARGET_ramips_mt7621)；m \|\| (PACKAGE_kmod-mmc-mtk != y) |
| `kmod-smi-bcm2835` | BCM2835 SMI driver | TARGET_bcm27xx |
| `kmod-smi-bcm2835-dev` | BCM2835 SMI device driver | TARGET_bcm27xx |
| `kmod-sound-arm-bcm2835` | BCM2835 ALSA driver | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_bcm27xx |
| `kmod-sound-cs5535audio` | CS5535/CS5536 Audio Controller | !TARGET_uml；(TARGET_x86_geode\|\|TARGET_x86_legacy)；PACKAGE_kmod-sound-core |
| `kmod-sound-mt7620` | MT7620 PCM/I2S Alsa Driver | !TARGET_ramips_rt288x；!TARGET_uml；PACKAGE_kmod-sound-core；TARGET_ramips |
| `kmod-sound-soc-adau1977-adc` | Support for ADAU1977 ADC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-allo-boss-dac` | Support for Allo Boss DAC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-allo-boss2-dac` | Support for Allo Boss2 DAC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-allo-digione` | Support for Allo Piano DigiOne | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-allo-katana-codec` | Support for Allo Katana DAC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-allo-piano-dac` | Support for Allo Piano DAC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-allo-piano-dac-plus` | Support for Allo Piano DAC Plus | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-audioinjector-isolated-soundcard` | kmod-sound-soc-audioinjector-isolated-soundcard | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-audioinjector-octo-soundcard` | kmod-sound-soc-audioinjector-octo-soundcard | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-audioinjector-pi-soundcard` | kmod-sound-soc-audioinjector-pi-soundcard | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-audiosense-pi` | Support for AudioSense Add-On Soundcard | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-bcm2835-i2s` | kmod-sound-soc-bcm2835-i2s | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_bcm27xx |
| `kmod-sound-soc-chipdip-dac` | Support for ChipDip DAC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s |
| `kmod-sound-soc-dacberry-soundcard` | Support for DACBERRY400 Soundcard | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-digidac1-soundcard` | Support for RRA DigiDAC1 | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-dionaudio-loco` | Support for Dion Audio LOCO DAC-AMP | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s |
| `kmod-sound-soc-dionaudio-loco-v2` | Support for Dion Audio LOCO-V2 DAC-AMP | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s |
| `kmod-sound-soc-fe-pi` | Support for Fe-Pi Audio Sound Card | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s |
| `kmod-sound-soc-googlevoicehat` | Support for Google VoiceHAT Sound Card | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s |
| `kmod-sound-soc-hifiberry-adc` | Support for HifiBerry ADC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-hifiberry-amp` | Support for HifiBerry Amp | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-hifiberry-dac` | Support for HifiBerry DAC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-hifiberry-dacplus` | kmod-sound-soc-hifiberry-dacplus | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-hifiberry-dacplusadc` | Support for HifiBerry DAC+ADC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-hifiberry-dacplusadc-pro` | kmod-sound-soc-hifiberry-dacplusadc-pro | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-hifiberry-dacplusdsp` | Support for HifiBerry DAC+DSP | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s |
| `kmod-sound-soc-hifiberry-dacplushd` | Support for HifiBerry DAC+HD | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-hifiberry-digi` | kmod-sound-soc-hifiberry-digi | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-i-sabe-q2m` | Support for Audiophonics I-Sabre Q2M DAC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-imx` | IMX SoC support | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_imx |
| `kmod-sound-soc-imx-sgtl5000` | IMX SoC support for SGTL5000 | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_imx |
| `kmod-sound-soc-ipq8064-storm` | kmod-sound-soc-ipq8064-storm | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_ipq806x |
| `kmod-sound-soc-iqaudio-codec` | Support for IQaudIO-CODEC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-iqaudio-dac` | Support for IQaudIO-DAC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-iqaudio-digi` | Support for IQaudIO-DIGI | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-justboom-both` | Support for JustBoom DAC and Digi | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-justboom-dac` | Support for JustBoom DAC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-justboom-digi` | Support for JustBoom Digi | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-merus-amp` | Support for Infineon Merus Amp | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-mt7986` | MediaTek MT7986 Audio support | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_mediatek_filogic |
| `kmod-sound-soc-mt7986-wm8960` | MediaTek MT7986 Audio support | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_mediatek_filogic |
| `kmod-sound-soc-pifi-40-amp` | Support for PiFi-40 amp | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s |
| `kmod-sound-soc-pisound` | Support for Blokas Labs PiSound | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s |
| `kmod-sound-soc-rpi-cirrus` | Support for Cirrus Logic Audio Card | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-rpi-dac` | Support for RPi-DAC | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-rpi-proto` | Support for RPi-PROTO | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s；TARGET_bcm27xx |
| `kmod-sound-soc-rpi-simple-soundcard` | kmod-sound-soc-rpi-simple-soundcard | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s |
| `kmod-sound-soc-rpi-wm8804-soundcard` | kmod-sound-soc-rpi-wm8804-soundcard | !TARGET_uml；PACKAGE_kmod-sound-core；PACKAGE_kmod-sound-soc-bcm2835-i2s |
| `kmod-sound-soc-stm32-dfsdm` | SoC Audio support for STM32 DFSDM | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_stm32 |
| `kmod-sound-soc-stm32-i2s` | STM32 I2S interface (SPI/I2S block) support | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_stm32 |
| `kmod-sound-soc-stm32-sai` | kmod-sound-soc-stm32-sai | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_stm32 |
| `kmod-sound-soc-stm32-spdifrx` | STM32 S/PDIF receiver (SPDIFRX) support | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_stm32 |
| `kmod-sound-soc-sunxi` | AllWinner built-in SoC sound support | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_sunxi |
| `kmod-sound-soc-sunxi-spdif` | Allwinner A10 SPDIF Support | !TARGET_uml；PACKAGE_kmod-sound-core；TARGET_sunxi |
| `kmod-sp5100-tco` | SP5100 Watchdog Support | TARGET_x86 |
| `kmod-sparx5-switch` | Sparx5 switch driver | TARGET_microchipsw |
| `kmod-spi-bcm2835` | BCM2835 SPI controller driver | TARGET_bcm27xx |
| `kmod-spi-bcm2835-aux` | BCM2835 Aux SPI controller driver | TARGET_bcm27xx |
| `kmod-spi-stm32` | STM32 SPI controller | TARGET_stm32 |
| `kmod-st-thermal` | Thermal sensors on STMicroelectronics STi series of SoCs | TARGET_stm32 |
| `kmod-stm32-adc` | STM32 ADC | TARGET_stm32 |
| `kmod-stm32-crc32` | Support for STM32 crc accelerators | TARGET_stm32 |
| `kmod-stm32-cryp` | Support for STM32 cryp accelerators | TARGET_stm32 |
| `kmod-stm32-dac` | STM32 DAC | TARGET_stm32 |
| `kmod-stm32-dcmi` | STM32 Digital Camera Memory Interface support | PACKAGE_kmod-video-core；TARGET_stm32 |
| `kmod-stm32-dcmipp` | kmod-stm32-dcmipp | PACKAGE_kmod-video-core；TARGET_stm32 |
| `kmod-stm32-dfsdm-adc` | STM32 DFSDM ADC | TARGET_stm32 |
| `kmod-stm32-hash` | Support for STM32 hash accelerators | TARGET_stm32 |
| `kmod-stm32-thermal` | kmod-stm32-thermal | TARGET_stm32_stm32mp1 |
| `kmod-stm32-timer-trigger` | STM32 Timer Trigger | TARGET_stm32 |
| `kmod-stm32-timers` | STM32 Timers | TARGET_stm32 |
| `kmod-stmmac-core` | Synopsis Ethernet Controller core (NXP,STMMicro,others) | !((TARGET_armsr\|\|TARGET_bcm27xx_bcm2708\|\|TARGET_loongarch64\|\|TARGET_malta\|\|TARGET_tegra)) \|\| !TARGET_x86；(TARGET_armsr\|\|TARGET_loongarch64\|\|TARGET_x86_64) |
| `kmod-sun4i-emac` | AllWinner EMAC Ethernet support | !TARGET_x86；TARGET_sunxi |
| `kmod-sunxi-ir` | Sunxi SoC built-in IR support | (TARGET_sunxi&&RTC_SUPPORT) |
| `kmod-switch-rtl8367s` | Realtek RTL8367S switch support | TARGET_mediatek |
| `kmod-thunderx-net` | Marvell (Cavium) Thunder network drivers | !TARGET_x86；TARGET_armsr；TARGET_armsr_armv8 |
| `kmod-tpm-tis` | TPM TIS 1.2 Interface / TPM 2.0 FIFO Interface | (TARGET_x86\|\|TARGET_armsr\|\|TARGET_imx) |
| `kmod-tpm-tis-spi` | TPM TIS 1.3 Interface SPI Interface | (TARGET_x86\|\|TARGET_armsr\|\|TARGET_imx) |
| `kmod-turris-omnia-mcu` | CZ.NIC's Turris Omnia MCU driver | TARGET_mvebu_cortexa9 |
| `kmod-usb-bcma` | kmod-usb-bcma | !(USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；TARGET_bcm47xx\|\|TARGET_bcm53xx；USB_SUPPORT |
| `kmod-usb-chipidea` | Host and device support for Chipidea controllers | !(USB_GADGET_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；!(USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；TARGET_ath79；USB_SUPPORT；USB_SUPPORT\|\|USB_GADGET_SUPPORT |
| `kmod-usb-chipidea2` | Host and device support for Chipidea2 controllers | !(USB_GADGET_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；!(USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；TARGET_ath79；USB_SUPPORT；USB_SUPPORT\|\|USB_GADGET_SUPPORT |
| `kmod-usb-dwc3-octeon` | DWC3 Cavium Octeon USB driver | !(USB_GADGET_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；!(USB_SUPPORT && USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；!(USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；TARGET_octeon；USB_SUPPORT；USB_SUPPORT\|\|USB_GADGET_SUPPORT |
| `kmod-usb-dwc3-qcom` | DWC3 Qualcomm USB driver | !(USB_GADGET_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；!(USB_SUPPORT && USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；!(USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；(TARGET_ipq40xx\|\|TARGET_ipq806x\|\|TARGET_qualcommax\|\|TARGET_qualcommbe)；USB_SUPPORT；USB_SUPPORT\|\|USB_GADGET_SUPPORT |
| `kmod-usb-fotg210` | Support for FOTG210 USB host and device controllers | !(USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；TARGET_gemini；USB_SUPPORT |
| `kmod-usb-gadget` | kmod-usb-gadget | (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；USB_GADGET_SUPPORT |
| `kmod-usb-gadget-cdc-composite` | USB CDC Composite (Ethernet + ACM) | (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；USB_GADGET_SUPPORT |
| `kmod-usb-gadget-ehci-debug` | USB EHCI debug port Gadget support | (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；USB_GADGET_SUPPORT |
| `kmod-usb-gadget-eth` | USB Ethernet Gadget support | (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；USB_GADGET_SUPPORT |
| `kmod-usb-gadget-fs` | USB FunctionFS Gadget Support | (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；USB_GADGET_SUPPORT |
| `kmod-usb-gadget-hid` | USB HID Gadget Support | (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；USB_GADGET_SUPPORT |
| `kmod-usb-gadget-mass-storage` | USB Mass Storage support | (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；USB_GADGET_SUPPORT |
| `kmod-usb-gadget-ncm` | USB Network Control Model (NCM) Gadget support | (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；USB_GADGET_SUPPORT |
| `kmod-usb-gadget-serial` | USB Serial Gadget support | (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；USB_GADGET_SUPPORT |
| `kmod-usb-lib-composite` | kmod-usb-lib-composite | (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；USB_GADGET_SUPPORT |
| `kmod-usb-net2280` | Support for NetChip 228x PCI USB peripheral controller | (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；PCI_SUPPORT；USB_GADGET_SUPPORT；USB_SUPPORT |
| `kmod-usb-ssb` | kmod-usb-ssb | !(USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；TARGET_bcm47xx；USB_SUPPORT |
| `kmod-usb-test` | USB Testing Driver | !(USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；DEVEL；USB_SUPPORT |
| `kmod-usb-xhci-mtk` | kmod-usb-xhci-mtk | !(USB_SUPPORT) \|\| (USB_SUPPORT\|\|USB_GADGET_SUPPORT)；USB_SUPPORT |
| `kmod-vc-sm-cma` | VideoCore Shared Memory (CMA) driver | PACKAGE_kmod-video-core；TARGET_bcm27xx |
| `kmod-vchiq-mmal-bcm2835` | BCM2835 MMAL VCHIQ service | PACKAGE_kmod-video-core；TARGET_bcm27xx |
| `kmod-vfio` | VFIO Non-Privileged userspace driver framework | TARGET_x86_64\|\|TARGET_armsr_armv8 |
| `kmod-vfio-pci` | Generic VFIO support for any PCI device | PCI_SUPPORT；TARGET_x86_64\|\|TARGET_armsr_armv8 |
| `kmod-video-async` | kmod-video-async | PACKAGE_kmod-video-core |
| `kmod-video-coda` | i.MX VPU support | (TARGET_imx&&TARGET_imx_cortexa9)；PACKAGE_kmod-video-core |
| `kmod-video-fwnode` | kmod-video-fwnode | PACKAGE_kmod-video-core |
| `kmod-video-mem2mem` | kmod-video-mem2mem | PACKAGE_kmod-video-core |
| `kmod-video-pxp` | i.MX PXP support | PACKAGE_kmod-video-core；TARGET_imx |
| `kmod-vrx518_ep` | VRX518 EP Support | TARGET_ipq40xx |
| `kmod-vrx518_tc` | VRX518 TC driver | TARGET_ipq40xx |
| `kmod-vsock-virtio` | Virtio transport driver for Virtual Sockets | VIRTIO_SUPPORT |
| `kmod-vsock-virtio-common` | kmod-vsock-virtio-common | 未由 Kconfig 选中 |
| `kmod-w1-master-mxc` | Freescale MXC 1-wire busmaster | PACKAGE_kmod-w1；TARGET_imx |
| `kmod-w83627hf-wdt` | Winbond 83627HF Watchdog Timer | TARGET_x86 |
| `kmod-wdt-sp805` | ARM SP805 Watchdog | TARGET_armsr |
| `kmod-ws2812-pio-rp1` | RP1 PIO-base WS2812 driver | TARGET_bcm27xx_bcm2712 |
| `kmod-xdp-sockets-diag` | kmod-xdp-sockets-diag | KERNEL_XDP_SOCKETS |

## 报告与签名

`all-kmods44-report.json` 记录构建产出的原始 APK；软件源重签后文件字节会变化，已发布 APK 的大小和 SHA256 以同目录 `manifest.json` 为准。两者的 kernel ABI 和包名必须一致。

主要证据：`reports/all-kmods44-report.json`、`reports/kernel-files-final44.json`、`reports/module-audit-final44.json`、`reports/feed-privacy-final44.json`。
