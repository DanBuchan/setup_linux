# 
# Script walks through the romset metadata xml and
# attempts to move any slot machines and blacklisted terms or
# countries to ~/roms_excluded
#
# Not yet decided what to do with ROMS that are in the 0.174/2016 set
# but not in emulation station's mamenames.xml (i.e. wpt_*, csi_*,
# bbh_*, sman_*, pepk0*, pepp0*, peps0*, pex0*, pex2*,). Are these 
# real machines or shared resouces? For now have manually moved them

import os
import xml.etree.ElementTree as ET

manufacturers = ["Maygay", "Barcrest", "Ace", "Pcp", "Bellfruit",
                 "Mazooma", "Astra", "BGT", "Atronic",
                 "Electrocoin", "EPOCH", "Qps", "Fairgames",
		 "JPM", "Avantime", "mpire", "Crystal", "Union",
		 "Bwb", "Brunel Research", "Vivid", "Gemini",
		 "Mdm", "BFM", "Concept", "Project", "Coinworld"]
black_list = ["bootleg", "hack", "coin dropper", "LaserDisc",
              "Fruit Bonus", "Fruit Cocktail", "Trackball",
	      "Gaminator", "MPU4", "MPU5", "Dance Dance Revolution",
	       "Player's Edge", "Fruit Carnival", "Luvvly Jubbly",
	       "Cal Omega", "Playboy", "Pit Boss", "Funcube", "Columbus",
	       "Touchmaster", "Royal", "Witch Jack", "Casino", "Cash",
	       "Poker", "Quiz", "Jackpot", "Addams"]
countries = ["Spanish", "Russian", "Russia", "Japan", "German",
             "France", "Korea"]
exclusions = manufacturers + black_list + countries
mamenames = "/opt/retropie/supplementary/emulationstation/resources/mamenames.xml"
rom_meta_data = "/media/pi/baf59409-c0e7-42a5-bcca-e155a9cf5fc8/ROMS/MAME_2016_Arcade_Romsets/MAME 2016 XML (Arcade Only).xml"
rom_source = "/media/pi/baf59409-c0e7-42a5-bcca-e155a9cf5fc8/ROMS/MAME_2016_Arcade_Romsets/roms/"

tree = ET.parse(rom_meta_data)
root = tree.getroot()
fh_white = open("white_list.csv", "w")
fh_black = open("black_list.csv", "w")
missing = open("missing.csv", "w")
white_count = 0
black_count = 0
for machine in root.iter("machine"):
    keep = True
    name = machine.attrib["name"] + ".zip"
    for desc in machine.iter("description"):
        description = desc.text
    for manufacturer in machine.iter("manufacturer"):
        manu_name = manufacturer.text        
    
    if manu_name in manufacturers or any(word in description for word in countries) or any(word in description for word in black_list):
        keep = False

    if keep == False:
        print(name, description, manu_name, sep=",", file=fh_black)
        black_count += 1
        try:
            os.remove(rom_source+name)
        except:
            print("MISSING:", name)
            print(name, description, manu_name, sep=",", file=missing)
    else:
        print(name, description, manu_name, sep=",", file=fh_white)
        white_count += 1

print("Kept:", white_count)
print("Removed:", black_count)
