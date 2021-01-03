# 
# Script walks through the mamenames.xml in emulation station and
# attempts to move any slot machines and blacklisted terms or
# countries to ~/roms_excluded
#
# A more correct solution would be to parse the genre and manufacturer
# in /mame/hash/*.xml and use that but this was easier
#
# Not yet decided what to do with ROMS that are in the 0.174/2016 set
# but not in emulation stations mamenames.xml (i.e. wpt_*, csi_*,
# bbh_*, sman_*, pepk0*, pepp0*, peps0*, pex0*, pex2*,). Are these 
# real machines or shared resouces? For now have manually moved them

import shutil
import os.path

manufacturers = ["(Maygay", "(Barcrest", "(Ace", "(Pcp", "(Bellfruit",
                 "(Mazooma", "(Astra", "(BGT", "(Atronic",
                 "(Electrocoin", "(EPOCH", "(Qps", "(Fairgames",
		 "(JPM", "(Avantime", "(Empire", "(Crystal", "(Union",
		 "Bwb", "(Brunel Research", "(Vivid", "(Gemini",
		 "(Mdm", "(BFM", "(Concept", "(Project", "(Coinworld"]
black_list = ["bootleg", "hack", "coin dropper", "LaserDisc",
              "Fruit Bonus", "Fruit Cocktail", "(Trackball",
	      "Gaminator", "(MPU4", "(MPU5", "Dance Dance Revolution",
	       "Player's Edge", "Fruit Carnival", "Luvvly Jubbly",
	       "Cal Omega", "Playboy", "Pit Boss", "Funcube", "Columbus",
	       "Touchmaster", "Royal", "Witch Jack", "Casino", "Cash",
	       "Poker", "Quiz", "Jackpot", "Addams"]
countries = ["(Spanish", "(Russian", "(Russia", "(Japan", "(German",
             "(France", "(Korea"]
exclusions = manufacturers + black_list + countries
mamenames = "/opt/retropie/supplementary/emulationstation/resources/mamenames.xml"
rom_source = "/home/pi/RetroPie/roms/arcade/roms/"
rom_bad = "/home/pi/roms_excluded/"

prt_ctl = True
name_buffer = ""
zip_name = ""
fh_white = open("white_list.xml", "w")
fh_black = open("black_list.xml", "w")
white_count = 0
black_count = 0
with open(mamenames, "r") as mamelist:
	for line in mamelist:
		name_buffer += line
		if "<realname>" in line:
			if any(name in line for name in exclusions):
				prt_ctl = False
		if "<mamename>" in line:
			zip_name = line[11:-12]
		if "</game>" in line:
			if prt_ctl is True:
				fh_white.write(name_buffer)
				white_count += 1
			else:
				fh_black.write(name_buffer)
				black_count += 1
				if os.path.isfile(rom_source+zip_name+".zip"):
					shutil.move(rom_source+zip_name+".zip", rom_bad+zip_name+".zip")
			prt_ctl = True
			name_buffer = ""
			zip_name = ""
fh_white.close()
fh_black.close()
print("Kept:", white_count)
print("Removed:", black_count)
