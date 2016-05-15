import xbmc, xbmcaddon, xbmcgui, os
from descriptionparserfactory import *
from util import *

addon = xbmcaddon.Addon(id='plugin.program.iarl')

wizard_data = {
			'settings' : {  'iarl_external_user_external_env' : addon.getSetting('iarl_external_user_external_env'),
							'iarl_external_launch_close_kodi' : addon.getSetting('iarl_external_launch_close_kodi'),
							'iarl_path_to_retroarch' : addon.getSetting('iarl_path_to_retroarch'),
							'iarl_path_to_retroarch_cfg' : addon.getSetting('iarl_path_to_retroarch_cfg'),
							'iarl_additional_emulator_1_type' : addon.getSetting('iarl_additional_emulator_1_type'),
							'iarl_additional_emulator_1_path' : addon.getSetting('iarl_additional_emulator_1_path'),
							'iarl_additional_emulator_2_type' : addon.getSetting('iarl_additional_emulator_2_type'),
							'iarl_additional_emulator_2_path' : addon.getSetting('iarl_additional_emulator_2_path'),
							'iarl_wizard_launcher_group' : addon.getSetting('iarl_wizard_launcher_group'),
						},
										#Most Playable, Balanced, Accurate
			'OSX' : { '32X_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Amiga_CD32_Full' : ['FS-UAE Launcher','FS-UAE Launcher','FS-UAE Launcher'],
							'Amiga_Full_ZRL' : ['FS-UAE Launcher','FS-UAE Launcher','FS-UAE Launcher'],
							'Amiga_Bestof' : ['FS-UAE Launcher','FS-UAE Launcher','FS-UAE Launcher'],
							'Atari_2600_Bestof_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris_Full' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_7800_ZachMorris' : ['RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)'],
							'Atari_Jaguar_ZachMorris' : ['RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)'],
							'Atari_Lynx_ZachMorris' : ['RetroArch Handy (Lynx)','RetroArch Handy (Lynx)','RetroArch Mednafen Lynx (Lynx)'],
							'C64_ZachMorris' : ['RetroArch MAME C64 Softlist (Commodore 64)','RetroArch MAME C64 Softlist (Commodore 64)','RetroArch MAME C64 Softlist (Commodore 64)'],
							'C64_ZachMorris_Full' : ['RetroArch MAME C64 Softlist (Commodore 64)','RetroArch MAME C64 Softlist (Commodore 64)','RetroArch MAME C64 Softlist (Commodore 64)'],
							'Colecovision_ZachMorris' : ['RetroArch MAME Coleco Softlist (ColecoVision)','RetroArch MAME Coleco Softlist (ColecoVision)','RetroArch MAME Coleco Softlist (ColecoVision)'],
							'Colecovision_ZachMorris_Full' : ['RetroArch MAME Coleco Softlist (ColecoVision)','RetroArch MAME Coleco Softlist (ColecoVision)','RetroArch MAME Coleco Softlist (ColecoVision)'],
							'Game_Gear_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'GB_Classic_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GB_Classic_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBA_Bestof_ZachMorris' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBA_ZachMorris_Full' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBA_ZachMorris' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBC_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBC_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'Genesis_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'IA_MSDOS_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'Magnavox_O2_ZachMorris' : ['RetroArch O2EM (Odyssey2/Videopac)','RetroArch O2EM (Odyssey2/Videopac)','RetroArch O2EM (Odyssey2/Videopac)'],
							'MAME_Bestof_ZachMorris' : ['RetroArch MAME (Arcade)','RetroArch MAME (Arcade)','RetroArch MAME (Arcade)'],
							'MAME_ZachMorris' : ['RetroArch MAME (Arcade)','RetroArch MAME (Arcade)','RetroArch MAME (Arcade)'],
							'Master_System_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'MSX_ZachMorris' : ['RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)'],
							'N64_Bestof_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris_Full' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'Neo_Geo_CD_ZachMorris' : ['RetroArch MAME NeoCD Softlist (Neo Geo CD)','RetroArch MAME NeoCD Softlist (Neo Geo CD)','RetroArch MAME NeoCD Softlist (Neo Geo CD)'],
							'NES_Bestof_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris_Full' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NGPC_ZachMorris' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'NGPC_ZachMorris_Full' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'Point_and_Click_Bestof_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'PS1_Bestof_ZachMorris' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris_Full' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'Sega_CD_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Sega_Saturn_ZachMorris' : ['RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)'],
							'Sega_SG1000_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Sega_SG1000_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'SNES_Bestof_ZachMorris' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'SNES_ZachMorris' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'SNES_ZachMorris_Full' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'TG16_Bestof_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris_Full' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'ZX_Spectrum_ZachMorris' : ['RetroArch FUSE (Spectrum)','RetroArch FUSE (Spectrum)','RetroArch FUSE (Spectrum)'],
							'x68000_ZachMorris' : ['RetroArch MAME X68k Softlist (x68000)','RetroArch MAME X68k Softlist (x68000)','RetroArch MAME X68k Softlist (x68000)'],
							'x68000_ZachMorris_Full' : ['RetroArch MAME X68k Softlist (x68000)','RetroArch MAME X68k Softlist (x68000)','RetroArch MAME X68k Softlist (x68000)'],
							},
			'Windows' : { '32X_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Amiga_CD32_Full' : ['FS-UAE Launcher','FS-UAE Launcher','FS-UAE Launcher'],
							'Amiga_Full_ZRL' : ['FS-UAE Launcher','FS-UAE Launcher','FS-UAE Launcher'],
							'Amiga_Bestof' : ['FS-UAE Launcher','FS-UAE Launcher','FS-UAE Launcher'],
							'Atari_2600_Bestof_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris_Full' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_7800_ZachMorris' : ['RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)'],
							'Atari_Jaguar_ZachMorris' : ['RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)'],
							'Atari_Lynx_ZachMorris' : ['RetroArch Handy (Lynx)','RetroArch Handy (Lynx)','RetroArch Mednafen Lynx (Lynx)'],
							'C64_ZachMorris' : ['RetroArch MAME C64 Softlist (Commodore 64)','RetroArch MAME C64 Softlist (Commodore 64)','RetroArch MAME C64 Softlist (Commodore 64)'],
							'C64_ZachMorris_Full' : ['RetroArch MAME C64 Softlist (Commodore 64)','RetroArch MAME C64 Softlist (Commodore 64)','RetroArch MAME C64 Softlist (Commodore 64)'],
							'Colecovision_ZachMorris' : ['RetroArch MAME Coleco Softlist (ColecoVision)','RetroArch MAME Coleco Softlist (ColecoVision)','RetroArch MAME Coleco Softlist (ColecoVision)'],
							'Colecovision_ZachMorris_Full' : ['RetroArch MAME Coleco Softlist (ColecoVision)','RetroArch MAME Coleco Softlist (ColecoVision)','RetroArch MAME Coleco Softlist (ColecoVision)'],
							'Game_Gear_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'GB_Classic_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GB_Classic_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBA_Bestof_ZachMorris' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBA_ZachMorris_Full' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBA_ZachMorris' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBC_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBC_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'Genesis_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'IA_MSDOS_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'Magnavox_O2_ZachMorris' : ['RetroArch O2EM (Odyssey2/Videopac)','RetroArch O2EM (Odyssey2/Videopac)','RetroArch O2EM (Odyssey2/Videopac)'],
							'MAME_Bestof_ZachMorris' : ['RetroArch MAME (Arcade)','RetroArch MAME (Arcade)','RetroArch MAME (Arcade)'],
							'MAME_ZachMorris' : ['RetroArch MAME (Arcade)','RetroArch MAME (Arcade)','RetroArch MAME (Arcade)'],
							'Master_System_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'MSX_ZachMorris' : ['RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)'],
							'N64_Bestof_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris_Full' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'Neo_Geo_CD_ZachMorris' : ['RetroArch MAME NeoCD Softlist (Neo Geo CD)','RetroArch MAME NeoCD Softlist (Neo Geo CD)','RetroArch MAME NeoCD Softlist (Neo Geo CD)'],
							'NES_Bestof_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris_Full' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NGPC_ZachMorris' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'NGPC_ZachMorris_Full' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'Point_and_Click_Bestof_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'PS1_Bestof_ZachMorris' : ['RetroArch Mednafen PSX (PS1)','RetroArch Mednafen PSX (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris_Full' : ['RetroArch Mednafen PSX (PS1)','RetroArch Mednafen PSX (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris' : ['RetroArch Mednafen PSX (PS1)','RetroArch Mednafen PSX (PS1)','RetroArch Mednafen PSX (PS1)'],
							'Sega_CD_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Sega_Saturn_ZachMorris' : ['RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)'],
							'Sega_SG1000_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Sega_SG1000_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'SNES_Bestof_ZachMorris' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'SNES_ZachMorris' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'SNES_ZachMorris_Full' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'TG16_Bestof_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris_Full' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'ZX_Spectrum_ZachMorris' : ['RetroArch FUSE (Spectrum)','RetroArch FUSE (Spectrum)','RetroArch FUSE (Spectrum)'],
							'x68000_ZachMorris' : ['RetroArch MAME X68k Softlist (x68000)','RetroArch MAME X68k Softlist (x68000)','RetroArch MAME X68k Softlist (x68000)'],
							'x68000_ZachMorris_Full' : ['RetroArch MAME X68k Softlist (x68000)','RetroArch MAME X68k Softlist (x68000)','RetroArch MAME X68k Softlist (x68000)'],
							},
			'Linux/Kodibuntu' : { '32X_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Amiga_CD32_Full' : ['FS-UAE Launcher','FS-UAE Launcher','FS-UAE Launcher'],
							'Amiga_Full_ZRL' : ['FS-UAE Launcher','FS-UAE Launcher','FS-UAE Launcher'],
							'Amiga_Bestof' : ['FS-UAE Launcher','FS-UAE Launcher','FS-UAE Launcher'],
							'Atari_2600_Bestof_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris_Full' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_7800_ZachMorris' : ['RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)'],
							'Atari_Jaguar_ZachMorris' : ['RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)'],
							'Atari_Lynx_ZachMorris' : ['RetroArch Handy (Lynx)','RetroArch Handy (Lynx)','RetroArch Mednafen Lynx (Lynx)'],
							'C64_ZachMorris' : ['RetroArch MAME C64 Softlist (Commodore 64)','RetroArch MAME C64 Softlist (Commodore 64)','RetroArch MAME C64 Softlist (Commodore 64)'],
							'C64_ZachMorris_Full' : ['RetroArch MAME C64 Softlist (Commodore 64)','RetroArch MAME C64 Softlist (Commodore 64)','RetroArch MAME C64 Softlist (Commodore 64)'],
							'Colecovision_ZachMorris' : ['RetroArch MAME Coleco Softlist (ColecoVision)','RetroArch MAME Coleco Softlist (ColecoVision)','RetroArch MAME Coleco Softlist (ColecoVision)'],
							'Colecovision_ZachMorris_Full' : ['RetroArch MAME Coleco Softlist (ColecoVision)','RetroArch MAME Coleco Softlist (ColecoVision)','RetroArch MAME Coleco Softlist (ColecoVision)'],
							'Game_Gear_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'GB_Classic_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GB_Classic_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBA_Bestof_ZachMorris' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBA_ZachMorris_Full' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBA_ZachMorris' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBC_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBC_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'Genesis_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'IA_MSDOS_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'Magnavox_O2_ZachMorris' : ['RetroArch O2EM (Odyssey2/Videopac)','RetroArch O2EM (Odyssey2/Videopac)','RetroArch O2EM (Odyssey2/Videopac)'],
							'MAME_Bestof_ZachMorris' : ['RetroArch MAME (Arcade)','RetroArch MAME (Arcade)','RetroArch MAME (Arcade)'],
							'MAME_ZachMorris' : ['RetroArch MAME (Arcade)','RetroArch MAME (Arcade)','RetroArch MAME (Arcade)'],
							'Master_System_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'MSX_ZachMorris' : ['RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)'],
							'N64_Bestof_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris_Full' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'Neo_Geo_CD_ZachMorris' : ['RetroArch MAME NeoCD Softlist (Neo Geo CD)','RetroArch MAME NeoCD Softlist (Neo Geo CD)','RetroArch MAME NeoCD Softlist (Neo Geo CD)'],
							'NES_Bestof_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris_Full' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NGPC_ZachMorris' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'NGPC_ZachMorris_Full' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'Point_and_Click_Bestof_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'PS1_Bestof_ZachMorris' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris_Full' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'Sega_CD_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Sega_Saturn_ZachMorris' : ['RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)'],
							'Sega_SG1000_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Sega_SG1000_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'SNES_Bestof_ZachMorris' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'SNES_ZachMorris' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'SNES_ZachMorris_Full' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'TG16_Bestof_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris_Full' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'ZX_Spectrum_ZachMorris' : ['RetroArch FUSE (Spectrum)','RetroArch FUSE (Spectrum)','RetroArch FUSE (Spectrum)'],
							'x68000_ZachMorris' : ['RetroArch MAME X68k Softlist (x68000)','RetroArch MAME X68k Softlist (x68000)','RetroArch MAME X68k Softlist (x68000)'],
							'x68000_ZachMorris_Full' : ['RetroArch MAME X68k Softlist (x68000)','RetroArch MAME X68k Softlist (x68000)','RetroArch MAME X68k Softlist (x68000)'],
							},
			'OpenElec x86 (tssemek Addon)' : { '32X_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Amiga_CD32_Full' : ['FS-UAE OpenElec Addon (Amiga)','FS-UAE OpenElec Addon (Amiga)','FS-UAE OpenElec Addon (Amiga)'],
							'Amiga_Full_ZRL' : ['FS-UAE OpenElec Addon (Amiga)','FS-UAE OpenElec Addon (Amiga)','FS-UAE OpenElec Addon (Amiga)'],
							'Amiga_Bestof' : ['FS-UAE OpenElec Addon (Amiga)','FS-UAE OpenElec Addon (Amiga)','FS-UAE OpenElec Addon (Amiga)'],
							'Atari_2600_Bestof_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris_Full' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_7800_ZachMorris' : ['RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)'],
							'Atari_Jaguar_ZachMorris' : ['RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)'],
							'Atari_Lynx_ZachMorris' : ['RetroArch Handy (Lynx)','RetroArch Handy (Lynx)','RetroArch Mednafen Lynx (Lynx)'],
							'Game_Gear_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'GB_Classic_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GB_Classic_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBA_Bestof_ZachMorris' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBA_ZachMorris_Full' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBA_ZachMorris' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBC_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBC_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'Genesis_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'IA_MSDOS_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'MAME_Bestof_ZachMorris' : ['RetroArch MAME (Arcade)','RetroArch MAME (Arcade)','RetroArch MAME (Arcade)'],
							'MAME_ZachMorris' : ['RetroArch MAME (Arcade)','RetroArch MAME (Arcade)','RetroArch MAME (Arcade)'],
							'Master_System_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'MSX_ZachMorris' : ['RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)'],
							'N64_Bestof_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris_Full' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'Neo_Geo_CD_ZachMorris' : ['RetroArch MAME (Arcade)','RetroArch MAME (Arcade)','RetroArch MAME (Arcade)'],
							'NES_Bestof_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris_Full' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NGPC_ZachMorris' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'NGPC_ZachMorris_Full' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'Point_and_Click_Bestof_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'PS1_Bestof_ZachMorris' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris_Full' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'Sega_CD_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Sega_Saturn_ZachMorris' : ['RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)'],
							'SNES_Bestof_ZachMorris' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'SNES_ZachMorris' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'SNES_ZachMorris_Full' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'TG16_Bestof_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris_Full' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							},
			'OpenElec RPi (Gamestarter Addon)' : { '32X_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Amiga_CD32_Full' : ['Amiga UAE4ARM','Amiga UAE4ARM','Amiga UAE4ARM'],
							'Amiga_Full_ZRL' : ['Amiga UAE4ARM','Amiga UAE4ARM','Amiga UAE4ARM'],
							'Amiga_Bestof' : ['Amiga UAE4ARM','Amiga UAE4ARM','Amiga UAE4ARM'],
							'Atari_2600_Bestof_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris_Full' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_7800_ZachMorris' : ['RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)'],
							'Atari_Jaguar_ZachMorris' : ['RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)'],
							'Atari_Lynx_ZachMorris' : ['RetroArch Handy (Lynx)','RetroArch Handy (Lynx)','RetroArch Mednafen Lynx (Lynx)'],
							'Game_Gear_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'GB_Classic_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GB_Classic_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBA_Bestof_ZachMorris' : ['RetroArch gpSP (GBA)','RetroArch gpSP (GBA)','RetroArch gpSP (GBA)'],
							'GBA_ZachMorris_Full' : ['RetroArch gpSP (GBA)','RetroArch gpSP (GBA)','RetroArch gpSP (GBA)'],
							'GBA_ZachMorris' : ['RetroArch gpSP (GBA)','RetroArch gpSP (GBA)','RetroArch gpSP (GBA)'],
							'GBC_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBC_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'Genesis_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'IA_MSDOS_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'MAME_Bestof_ZachMorris' : ['RetroArch iMAME4All (Arcade)','RetroArch iMAME4All (Arcade)','RetroArch iMAME4All (Arcade)'],
							'MAME_ZachMorris' : ['RetroArch iMAME4All (Arcade)','RetroArch iMAME4All (Arcade)','RetroArch iMAME4All (Arcade)'],
							'Master_System_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'MSX_ZachMorris' : ['RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)'],
							'N64_Bestof_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris_Full' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'Neo_Geo_CD_ZachMorris' : ['RetroArch iMAME4All (Arcade)','RetroArch iMAME4All (Arcade)','RetroArch iMAME4All (Arcade)'],
							'NES_Bestof_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris_Full' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NGPC_ZachMorris' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'NGPC_ZachMorris_Full' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'Point_and_Click_Bestof_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'PS1_Bestof_ZachMorris' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris_Full' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'Sega_CD_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Sega_Saturn_ZachMorris' : ['RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)'],
							'SNES_Bestof_ZachMorris' : ['RetroArch SNES9xNext (SNES)','RetroArch SNES9xNext (SNES)','RetroArch SNES9xNext (SNES)'],
							'SNES_ZachMorris' : ['RetroArch SNES9xNext (SNES)','RetroArch SNES9xNext (SNES)','RetroArch SNES9xNext (SNES)'],
							'SNES_ZachMorris_Full' : ['RetroArch SNES9xNext (SNES)','RetroArch SNES9xNext (SNES)','RetroArch SNES9xNext (SNES)'],
							'TG16_Bestof_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris_Full' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							},
			'OpenElec RPi (Mezo/lollo78 Addon)' : { '32X_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Amiga_CD32_Full' : ['RetroArch PUAE (Amiga)','RetroArch PUAE (Amiga)','RetroArch PUAE (Amiga)'],
							'Amiga_Full_ZRL' : ['RetroArch PUAE (Amiga)','RetroArch PUAE (Amiga)','RetroArch PUAE (Amiga)'],
							'Amiga_Bestof' : ['RetroArch PUAE (Amiga)','RetroArch PUAE (Amiga)','RetroArch PUAE (Amiga)'],
							'Atari_2600_Bestof_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris_Full' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_7800_ZachMorris' : ['RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)'],
							'Atari_Jaguar_ZachMorris' : ['RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)'],
							'Atari_Lynx_ZachMorris' : ['RetroArch Handy (Lynx)','RetroArch Handy (Lynx)','RetroArch Mednafen Lynx (Lynx)'],
							'Game_Gear_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'GB_Classic_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GB_Classic_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBA_Bestof_ZachMorris' : ['RetroArch gpSP (GBA)','RetroArch gpSP (GBA)','RetroArch gpSP (GBA)'],
							'GBA_ZachMorris_Full' : ['RetroArch gpSP (GBA)','RetroArch gpSP (GBA)','RetroArch gpSP (GBA)'],
							'GBA_ZachMorris' : ['RetroArch gpSP (GBA)','RetroArch gpSP (GBA)','RetroArch gpSP (GBA)'],
							'GBC_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBC_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'Genesis_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'IA_MSDOS_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'MAME_Bestof_ZachMorris' : ['RetroArch iMAME4All (Arcade)','RetroArch iMAME4All (Arcade)','RetroArch iMAME4All (Arcade)'],
							'MAME_ZachMorris' : ['RetroArch iMAME4All (Arcade)','RetroArch iMAME4All (Arcade)','RetroArch iMAME4All (Arcade)'],
							'Master_System_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'MSX_ZachMorris' : ['RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)'],
							'N64_Bestof_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris_Full' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'Neo_Geo_CD_ZachMorris' : ['RetroArch iMAME4All (Arcade)','RetroArch iMAME4All (Arcade)','RetroArch iMAME4All (Arcade)'],
							'NES_Bestof_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris_Full' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NGPC_ZachMorris' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'NGPC_ZachMorris_Full' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'Point_and_Click_Bestof_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'PS1_Bestof_ZachMorris' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris_Full' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'Sega_CD_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Sega_Saturn_ZachMorris' : ['RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)'],
							'SNES_Bestof_ZachMorris' : ['RetroArch SNES9xNext (SNES)','RetroArch SNES9xNext (SNES)','RetroArch SNES9xNext (SNES)'],
							'SNES_ZachMorris' : ['RetroArch SNES9xNext (SNES)','RetroArch SNES9xNext (SNES)','RetroArch SNES9xNext (SNES)'],
							'SNES_ZachMorris_Full' : ['RetroArch SNES9xNext (SNES)','RetroArch SNES9xNext (SNES)','RetroArch SNES9xNext (SNES)'],
							'TG16_Bestof_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris_Full' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							},
			'Android' : { '32X_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Amiga_CD32_Full' : ['RetroArch PUAE (Amiga)','RetroArch PUAE (Amiga)','RetroArch PUAE (Amiga)'],
							'Amiga_Full_ZRL' : ['RetroArch PUAE (Amiga)','RetroArch PUAE (Amiga)','RetroArch PUAE (Amiga)'],
							'Amiga_Bestof' : ['RetroArch PUAE (Amiga)','RetroArch PUAE (Amiga)','RetroArch PUAE (Amiga)'],
							'Atari_2600_Bestof_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris_Full' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_2600_ZachMorris' : ['RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)','RetroArch Stella (Atari 2600)'],
							'Atari_7800_ZachMorris' : ['RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)','RetroArch ProSystem (Atari 7800)'],
							'Atari_Jaguar_ZachMorris' : ['RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)','RetroArch Virtual Jaguar (Jaguar)'],
							'Atari_Lynx_ZachMorris' : ['RetroArch Handy (Lynx)','RetroArch Handy (Lynx)','RetroArch Mednafen Lynx (Lynx)'],
							'Game_Gear_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Game_Gear_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'GB_Classic_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GB_Classic_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBA_Bestof_ZachMorris' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBA_ZachMorris_Full' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBA_ZachMorris' : ['RetroArch mGBA (GBA)','RetroArch mGBA (GBA)','RetroArch mGBA (GBA)'],
							'GBC_ZachMorris_Full' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'GBC_ZachMorris' : ['RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)','RetroArch Gambatte (GB/GBC)'],
							'Genesis_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Genesis_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'IA_MSDOS_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'MAME_Bestof_ZachMorris' : ['RetroArch MAME (Arcade)','RetroArch MAME (Arcade)','RetroArch MAME (Arcade)'],
							'MAME_ZachMorris' : ['RetroArch MAME (Arcade)','RetroArch MAME (Arcade)','RetroArch MAME (Arcade)'],
							'Master_System_Bestof_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'Master_System_ZachMorris_Full' : ['RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)','RetroArch Genesis Plus GX (GG/SMS/Gen/PICO/SG-1000)'],
							'MSX_ZachMorris' : ['RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)','RetroArch BlueMSX (MSX)'],
							'N64_Bestof_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'N64_ZachMorris_Full' : ['RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)','RetroArch Mupen64Plus (N64)'],
							'Neo_Geo_CD_ZachMorris' : ['RetroArch MAME (Arcade)','RetroArch MAME (Arcade)','RetroArch MAME (Arcade)'],
							'NES_Bestof_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NES_ZachMorris_Full' : ['RetroArch Nestopia (NES)','RetroArch Nestopia (NES)','RetroArch Nestopia (NES)'],
							'NGPC_ZachMorris' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'NGPC_ZachMorris_Full' : ['RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)','RetroArch Mednafen NeoPop (NGP/NGPC)'],
							'Point_and_Click_Bestof_ZachMorris' : ['RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)','RetroArch DOSBox (DOS)'],
							'PS1_Bestof_ZachMorris' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris_Full' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'PS1_ZachMorris' : ['RetroArch PCSX ReArmed (PS1)','RetroArch PCSX ReArmed (PS1)','RetroArch Mednafen PSX (PS1)'],
							'Sega_CD_ZachMorris' : ['RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)','RetroArch PicoDrive (SMS/Gen/Sega CD/32X)'],
							'Sega_Saturn_ZachMorris' : ['RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)','RetroArch Yabuse (Saturn)'],
							'SNES_Bestof_ZachMorris' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'SNES_ZachMorris' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'SNES_ZachMorris_Full' : ['RetroArch SNES9x (SNES)','RetroArch BSNES Mercury Balanced (SNES)','RetroArch BSNES Mercury Accuracy (SNES)'],
							'TG16_Bestof_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris_Full' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							'TG16_ZachMorris' : ['RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)','RetroArch Mednafen PCE FAST (PCE/TG16)'],
							},
            }

parserfile = os.path.join(addon.getAddonInfo('path'),'resources','data','external_launcher_parser.xml')
launchersfile = os.path.join(addon.getAddonInfo('path'),'resources','data','external_command_database.xml')
descParser = DescriptionParserFactory.getParser(parserfile)
results = descParser.parseDescription(launchersfile,'xml')
# print results[0]

current_dialog = xbmcgui.Dialog()
not_ready = False

if 'Select' in wizard_data['settings']['iarl_wizard_launcher_group']:
	ok_ret = current_dialog.ok('Setup not ready','Please select a setup type[CR]Then hit OK to save your settings and try again.')
	not_ready = True

# Select|OSX|Windows|Linux/Kodibuntu|OpenElec x86 (tssemek Addon)|OpenElec RPi (Gamestarter Addon)|Android
if not not_ready:
	if 'Select' in wizard_data['settings']['iarl_external_user_external_env']:
		ok_ret = current_dialog.ok('Setup not ready','Please select your system type[CR]Then hit OK to save your settings and try again.')
		not_ready = True

if not not_ready:
	if 'OSX' in wizard_data['settings']['iarl_external_user_external_env'] or 'Windows' in wizard_data['settings']['iarl_external_user_external_env'] or 'Linux/Kodibuntu' in wizard_data['settings']['iarl_external_user_external_env'] :
		if len(wizard_data['settings']['iarl_path_to_retroarch'])<1:
			ok_ret = current_dialog.ok('External Program Warning','Path to retroarch must be set first.[CR]Then hit OK to save your settings and try again.')
			not_ready = True
		if 'Disabled' in wizard_data['settings']['iarl_additional_emulator_1_type'] and 'Disabled' in wizard_data['settings']['iarl_additional_emulator_2_type']:
			ret2 = current_dialog.select('Additional emulators for some archives are not setup, continue?', ['Yes','Cancel'])
			if ret2>0:
				not_ready = True

if not not_ready:
	try:
		group_index = 'Select|Most Playable (Least CPU Intensive)|Balanced|Most Accurate'.split('|').index(wizard_data['settings']['iarl_wizard_launcher_group'])
	except:
		group_index = None
		not_ready = True
		xbmc.log(msg='IARL:  Wizard group could not be defined', level=xbmc.LOGDEBUG)

#Main script start
if not not_ready:
	user_options = list()
	launch_command = list()
	new_launch_command = None
	xbmc.log(msg='IARL:  Wizard Script Started', level=xbmc.LOGNOTICE)
	if 'enabled' in wizard_data['settings']['iarl_external_launch_close_kodi'].lower():
		external_launch_database_os = wizard_data['settings']['iarl_external_user_external_env'] + ' Close_Kodi' #Look for launch commands to close Kodi
	else:
		external_launch_database_os = wizard_data['settings']['iarl_external_user_external_env']
	if wizard_data['settings']['iarl_external_user_external_env'] in 'OpenElec x86 (tssemek Addon)|OpenElec RPi (Gamestarter Addon)|OpenElec RPi (Mezo/lollo78 Addon)|Android'.split('|'):
		external_launch_database_os = external_launch_database_os.replace(' Close_Kodi','') #By default, the above setups auto close Kodi, so there's only one list of launchers to choose from
	
	for entries in results:
		#Define the list of commands from the external database corresponding to the current environment
		if entries['operating_system'][0] == external_launch_database_os:
			user_options.append(entries['launcher'][0])
			launch_command.append(entries['launcher_command'][0])

	initialize_userdata()
	userdata_xmldir = get_userdata_xmldir()
	userdata_subfolders, userdata_files = xbmcvfs.listdir(userdata_xmldir)

	dp = xbmcgui.DialogProgress()
	dp.create('IARL Wizard','Updating Settings','')
	dp.update(0)
	for ffiles in userdata_files:
		try:
			current_name = os.path.splitext(os.path.split(ffiles)[-1])[0]
		except:
			current_name = None
			xbmc.log(msg='IARL:  '+str(current_name)+' could not be found', level=xbmc.LOGDEBUG)
		try:
			current_key = wizard_data[wizard_data['settings']['iarl_external_user_external_env']][current_name][group_index-1]
		except:
			current_key = None
			xbmc.log(msg='IARL:  Wizard setting for '+str(current_name)+' could not be found', level=xbmc.LOGDEBUG)

		if current_key is not None:
			# print current_name
			# print current_key
			# print launch_command[user_options.index(current_key)]
			percent_complete = int((int(userdata_files.index(ffiles))*100)/int(len(userdata_files)))
			dp.update(percent_complete)
			xbmc.sleep(100)
			if dp.iscanceled():
				dp.close()
				raise
			try:
				update_xml_header(userdata_xmldir,ffiles,'emu_launcher','external')
			except:
				xbmc.log(msg='IARL:  emu_launcher command for '+str(ffiles)+' could not be set in Wizard', level=xbmc.LOGDEBUG)
			try:
				update_xml_header(userdata_xmldir,ffiles,'emu_ext_launch_cmd',launch_command[user_options.index(current_key)])
				xbmc.log(msg='IARL:  '+str(ffiles)+' new command: '+str(launch_command[user_options.index(current_key)]), level=xbmc.LOGDEBUG)
			except:
				xbmc.log(msg='IARL:  emu_ext_launch_cmd for '+str(ffiles)+' could not be set in Wizard', level=xbmc.LOGDEBUG)
	
	clear_userdata_list_cache_dir()
	dp.close()
	ok_ret = current_dialog.ok('Complete','Wizard run completed!')
	xbmc.log(msg='IARL:  Wizard Script Completed', level=xbmc.LOGNOTICE)
else:
	xbmc.log(msg='IARL:  Wizard Script Cancelled', level=xbmc.LOGNOTICE)