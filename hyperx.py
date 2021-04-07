# Memory Part Number Decoder: https://www.hyperxgaming.com/unitedstates/en/decoder

PRODUCTS = {
            # Microphones
            "SOLOCAST": "HMIS1X-XX-BK/G",
            "QUADCAST": "HX-MICQC-BK",
            "QUADCAST S": "HMIQ1S-XX-RG/G",
            "CLOUD EARBUDS": "HX-HSCEB-RD",
            "CLOUD BUDS": "HEBBXX-MC-RD/G",

            # Power
            "CHARGEPLAY DUO": "HX-CPDUX-G (XBOX) HX-CPDU-G (PS4)",
            "CHARGEPLAY QUAD": "HX-CPQD-U",
            "CHARGEPLAY CLUTCH": "HX-CPCS-U (SWITCH) HX-CPCM-U (MOBILE)",
            "CHARGEPLAY BASE": "HX-CPBS-G",

            # Headphones
            "CLOUD REVOLVER": "HHSR1-AH-GM/G (7.1) HX-HSCR-GM (original)",
            "CLOUD": "HHSC2X-BA-RD/G",
            "CLOUD MIX": "HX-HSCAM-GM",
            "CLOUD CORE": "HX-HSCC-2-BK/WW",
            "CLOUD II WIRELESS": "HHSC2X-BA-RD/G",
            "CLOUD II": "KHX-HSCP-RD",
            "CLOUD ORBIT": "HX-HSCO-GM/WW",
            "CLOUD ORBIT S": "HX-HSCOS-GM/WW",
            "CLOUD STINGER": "HX-HSCS-BK/EM (PC) HX-HSCLS-BL/EM (PS4)",
            "CLOUD STINGER S": "HHSS1S-AA-BK/G (PC)",
            "CLOUD STINGER WIRELESS": "HX-HSCSW2-BK/WW (PC)",
            "CLOUD STINGER CORE": "HX-HSCSC2-BK/WW (PC) HX-HSCSC-BK (PS4)",
            "CLOUD STINGER CORE WIRELESS": "HHSS1C-BA-BK/G (PC+7.1) HHSS1C-KB-WT/G (PS4)",
            "CLOUD ALPHA S": "HX-HSCAS-BK/WW",
            "CLOUD ALPHA": "HX-HSCA-RD/EM",
            "CLOUDX STINGER CORE": "HX-HSCSCX-BK (XBOX) ",
            "CLOUDX STINGER": "HX-HSCSX-BK/WW (PC) HX-HSCSX-BK/WW (XBOX) ",
            "CLOUDX CHAT": "HX-HSCCHX-BK/WW (PC) HX-HSCCHS-BK/EM (PS4)",
            "CLOUD FLIGHT S": "HX-HSCFS-SG/WW",
            "CLOUD FLIGHT": "HX-HSCF-BK/EM",

            # Headphone Accessories
            "CONTROLLER BOX": "HXS-HSCB1",
            "CLOUD EARBUDS EAR TIPS": "HXS-HSCEB-RD-ET-L (large) HXS-HSCEB-RD-ET-M (medium) HXS-HSCEB-RD-ET-SM (small)",
            "DUAL 3.5MM PC EXTENSION CABLE": "HXS-HSEC1",
            "CLOUD STINGER WIRELESS ADAPTER": "HXS-HSWA-CSW",
            "CLOUD HEADSET CARRYING CASE": "HXS-HSCC1/EM",
            "CLOUD EARBUDS CARRYING CASE": "HXS-HSCEB-BK-CC",
            "CLOUD EAR CUSHIONS": "HXS-HSEP1 (Black/ Red) HXS-HSEP2 (Black) HXS-HSEP3 (Black/Green)",
            "CLOUD MICROPHONE": "HXS-HSMC1",
            "CLOUD MESH BAG": "HXS-HSBG",
            "CLOUD MIX DETACHABLE CABLE": "HXS-HSDC1",
            "4 POLE TO DUAL 3.5MM PC EXTENSION CABLE": "HXS-HSEC2",
            "CLOUD ALPHA EAR CUSHIONS": "HXS-HSEP4",
            "CLOUD REVOLVER EAR CUSHIONS": "HXS-HSEP5",
            "CLOUD STINGER EAR CUSHIONS": "HXS-HSEP6",
            "3.5MM HEADPHONE CABLE, CLOUD FLIGHT": "HXS-HSHC-CF",
            "CLOUD REVOLVER MICROPHONE": "HXS-HSMC2",
            "CLOUD MICROPHONE (CONSOLE)": "HXS-HSMC3",
            "CLOUD MIX MICROPHONE": "HXS-HSMC4",
            "CLOUD ALPHA MICROPHONE": "HXS-HSMC-CA",
            "CLOUD FLIGHT MICROPHONE": "HXS-HSMC-CF",
            "CLOUD MIX EAR CUSHIONS": "HXS-HSCAM-EP1",
            "CLOUD FLIGHT EAR CUSHIONS": "HXS-HSCF-EP1",
            "CLOUD ALPHA S EAR CUSHIONS": "HXS-HSCAS-EP1 (Leatherette) HXS-HSCAS-EP2 (Fabric)",
            "CLOUD FLIGHT S EAR CUSHIONS": "HXS-HSCFS-EP1",

            # Apparel
            "GG HOODIE": "https://www.hyperxgaming.com/unitedkingdom/en/apparel/gg-hoodie?color=red&size=s",
            "GG TEE": "https://www.hyperxgaming.com/unitedkingdom/en/apparel/gg-tee",
            "GG HAT": "https://www.hyperxgaming.com/unitedkingdom/en/apparel/gg-hat",
            "GG MASK": "https://www.hyperxgaming.com/unitedkingdom/en/apparel/gg-mask",

            # Keyboards
            "ALLOY CORE RGB": "HX-KB5ME2-UK",
            "ALLOY FPS": "HX-KB4RD1-US/R1 (MX Red) HX-KB4BL1-US/WW (MX Blue)",
            "ALLOY FPS PRO": "HX-KB4RD1-US/R1 (MX Red) HX-KB4BL1-US/WW (MX Blue)",
            "ALLOY FPS RGB": "HX-KB1SS2-UK",
            "ALLOY ORIGINS CORE": "HX-KB7AQX-US",
            "ALLOY ORIGINS": "HX-KB6RDX-UK",
            "ALLOY ORIGINS 60": "HKBO1S-RB-US/G",
            "ALLOY ELITE RGB": "HX-KB2RD2-UK/R1 https://media.kingston.com/support/downloads/HyperX-Alloy-Elite-RGB-keyboard-user-manual.pdf",
            "ALLOY ELITE 2": "HKBE2X-1X-UK/G",

            # Keyboard Accessories
            "HYPERX PUDDING KEYCAPS": "HKCPXP-BK-US/G (black) HKCPXP-WT-US/G (white)",
            "HYPERX WRIST WREST": "HX-WR",
            "ABS PUDDING KEYCAPS": "HKCPXA-BK-UK/G (full set)",

            # RAM
            "FURY DDR4 RGB": "HX424C15FB3A/8 https://www.hyperxgaming.com/unitedkingdom/en/memory/fury-ddr4-rgb",
            "FURY DDR4": "HX424C15FB3A/8 https://www.hyperxgaming.com/unitedkingdom/en/memory/fury-ddr4",
            "FURY DDR3": "HX316LC10FB/4 https://www.hyperxgaming.com/unitedkingdom/en/memory/fury-ddr3",
            "PREDATOR DDR4 RGB": "HX429C15PB3A/8 https://www.hyperxgaming.com/unitedkingdom/en/memory/predator-ddr4-rgb",
            "PREDATOR DDR4": "HX424C12PB3/8 https://www.hyperxgaming.com/unitedkingdom/en/memory/predator-ddr4",
            "IMPACT DDR4": "https://www.hyperxgaming.com/unitedkingdom/en/memory/impact-ddr4",
            "IMPACT DDR3": "HX316LS9IB/4 https://www.hyperxgaming.com/unitedkingdom/en/memory/impact-ddr3",

            # Mice
            "PULSEFIRE FPS PRO": "HX-MC003B",
            "PULSEFIRE SURGE": "HX-MC002B",
            "PULSEFIRE CORE": "HX-MC004B",
            "PULSEFIRE HASTE": "HMSH1-A-BK/G",
            "PULSEFIRE RAID": "HX-MC005B",
            "PULSEFIRE DART": "HX-MC006B",

            # Mouse Pads
            "FURY ULTRA RGB": "HX-MPFU-M",
            "FURY S MOUSE PAD": "HX-MPFS-M",
            "FURY S": "HX-MPFS-M",
            "FURY S SPEED": "HX-MPFS-S-M",

            # Storage
            "HYPERX GAMING MICROSD CARD": "HXSDC/256GB",

            # Eyewear
            "SPECTRE REACT": "HMC-GL-E03SM211",
            "SPECTRE 1ST EDITION": "HMC-GL-E01ML114",

            # Best Device
            "Mini Fridge": "HX-MF-PLEASE/UK"

            }
