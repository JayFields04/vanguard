import random

# AR
STG = {
    "Muzzle":["None","Scyth Compensator","MX Silencer","T1 Flash Hider"," Recoil Booster","Mercury Silencer","Chord Muzzle Break","F8 Stabilizer"],
    "Barrel":["None","VDD 320MM 02B", "VDD 760 05B", "Krausnick 620MM Precision","Krausnick 220MM Rapid"],
    "Optic":random.randrange(0,23),
    "Stock":["None","Krausnick S11S Folding","Konstanz Tactical","Removed Stock","VDD 27 Percision","VDD 34S Weighted"],
    "Underbarrel":["None","Carver Foregrip","M1941 Hand Stop","M3 Ready Grip","Bipod","Flashlight","SMLE Pistol Grip","M1930 Strife Angled","Bayonet","Mark IV Skelatal"],
    "Magazine":["None","Gorenck 30 Round", "Russion Short 20 Round","Kurz 45 Round","Russion Short 30 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Pressure","Acrobatic","Sleight of Hand","Nerves of Steel","Focus","Vital"],
    "Kit":["None","Fast Melee", "Reach","Surplus","Deep Breath","Fully Loaded","Defender","Heavy Hitter","On-Hand"]
    }
Automaton = {
    "Muzzle":["None","G28 Compensator","MX silencer","M9 Flash Hider","Recoil Booster","Mercury Silencer","Chord Muzzle Brake","F8 Stabilizer"],
    "Barrel":["None","ZAC 600MM BFA","ZAC FA Short","ZAC 320MM Burst", "Empress 620MM Precision","Ananstasia Sniper"],
    "Optic":random.randrange(0,21),
    "Stock":["None","Empress Broadsword","Anastasia Padded","ZAC Skeletal"],
    "Underbarrel":["None","Carver Foregrip","M1941 Hand Stop","M3 Ready Grip","Bipod","Flashlight","Bayonet","Mark VI Skelatal","M1915 Steady"],
    "Magazine":["None","Sakura 45 Round","5.6MM 25 Round","Sakura 75 Round","Klauser 50 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Spotter","Pressure","Steady","Sleight of Hand","Dismantle","tight Grip","Frenzy"],
    "Kit":["None","Fast Melee", "Reach","Surplus","Deep Breath","Fully Loaded","Defender","Heavy Hitter","On-Hand"]
    }
IrtaBurst = {
    "Muzzle":["None","G28 Compensator","MX silencer","M9 Flash Hider","Recoil Booster","Mercury Silencer","Chord Muzzle Brake","F8 Stabilizer"],
    "Barrel":["None","Botti 300MM","IMERITO 180MM","PERFETTO 140MM","Botti 270MM"],
    "Optic":random.randrange(0,23),
    "Stock":["None","SSI Skeletal","Imerito Custom","SMI Adjustable","Padded Grip","DII Grip"],
    "Underbarrel":["None","Carver Foregrip","M1941 Hand Stop","M3 Ready Grip","Bipod","Flashlight","Bayonet","Mark VI Skelatal","SMLE Pistol Grip"],
    "Magazine":["None","Klauser 12 Round","Sakura 20 Round","Klauser 32 Round","British 32 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Quickscope","Surveil","Focus","Sleight of Hand","Hardscope","Vital"],
    "Kit":["None","Fast Melee", "Reach","Surplus","Deep Breath","Fully Loaded","Defender","Heavy Hitter","On-Hand"]
    }
Bar = {    
    "Muzzle":["None","G28 Compensator","MX silencer","Iscove Flash Hider","Recoil Booster","Mercury Silencer","Chord Muzzle Brake","F8 Stabilizer"],
    "Barrel":["None","30 XL","27 2B","21 Scythe","18 Rapid"],
    "Optic":random.randrange(0,23),
    "Stock":["None","CGC Wire","Chariot WR","Removed Stock","Pistol Grip Custom","Cooper SP"],
    "Underbarrel":["None","Carver Foregrip","M1941 Hand Stop","M3 Ready Grip","Bipod","Flashlight","Bayonet","Mark VI Skelatal","SMLE Pistol Grip"],
    "Magazine":["None","12 Round Fast Mag","Klauser 20 Round","BMG 20 Round","BMG 30 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Sleight of Hand","Discard","Driller","Acrobat","Hardscope","Focus"],
    "Kit":["None","Fast Melee", "Reach","Surplus","Deep Breath","Fully Loaded","Defender","Heavy Hitter","On-Hand"]
    }
AS44= {    
    "Muzzle":["None","G28 Compensator","MX silencer","M9 Flash Hider","Recoil Booster","Mercury Silencer","Chord Muzzle Brake","F8 Stabilizer"],
    "Barrel":["None","Kovalevskaya 615MM","Empress 400MM","Kovalevskaya 420MM Burst","Empress Falchion A"],
    "Optic":random.randrange(0,21),
    "Stock":["None","ZAC Skeletal","Removed Stock","Kovalevskaya Custom","ZAC 12A","ZAC 12B Custom"],
    "Underbarrel":["None","Carver Foregrip","M1941 Hand Stop","M3 Ready Grip","Bipod","Flashlight","Bayonet","Mark VI Skelatal","SMLE Pistol Grip"],
    "Magazine":["None","MMR 30 Round","Russion Short 60 Round","Gorenko 45 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Disable","Gung-Ho","Steady","Sleight of Hand","Acquisition","Mementum"],
    "Kit":["None","Fast Melee", "Reach","Surplus","Deep Breath","Fully Loaded","Defender","Heavy Hitter","On-Hand"]
    }
NZ41= {
    "Muzzle":["None","G28 Compensator","MX silencer","ISCIVE Flash Hider","Recoil Booster","Mercury Silencer","Chord Muzzle Brake","F8 Stabilizer"],
    "Barrel":["None","Ravenwood 480MM","Orbweaver Custom","Orbweaver 360MM","MK1 Burst"],
    "Optic":random.randrange(0,22),
    "Stock":["None","Ravenwood Padded","MK3 SC","Orbweaver Folding","Orbweaver E Pack","LOR Reinforced","Orbweaver Elite"],
    "Underbarrel":["None","Carver Foregrip","M1941 Hand Stop","M3 Ready Grip","Bipod","Flashlight","Bayonet","Mark VI Skelatal","SMLE Pistol Grip"],
    "Magazine":["None","British 20 Round", "Klauser 30 Round","Sakura 45 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Discard","Brace","Frenzy","Acrobat","Pinned","Unmarked"],
    "Kit":["None","Fast Melee", "Reach","Surplus","Deep Breath","Fully Loaded","Defender","Heavy Hitter","On-Hand"]
    }
Volk = {
    "Muzzle":["None","G28 Compensator","MX silencer","M9 Flash Hider","Recoil Booster","Mercury Silencer","Chord Muzzle Brake","F8 Stabilizer"],
    "Barrel":["None","Krausnick 428MM","VDD 287MM","Residorf 407MM"],
    "Optic":random.randrange(0,23),
    "Stock":["None","SA Converted","Krausnick S10V","Krausnick S12V","Residorf 22V"],
    "Underbarrel":["None","Carver Foregrip","M1941 Hand Stop","M3 Ready Grip","Bipod","Flashlight","Bayonet","Mark VI Skelatal","SMLE Pistol Grip"],
    "Magazine":["None","Kurz 20 Round","Gorenko 30 Round","Kurz 60 Round","Gorenko 20 Round","Russian Short 45 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Steady","Pressure","Gung-Ho","Perfectionist","Sleight of Hand","Fleet"],
    "Kit":["None","Fast Melee", "Reach","Surplus","Deep Breath","Fully Loaded","Defender","Heavy Hitter","On-Hand"]
    }
CooperCarbine = {
    "Muzzle":["None","G28 Compensator","MX silencer","T1 Flash Hider","Recoil Booster","Mercury Silencer","Chord Muzzle Brake","F8 Stabilizer"],
    "Barrel":["None","22 cooper Custom","8 Ragdoll Short","18 Ragdoll G45","14 Gracey rapid"],
    "Optic":random.randrange(0,21),
    "Stock":["None","Cooper 45RS","ragdoll G45 Skeletal","Cooper Custom Padded","Cooper 45W","Removed Stock"],
    "Underbarrel":["None","Carver Foregrip","M1941 Hand Stop","M3 Ready Grip","Bipod","GF-59 Flashlight","Bayonet","Mark VI Skelatal","SMLE Pistol Grip"],
    "Magazine":["None",".30 Carbine 45 Round",".45 25 Round","9MM 60 Round",".30 Carbine 20 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point","Compressed rounds"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Tight Grip","Discrd","Hardscope","Brace","Fleet","Vital","Icy Veins"],
    "Kit":["None","Fast Melee", "Reach","Surplus","Deep Breath","Fully Loaded","Defender","Heavy Hitter","On-Hand"]
    }

#SMGS
MP40 = {
    "Muzzle":["None","F8 Stabilizer","Marauder Flash Hider","Mercury Silencer","No.3 Rifle Break","Strife Compensator","M1929 Silencer","Recoil Booster"],
    "Barrel":["None","Krausnic 317MM","VDD 285MM","Krausnick 221MM","VDD 189MM"],
    "Optic":random.randrange(0,20),
    "Stock":["None","Krausnick 33M","Removed Stock","VDD 34M Padded","VDD 34M","VDD 35M Wire Grip"],
    "Underbarrel":["None","M1930 Strife Angled","Craver Foregrip","SG98 Compact","M1915 Steady","Mark IV","M1941 Hand Stop","GF-59 Flashlight","SMLE Pistol Grip"],
    "Magazine":["None","9MM 24 Round","7.62 Gorenko  32 Round","9MM 64 Round","8MM Kurz 32 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Steady","Perfectionist","Nerves of Steel","Momentum","Brace","Unmarked"],
    "Kit":["None","Fast Melee","Reach","Surplus","Quick","Fully Loaded","Defender","Heavy Hitter","On-Hand"]
    }
STEN = {
    "Muzzle":["None","F8 Stabilizer","Marauder Flash Hider","Mercury Silencer","No.3 Rifle Break","Strife Compensator","M1929 Silencer","Recoil Booster"],
    "Barrel":["None","Hockenson 174MM","Gawain 140MM","Hockenson 248MM","Hockenson 348MM","SA 65MM"],
    "Optic":random.randrange(0,20),
    "Stock":["None","Gawain Para","SA 41S","Hockenson S33S Padded","Gawain Custom","Hockenson S32S Foregrip","Gawain Folding 43S"],
    "Underbarrel":["None","M1930 Strife Angled","Craver Foregrip","SG98 Compact","M1915 Steady","Mark IV","M1941 Hand Stop","GF-59 Flashlight","SMLE Pistol Grip"],
    "Magazine":["None","9MM 20 Round","7.62 Gorenko 32 Round","9MM 50 Round",".45 ACP 20 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Steady","Acrobatic","Gung-Ho","Sleight of Hand","Frenzy","Momentum"],
    "Kit":["None","Fast Melee","Reach","Surplus","Quick","Fully Loaded","Defender","Heavy Hitter","On-Hand"]}
M1928 = {
    "Muzzle":["None","F8 Stabilizer","Marauder Flash Hider","Mercury Silencer","No.3 Rifle Break","G28 Compensator","M1929 Silencer","Recoil Booster"],
    "Barrel":["None","CGC 14.5","CGC 12","Chariot 2.5","Chariot 5.5"],
    "Optic":random.randrange(0,20),
    "Stock":["None","CGC S Adjustable","CGC Wire Grip","Ragdoll T2","Chariot SI","Chariot Marksman"],
    "Underbarrel":["None","M1930 Strife Angled","Craver Foregrip","SG98 Compact","M1915 Steady","Mark IV","M1941 Hand Stop","GF-59 Flashlight","SMLE Pistol Grip"],
    "Magazine":["None",".45 ACP 30 Round","9MM 50 Round",".45 ACP 100 Round","8MM Kurz 50 Round","8MM Kurz 100 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Steady","Disable","Pressure","Sleight of Hand","Fleet","Frenzy"],
    "Kit":["None","Fast Melee","Reach","Surplus","Quick","Fully Loaded","Defender","Heavy Hitter","On-Hand"]}
OwenGun = {
    "Muzzle":["None","F8 Stabilizer","Marauder Flash Hider","Mercury Silencer","No.3 Rifle Break","M1929 Silencer","Recoil Booster"],
    "Barrel":["None","Gawain 188MM","Hockenson 142MM","Hockenson 305MM"],
    "Optic":random.randrange(0,17),
    "Stock":["None","Ravenwood MK","Gawain H4","Removed Stock","Orbweaver Padded","LOR Folding"],
    "Underbarrel":["None","M1930 Strife Angled","Craver Foregrip","SG98 Compact","M1915 Steady","Mark IV","M1941 Hand Stop","GF-59 Flashlight","SMLE Pistol Grip"],
    "Magazine":["7.62 Gorenko 33 Round","7.62 Gorenko 72 Round","9MM 20 Round","8MM Kurz 60 Round","9MM 72 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Steady","Acrobatic","Wreck","Brace","Sleight of hand","Fleet"],
    "Kit":["None","Fast Melee","Reach","Surplus","Quick","Fully Loaded","Defender","Heavy Hitter","On-Hand"]}
Type100 = {
    "Muzzle":["None","F8 Stabilizer","Marauder Flash Hider","Mercury Silencer","No.3 Rifle Break","M1929 Silencer","Recoil Booster"],
    "Barrel":["None","Sakura 282MM","Sakura 196MM","Shiraishi 374MM","Shiraishi Percision","Warubachi 134MM"],
    "Optic":random.randrange(0,19),
    "Stock":["None","Warubachi Skeletal","Warubachi Grip","Shiraishi Weighted","Shiraishi T100","Sakura Type 2"],
    "Underbarrel":["None","M1930 Strife Angled","Craver Foregrip","SG98 Compact","M1915 Steady","Mark IV","M1941 Hand Stop","GF-59 Flashlight","SMLE Pistol Grip"],
    "Magazine":["None","8MM Nambu 20 Round",".30 Russian Short 30 Round","8MM Kurz 40 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Acrobatic","Gung-Ho","Fleet","Sleight of Hand","Vital","Unmarked"],
    "Kit":["None","Fast Melee","Reach","Surplus","Quick","Fully Loaded","Defender","Heavy Hitter","On-Hand"]}
PPSH = {
    "Muzzle":["None","F8 Stabilizer","Marauder Flash Hider","Mercury Silencer","No.3 Rifle Break","M1929 Silencer","Recoil Booster"],
    "Barrel":["None","Zac 280MM","Kovalevskaya 230MM","Empress 140MM","ZAC 300MM"],
    "Optic":random.randrange(0,20),
    "Stock":["None","Kovalevskaya Skelatal","ZAC Folding","Removed Stock","Empress Custom","Empress S12P"],
    "Underbarrel":["None","M1930 Strife Angled","Craver Foregrip","SG98 Compact","M1915 Steady","Mark IV","M1941 Hand Stop","GF-59 Flashlight","SMLE Pistol Grip"],
    "Magazine":["None","8MM Nambu 71 Round","7.62MM Gorenko 71 Round","7.62MM Gorenko 25 Round",".30 Russian Short 35 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Steady","Discard","Disable","Tight Grip","Nerves of Steel","Fleet"],
    "Kit":["None","Fast Melee","Reach","Surplus","Quick","Fully Loaded","Defender","Heavy Hitter","On-Hand"]}

# Shotty
Horn = {
    "Muzzle":["None","M97 Full Choke","G28 Compensator","A5 Smoothbore","Suhl 16 Brake"],
    "Barrel":["None","Sawed-Off","Klauser 610MM","Klauser 560MM","Klauser 710MM"],
    "Optic":random.randrange(0,18),
    "Stock":["None","Reisdorf Folding","Removed Stock","VDD Hunter","VDD 33B","Klauser S2"],
    "Underbarrel":["None","M1930 Strife Angled","Carver Foregrip","Mark VI","GF-59 Flashlight","SMLE Pistol Grip","M1941 Hand Stop","M1915 Steady"],
    "Magazine":["None","16 Gauge 3 Round","Birdshot 5 Round","16 Gauge 7 Round","12 Gauge 5 Round"],
    "Ammo Type":["None","Reduced Powder","Slug","Incendiary","Packed Powder","Hollow Point","Frangible","Buck and Slug"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Wreck","Nerves of Steel","Acrobatic","Gung-Ho","Disable","Sleight of Hand","Momentum"],
    "Kit":["None","Fast Melee","On-Hand","Quick","Surplus","Fully Loaded","Heavy Hitter","Reach"]}
Combat = {
    "Muzzle":["None","M97 Full Choke","G28 Compensator","A5 Smoothbore","Suhl 16 Brake"],
    "Barrel":["None","Chariot 16","Framable 23","Framable 18","Sawed-Off","Framable No.3"],
    "Optic":random.randrange(0,16),
    "Stock":["None","Wire Custom","CGC 2M Wire","CGC 3M Adjustable","Framable Big-Game"],
    "Underbarrel":["None","M1930 Strife Angled","Carver Foregrip","Mark VI","GF-59 Flashlight","SMLE Pistol Grip","M1941 Hand Stop","M1915 Steady"],
    "Magazine":["None","16 Gauge 3 Round","16 Gauge 7 Round","16 Gauge 10 Round","12 Gauge 5 Round"],
    "Ammo Type":["None","Reduced Powder","Slug","Incendiary","Packed Powder","Hollow Point","Frangible","Buck and Slug"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Wreck","Disable","Steady","Vital","Sleight of Hand","Momentum","Frenzy"],
    "Kit":["None","Fast Melee","On-Hand","Quick","Surplus","Fully Loaded","Heavy Hitter","Reach"]}
GraceyAuto = {
    "Muzzle":["None","M97 Full Choke","G28 Compensator","A5 Smoothbore","Suhl 16 Brake"],
    "Barrel":["None","CGC 28","Chariot 33","Sawed-Off","CGC 22"],
    "Optic":random.randrange(0,16),
    "Stock":["None","Ragdoll P-Wire","Chariot S Huntsman","Chariot Sport","Removed Sport","CGC H4"],
    "Underbarrel":["None","M1930 Strife Angled","Carver Foregrip","Mark VI","GF-59 Flashlight","SMLE Pistol Grip","M1941 Hand Stop","M1915 Steady"],
    "Magazine":["None","12 Gauge 7 Round","Extra Range","Extra Pellets","12 Gauge 10 Round"],
    "Ammo Type":["None","Reduced Powder","Slug","Incendiary","Packed Powder","Hollow Point","Frangible","Buck and Slug"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Discard","Tight","Fleet","Gung-Ho","Spotter","Pinned","Frenzy"],
    "Kit":["None","Fast Melee","On-Hand","Quick","Surplus","Fully Loaded","Heavy Hitter","Reach"]}
DoubleBarrel = {
    "Muzzle":["None","M97 Full Choke","G28 Compensator","A5 Smoothbore","Suhl 16 Brake"],
    "Barrel":["None","Wilkie LJ-24","Wilkie Huntsman","Sawed-Off","LJ-18 Defender"],
    "Optic":random.randrange(0,16),
    "Stock":["None","Skeletal Chopped","Gawain Skeletal","Removed Stock","SA 12R","SA Weighted","Wilkie Marksman"],
    "Underbarrel":["None","M1930 Strife Angled","Carver Foregrip","Mark VI","GF-59 Flashlight","SMLE Pistol Grip","M1941 Hand Stop","M1915 Steady"],
    "Magazine":["None","16 Gauge","Double Aught"],
    "Ammo Type":["None","Reduced Powder","Slug","Incendiary","Packed Powder","Hollow Point","Frangible","Buck and Slug"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Discard","Pressure","Gung-Ho","Panic","Vital","Sleight of Hand","Steady","Akimbo"],
    "Kit":["None","Fast Melee","On-Hand","Quick","Surplus","Fully Loaded","Heavy Hitter","Reach"]}

# LMG
MG42 = {
    "Muzzle":["None","F8 Stabilizer","ISCOVE Flash Hider","L Brake","Mercury Silencer","Recoil Booster","MX Silencer","G28 Compensator"],
    "Barrel":["None","VDD 680MM 31M","Krausnick 450MM","VDD 890MM 32M","Krausnick 355MM"],
    "Optic":random.randrange(0,24),
    "Stock":["None","Removed Stock","VDD Skeletal","Krausnick S91 Padded","VDD 64M","Krausnick S91MG"],
    "Underbarrel":["None","Carver Foregrip",'M1930 Strife Angled',"SMLE Pistol Grip","Heavy Foregrip","GF-59 Flashlight","Bipod","Mark VI Skeletal","M1941 Hand Stop"],
    "Magazine":["None","Sakura 125 Round","8MM Klauser 50 Round","13MM Anti-Material 125 Round","8MM Klauser 250 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Steady","Disable","Wreck","Nerves of Steel","Tight Grip","Frenzy"],
    "Kit":["None","Fast Melee","Reach","Surplus","Quick","Fully Loaded","Defender","Heavy Hitter","On-Hand"]}
DP27 = {
    "Muzzle":["None","F8 Stabilizer","ISCOVE Flash Hider","L Brake","Mercury Silencer","Recoil Booster","MX Silencer","G28 Compensator"],
    "Barrel":["None","Zac 595MM","Kovalevskaya 604MM","Kovalevskaya 680MM","Empress 490MM"],
    "Optic":random.randrange(0,23),
    "Stock":["None","Zac S3 Tac","Empress SK Adjustable","Empress VZV","Zac S2M"],
    "Underbarrel":["None","Carver Foregrip",'M1930 Strife Angled',"SMLE Pistol Grip","Heavy Foregrip","GF-59 Flashlight","Bipod","Mark VI Skeletal","M1941 Hand Stop"],
    "Magazine":["None","6.5MM Sakura 47 Round","7.62x54MMr 30 Round",".30-06 63 Round","7.62x54MMR 105 Round",".30-06 81 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Disable","Spotter","Sleight of Hand","Fleet","Discard","Hardscope"],
    "Kit":["None","Fast Melee","Reach","Surplus","Quick","Fully Loaded","Defender","Heavy Hitter","On-Hand"]
    }
Type11 = {
    "Muzzle":["None","F8 Stabilizer","ISCOVE Flash Hider","L Brake","Mercury Silencer","Recoil Booster","MX Silencer","G28 Compensator"],
    "Barrel":["None","Sakura 261MM","Warubachi 352MM","Sakura 487MM Shrouded"],
    "Optic":random.randrange(0,22),
    "Stock":["None","Warubachi Type 33","Removed Stock","warubachi Weighted","Shiraishi Custom","Shiraishi Skeletal","Warubachi Padded","Sakura Precision"],
    "Underbarrel":["None","Carver Foregrip",'M1930 Strife Angled',"SMLE Pistol Grip","Heavy Foregrip","GF-59 Flashlight","Bipod","Mark VI Skeletal","M1941 Hand Stop"],
    "Magazine":["None","5.6MM 45 Round","6.5MM Sakura 30 Round","6.5MM Sakura 90 Round","8MM Klauser 30 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Steady","Driller","Sleight of Hand","Brace","Pressure","Fleet"],
    "Kit":["None","Fast Melee","Reach","Surplus","Quick","Fully Loaded","Defender","Heavy Hitter","On-Hand"]}
Bren = {
    "Muzzle":["None","F8 Stabilizer","ISCOVE Flash Hider","L Brake","Mercury Silencer","Recoil Booster","MX Silencer","G28 Compensator"],
    "Barrel":["None","Oak a& Sheild 590MM","Queen's 705MM","Queen's 615MM","Queen's 775M"],
    "Optic":random.randrange(0,22),
    "Stock":["None","Queen's Model 11","Hockenson SP2B","Removed Stock","Oak & Sheild Padded","Oak & Sheild 12B"],
    "Underbarrel":["None","Carver Foregrip",'M1930 Strife Angled',"SMLE Pistol Grip","Heavy Foregrip","GF-59 Flashlight","Bipod","Mark VI Skeletal","M1941 Hand Stop"],
    "Magazine":["None","6.5 Sakura 30 Round",".50 BMG 20 Round",".303 British 100 Round",".50 BMG 50 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Acquisition","Dismantle","Wreck","Tight Grip","Sleight of Hand","Brace"],
    "Kit":["None","Fast Melee","Reach","Surplus","Quick","Fully Loaded","Defender","Heavy Hitter","On-Hand"]}

# Marksman
M1_Grand = {
    "Muzzle":["None","T1 Flash Hider","F8 Stabilizer","Mercury Silencer","G28 Compensator","MX Silencer","L Brake"],
    "Barrel":["None","CGC Ironsides","Cooper 25 Custom","Cooper 21 Shrouded","Chariot 26 Precision"],
    "Optic":random.randrange(0,21),
    "Stock":["None","CGC G2 Thumbhole","Chariot S3 TC","Cooper Adjustable","Chariot S1 Custom","CHC G2 Padded"],
    "Underbarrel":["None","M1930 Strife Angled","Craver Foregrip","Bayonet","Bipod","GF-59 Flashlight","Heavy Foregrip","SMLE Pistol Grip","M1941 Hand Stop"],
    "Magazine":["None",".303 British 8 Round",".30-06 16 Round",".30-06 12 Round","6.5 Sakura 16 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Pressure","Spotter","Acqusition","Sleight of Hand","Hardscope","Vital"],
    "Kit":["None","Fast Melee","Deep Breath","On-Hand","Surplus","Heavy Hitter","Reach","Fully Loaded","Defender"]}
SVT = {
    "Muzzle":["None","T1 Flash Hider","F8 Stabilizer","Mercury Silencer","G28 Compensator","MX Silencer","L Brake"],
    "Barrel":["None","Kovalevskaya 800MM","Kovalevskaya Custom","Zac 400MM","Zac 730MM Precision"],
    "Optic":random.randrange(0,21),
    "Stock":["None","Zac Grip","Removed Stock","Kovalevskaya S02 Weighted","Empress Crown","Crown Padded"],
    "Underbarrel":["None","M1930 Strife Angled","Craver Foregrip","Bayonet","Bipod","GF-59 Flashlight","Heavy Foregrip","SMLE Pistol Grip","M1941 Hand Stop"],
    "Magazine":["None",".303 British 10 Round","7.62x54MMR 15 Round","6.5 Sakura 15 Round","7.62x54MMR 7 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Refresh","Shrouded","Focus","Perfectionist","Vital","Unmarked"],
    "Kit":["None","Fast Melee","Deep Breath","On-Hand","Surplus","Heavy Hitter","Reach","Fully Loaded","Defender"]}
G43 = {
    "Muzzle":["None","T1 Flash Hider","F8 Stabilizer","Mercury Silencer","G28 Compensator","MX Silencer","L Brake"],
    "Barrel":["None","Firzherbert Short","Zp 770MM","Fitzherbert 500MM Rapid","Wyvern Burst","Wyvern 570MM Full-Auto"],
    "Optic":random.randrange(0,21),
    "Stock":["None","Wyvern Skeletal","Fitzherbert Reinforced","ZP Padded","ZP MS02 Custom"],
    "Underbarrel":["None","M1930 Strife Angled","Craver Foregrip","Bayonet","Bipod","GF-59 Flashlight","Heavy Foregrip","SMLE Pistol Grip","M1941 Hand Stop"],
    "Magazine":["None","8MM Klauser 20 Round",".30-06 10 Round","8MM Klauser 8 Round","6.5 Sakura 20 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Steady","Shrouded","Tight Grip","Awareness","Fleet","Quickscope"],
    "Kit":["None","Fast Melee","Deep Breath","On-Hand","Surplus","Heavy Hitter","Reach","Fully Loaded","Defender"]}

# Sniper
Type99 = {
    "Muzzle":["None","T1 Flash Hider","F8 Stabilizer","Mercury Silencer","G28 Compensator","MX Silencer","L Brake"],
    "Barrel":["None","Sakura 776MM","Shiraishi 712MM","Shiraishi Short"],
    "Optic":random.randrange(0,23),
    "Stock":["None","Sakura Wire","Shiraishi Precision","Warubachi Type 40","Sakura CVR Custom","Removed Stock","Warubachi Padded"],
    "Underbarrel":["None","M1930 Strife Angled","Craver Foregrip","Bayonet","Bipod","GF-59 Flashlight","Heavy Foregrip","SMLE Pistol Grip","M1941 Hand Stop"],
    "Magazine":["None","5.6MM 8 Round","6.5MM Sakura 3 Round","8MM Klauser 5 Round","6.5MM Sakura 20 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Discard","Spotter","Hardscope","Perfectionist","Focus","Vital"],
    "Kit":["None","Fast Melee","Deep Breath","On-Hand","Surplus","Heavy Hitter","Reach","Fully Loaded","Defender"]}
_3Line = {
    "Muzzle":["None","T1 Flash Hider","F8 Stabilizer","Mercury Silencer","G28 Compensator","MX Silencer","L Brake"],
    "Barrel":["None","Empress 514MM F01","Kovalevskaya 820MM R1MN","Kovalevskaya 700MM","500MM MN Custom","Empress 700MM","270MM VOZ Carbine"],
    "Optic":random.randrange(0,23),
    "Stock":["None","Empress Marksman","ZAC Custom MZ","MN Custom","Kovalevskaya Weighted","Kovalevskaya S01"],
    "Underbarrel":["None","M1930 Strife Angled","Craver Foregrip","Bayonet","Bipod","GF-59 Flashlight","Heavy Foregrip","SMLE Pistol Grip","M1941 Hand Stop"],
    "Magazine":["None","7.62x54MMR 3 Round",".303 British 5 Round",".30-06 20 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Awareness","Unmarked","Sleight of Hand","Silent Focus","Hardscope","Shrouded"],
    "Kit":["None","Fast Melee","Deep Breath","On-Hand","Surplus","Heavy Hitter","Reach","Fully Loaded","Defender"]}
Kar98 = {
    "Muzzle":["None","T1 Flash Hider","F8 Stabilizer","Scout Silencer","G28 Compensator","SD Silencer","L Brake"],
    "Barrel":["None","VDD 660MM 05HE","Krausnick Scout","VDD REO2k","Krausnick 560MM LW..","Krausnick 520MM Rapid"],
    "Optic":random.randrange(0,23),
    "Stock":["None","VDD Thumbhole","Short Stock","VDD 98","Reisdorf Wire","Krausnick Padded"],
    "Underbarrel":["None","M1930 Strife Angled","Craver Foregrip","Bayonet","Bipod","GF-59 Flashlight","Heavy Foregrip","SMLE Pistol Grip","M1941 Hand Stop"],
    "Magazine":["None","6.5MM Sakura 5 Round","8MM Klauser 3 Round","8MM Klauser 3 Round","5.6MM 20 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Armor Piercing","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Icy Veins","Driller","Unmarked","Fleet","Quickscope","Shrouded","Frenzy"],
    "Kit":["None","Fast Melee","Deep Breath","On-Hand","Surplus","Heavy Hitter","Reach","Fully Loaded","Defender"]}
Anti_Tank = {
    "Muzzle":["None","Iscove Flash Hider","F8 Stabilizer","Mercury Silencer","G28 Compensator","MX Silencer","L Brake"],
    "Barrel":["None","440MM Anastasia Custom","240MM Zac rapid","440MM Kovalevskaya Wrap","420MM Empress"],
    "Optic":random.randrange(0,23),
    "Stock":["None","Zac Custom Precision","Anastasio Type 1A","Zac Adjustable","Zac padded","Anastasia Type 3B Stoyat","Kovalevskaya Type 2 Padded"],
    "Underbarrel":["None","Bayonet","Bipod","GF-59 Flashlight"],
    "Magazine":["None","13MM AM 3 Round","13MM AM 7 Round","13MM AM 10 Round"],
    "Ammo Type":["None","FMJ","Concussive","Explosive"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Focus","Discard","Shrouded","Acquisiton","Driller","Dismantle"],
    "Kit":["None","Fast Melee","Deep Breath","On-Hand","Surplus","Heavy Hitter","Reach","Fully Loaded","Defender"]}

# Pistols
Ratt = {
    "Muzzle":["None","Marauder Flsh Hider","F8 Stabilizer","Mercury Silencer","No.3 Rifle Brake","M1929 Silencer","Strife Compensator"],
    "Barrel":["None","Zac 98MM","Empress 129MM"],
    "Optic":random.randrange(0,16),
    "Stock":["None"],
    "Underbarrel":["None","Lightweight Trigger","Steady trigger","Heavy Trigger","Rapid Action","Hair Trigger"],
    "Magazine":["None","9MM 6 Round","9MM 18 Round","9MM 13 Round","7.62 Gorenko 9 Round",".45 ACP 9 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Sleight of Hand","Acrobatic","Steady","Panic","Perfectionist","Unmarked","Fleet"],
    "Kit":["None","Fast Melee","Quick","On-Hand","Surplus","Heavy Hitter","Reach","Fully Loaded"]}
TopBreak = {
    "Muzzle":["None","Marauder Flsh Hider","F8 Stabilizer","SO Silencer","No.3 Rifle Brake","M1929 Silencer","Strife Compensator"],
    "Barrel":["None","Wilkie W-4 Stub","Wilkie W-7"],
    "Optic":random.randrange(0,16),
    "Stock":["None"],
    "Underbarrel":["None","Lightweight Trigger","Steady trigger","Heavy Trigger","Rapid Action","Hair Trigger"],
    "Magazine":["None","9MM",".30 russion Short"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Acrobatic","Steady","Wreck","Vital Focus","Quickscope","Akimbo"],
    "Kit":["None","Fast Melee","Quick","On-Hand","Surplus","Heavy Hitter","Reach","Fully Loaded"]}
_1911 = {
    "Muzzle":["None","Marauder Flsh Hider","F8 Stabilizer","Mercury Silencer","No.3 Rifle Brake","M1929 Silencer","Strife Compensator"],
    "Barrel":["None","Cooper 6.5","Gracey #1","Gracey Short No.2","Cooper Full-Auto"],
    "Optic":random.randrange(0,15),
    "Stock":["None"],
    "Underbarrel":["None","Lightweight Trigger","Steady trigger","Heavy Trigger","Rapid Action","Hair Trigger"],
    "Magazine":["None",".45 ACP 5 Round","9MM 12 Round",".45 AACP 18 Round",".30 Russion Short 8 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Fleet","Nerves of Steel","Vital","Pinned","Akimbo"],
    "Kit":["None","Fast Melee","Quick","On-Hand","Surplus","Heavy Hitter","Reach","Fully Loaded"]}
Klauser = {
    "Muzzle":["None","Marauder Flsh Hider","F8 Stabilizer","Mercury Silencer","No.3 Rifle Brake","M1929 Silencer","Strife Compensator"],
    "Barrel":["None","Fitzherbert 200MM","Wyvern 170MM"],
    "Optic":random.randrange(0,18),
    "Stock":["None"],
    "Underbarrel":["None","Lightweight Trigger","Steady trigger","Heavy Trigger","Rapid Action","Hair Trigger"],
    "Magazine":["None","9MM 12 Round",".45 ACP 8 round",".45 ACP 12 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Pressure","Driller","Focus","Spotter","Sleight of Hand","Brace","Hardscope"],
    "Kit":["None","Fast Melee","Quick","On-Hand","Surplus","Heavy Hitter","Reach","Fully Loaded"]}
MachinePistol = {
    "Muzzle":["None","Marauder Flsh Hider","F8 Stabilizer","Mercury Silencer","No.3 Rifle Brake","M1929 Silencer","Strife Compensator"],
    "Barrel":["None","Burst-Fire Conversion","VDD 140MM HE","VDD 35MM Short"],
    "Optic":random.randrange(0,18),
    "Stock":["None"],
    "Underbarrel":["None","Lightweight Trigger","Steady trigger","Heavy Trigger","Rapid Action","Hair Trigger"],
    "Magazine":["None","7.62 Gorenko 40 Round","9MM 20 Round","8MM Nambu 20 Round"],
    "Ammo Type":["None","Subsonic","FMJ","Frangible","Incendiary","Lengthened","Hollow Point"],
    "Rear Grip":["None","Rubber","Taped","Leather","Fabric","Grooved","Hatched","Polymer","Pine","Granular","Stippled"],
    "Proficiency":["None","Tight Grip","Brace","Steady","Disable","Panic","Gung-Ho","Akimbo"],
    "Kit":["None","Fast Melee","Quick","On-Hand","Surplus","Heavy Hitter","Reach","Fully Loaded"]}

def rand_attachments(gun):
    muz=""
    bar=""
    optic=""
    stock=""
    under=""
    mag=""
    ammo=""
    grip=""
    prof=""
    kit=""
# ARs
    if "STG" in gun:
        muz=random.choice(STG["Muzzle"])
        bar=random.choice(STG["Barrel"])
        optic=STG["Optic"]
        stock=random.choice(STG["Stock"])
        under=random.choice(STG["Underbarrel"])
        mag=random.choice(STG["Magazine"])
        ammo=random.choice(STG["Ammo Type"])
        grip=random.choice(STG["Rear Grip"])
        prof=random.choice(STG["Proficiency"])
        kit=random.choice(STG["Kit"])
    elif "Automaton" in gun:
        muz=random.choice(Automaton["Muzzle"])
        bar=random.choice(Automaton["Barrel"])
        optic=Automaton["Optic"]
        stock=random.choice(Automaton["Stock"])
        under=random.choice(Automaton["Underbarrel"])
        mag=random.choice(Automaton["Magazine"])
        ammo=random.choice(Automaton["Ammo Type"])
        grip=random.choice(Automaton["Rear Grip"])
        prof=random.choice(Automaton["Proficiency"])
        kit=random.choice(Automaton["Kit"]) 
    elif "Itra Burst" in gun:
        muz=random.choice(IrtaBurst["Muzzle"])
        bar=random.choice(IrtaBurst["Barrel"])
        optic=IrtaBurst["Optic"]
        stock=random.choice(IrtaBurst["Stock"])
        under=random.choice(IrtaBurst["Underbarrel"])
        mag=random.choice(IrtaBurst["Magazine"])
        ammo=random.choice(IrtaBurst["Ammo Type"])
        grip=random.choice(IrtaBurst["Rear Grip"])
        prof=random.choice(IrtaBurst["Proficiency"])
        kit=random.choice(IrtaBurst["Kit"])
    elif "Bar" in gun:
        muz=random.choice(IrtaBurst["Muzzle"])
        bar=random.choice(IrtaBurst["Barrel"])
        optic=IrtaBurst["Optic"]
        stock=random.choice(IrtaBurst["Stock"])
        under=random.choice(IrtaBurst["Underbarrel"])
        mag=random.choice(IrtaBurst["Magazine"])
        ammo=random.choice(IrtaBurst["Ammo Type"])
        grip=random.choice(IrtaBurst["Rear Grip"])
        prof=random.choice(IrtaBurst["Proficiency"])
        kit=random.choice(IrtaBurst["Kit"])
    elif "AS44" in gun:
        muz=random.choice(AS44["Muzzle"])
        bar=random.choice(AS44["Barrel"])
        optic=AS44["Optic"]
        stock=random.choice(AS44["Stock"])
        under=random.choice(AS44["Underbarrel"])
        mag=random.choice(AS44["Magazine"])
        ammo=random.choice(AS44["Ammo Type"])
        grip=random.choice(AS44["Rear Grip"])
        prof=random.choice(AS44["Proficiency"])
        kit=random.choice(AS44["Kit"])
    elif "NZ-41" in gun:
        muz=random.choice(NZ41["Muzzle"])
        bar=random.choice(NZ41["Barrel"])
        optic=NZ41["Optic"]
        stock=random.choice(NZ41["Stock"])
        under=random.choice(NZ41["Underbarrel"])
        mag=random.choice(NZ41["Magazine"])
        ammo=random.choice(NZ41["Ammo Type"])
        grip=random.choice(NZ41["Rear Grip"])
        prof=random.choice(NZ41["Proficiency"])
        kit=random.choice(NZ41["Kit"])
    elif "Volk" in gun:
        muz=random.choice(Volk["Muzzle"])
        bar=random.choice(Volk["Barrel"])
        optic=Volk["Optic"]
        stock=random.choice(Volk["Stock"])
        under=random.choice(Volk["Underbarrel"])
        mag=random.choice(Volk["Magazine"])
        ammo=random.choice(Volk["Ammo Type"])
        grip=random.choice(Volk["Rear Grip"])
        prof=random.choice(Volk["Proficiency"])
        kit=random.choice(Volk["Kit"])
    elif "Cooper Carbine" in gun:
        muz=random.choice(CooperCarbine["Muzzle"])
        bar=random.choice(CooperCarbine["Barrel"])
        optic=CooperCarbine["Optic"]
        stock=random.choice(CooperCarbine["Stock"])
        under=random.choice(CooperCarbine["Underbarrel"])
        mag=random.choice(CooperCarbine["Magazine"])
        ammo=random.choice(CooperCarbine["Ammo Type"])
        grip=random.choice(CooperCarbine["Rear Grip"])
        prof=random.choice(CooperCarbine["Proficiency"])
        kit=random.choice(CooperCarbine["Kit"])

# SMGs
    elif "MP-40" in gun:
        muz=random.choice(MP40["Muzzle"])
        bar=random.choice(MP40["Barrel"])
        optic=MP40["Optic"]
        stock=random.choice(MP40["Stock"])
        under=random.choice(MP40["Underbarrel"])
        mag=random.choice(MP40["Magazine"])
        ammo=random.choice(MP40["Ammo Type"])
        grip=random.choice(MP40["Rear Grip"])
        prof=random.choice(MP40["Proficiency"])
        kit=random.choice(MP40["Kit"])
    elif "Sten" in gun:
        muz=random.choice(STEN["Muzzle"])
        bar=random.choice(STEN["Barrel"])
        optic=STEN["Optic"]
        stock=random.choice(STEN["Stock"])
        under=random.choice(STEN["Underbarrel"])
        mag=random.choice(STEN["Magazine"])
        ammo=random.choice(STEN["Ammo Type"])
        grip=random.choice(STEN["Rear Grip"])
        prof=random.choice(STEN["Proficiency"])
        kit=random.choice(STEN["Kit"])
    elif "M1928" in gun:
        muz=random.choice(M1928["Muzzle"])
        bar=random.choice(M1928["Barrel"])
        optic=M1928["Optic"]
        stock=random.choice(M1928["Stock"])
        under=random.choice(M1928["Underbarrel"])
        mag=random.choice(M1928["Magazine"])
        ammo=random.choice(M1928["Ammo Type"])
        grip=random.choice(M1928["Rear Grip"])
        prof=random.choice(M1928["Proficiency"])
        kit=random.choice(M1928["Kit"])
    elif "Owen Gun" in gun:
        muz=random.choice(OwenGun["Muzzle"])
        bar=random.choice(OwenGun["Barrel"])
        optic=OwenGun["Optic"]
        stock=random.choice(OwenGun["Stock"])
        under=random.choice(OwenGun["Underbarrel"])
        mag=random.choice(OwenGun["Magazine"])
        ammo=random.choice(OwenGun["Ammo Type"])
        grip=random.choice(OwenGun["Rear Grip"])
        prof=random.choice(OwenGun["Proficiency"])
        kit=random.choice(OwenGun["Kit"])
    elif "Type 100" in gun:
        muz=random.choice(Type100["Muzzle"])
        bar=random.choice(Type100["Barrel"])
        optic=Type100["Optic"]
        stock=random.choice(Type100["Stock"])
        under=random.choice(Type100["Underbarrel"])
        mag=random.choice(Type100["Magazine"])
        ammo=random.choice(Type100["Ammo Type"])
        grip=random.choice(Type100["Rear Grip"])
        prof=random.choice(Type100["Proficiency"])
        kit=random.choice(Type100["Kit"])
    elif "PPSH-41" in gun:
        muz=random.choice(PPSH["Muzzle"])
        bar=random.choice(PPSH["Barrel"])
        optic=PPSH["Optic"]
        stock=random.choice(PPSH["Stock"])
        under=random.choice(PPSH["Underbarrel"])
        mag=random.choice(PPSH["Magazine"])
        ammo=random.choice(PPSH["Ammo Type"])
        grip=random.choice(PPSH["Rear Grip"])
        prof=random.choice(PPSH["Proficiency"])
        kit=random.choice(PPSH["Kit"])

# Shotty
    elif "Einhorn Revolving" in gun:
        muz=random.choice(Horn["Muzzle"])
        bar=random.choice(Horn["Barrel"])
        optic=Horn["Optic"]
        stock=random.choice(Horn["Stock"])
        under=random.choice(Horn["Underbarrel"])
        mag=random.choice(Horn["Magazine"])
        ammo=random.choice(Horn["Ammo Type"])
        grip=random.choice(Horn["Rear Grip"])
        prof=random.choice(Horn["Proficiency"])
        kit=random.choice(Horn["Kit"])
    elif "Combat Shotgun" in gun:
        muz=random.choice(GraceyAuto["Muzzle"])
        bar=random.choice(GraceyAuto["Barrel"])
        optic=GraceyAuto["Optic"]
        stock=random.choice(GraceyAuto["Stock"])
        under=random.choice(GraceyAuto["Underbarrel"])
        mag=random.choice(GraceyAuto["Magazine"])
        ammo=random.choice(GraceyAuto["Ammo Type"])
        grip=random.choice(GraceyAuto["Rear Grip"])
        prof=random.choice(GraceyAuto["Proficiency"])
        kit=random.choice(GraceyAuto["Kit"])
    elif "Gracey Auto" in gun:
        muz=random.choice(GraceyAuto["Muzzle"])
        bar=random.choice(GraceyAuto["Barrel"])
        optic=GraceyAuto["Optic"]
        stock=random.choice(GraceyAuto["Stock"])
        under=random.choice(GraceyAuto["Underbarrel"])
        mag=random.choice(GraceyAuto["Magazine"])
        ammo=random.choice(GraceyAuto["Ammo Type"])
        grip=random.choice(GraceyAuto["Rear Grip"])
        prof=random.choice(GraceyAuto["Proficiency"])
        kit=random.choice(PPSH["Kit"])
    elif "Double Barrel" in gun:
        muz=random.choice(DoubleBarrel["Muzzle"])
        bar=random.choice(DoubleBarrel["Barrel"])
        optic=DoubleBarrel["Optic"]
        stock=random.choice(DoubleBarrel["Stock"])
        under=random.choice(DoubleBarrel["Underbarrel"])
        mag=random.choice(DoubleBarrel["Magazine"])
        ammo=random.choice(DoubleBarrel["Ammo Type"])
        grip=random.choice(DoubleBarrel["Rear Grip"])
        prof=random.choice(DoubleBarrel["Proficiency"])
        kit=random.choice(DoubleBarrel["Kit"])

# LMGs
    elif "MG42" in gun:
        muz=random.choice(MG42["Muzzle"])
        bar=random.choice(MG42["Barrel"])
        optic=MG42["Optic"]
        stock=random.choice(MG42["Stock"])
        under=random.choice(MG42["Underbarrel"])
        mag=random.choice(MG42["Magazine"])
        ammo=random.choice(MG42["Ammo Type"])
        grip=random.choice(MG42["Rear Grip"])
        prof=random.choice(MG42["Proficiency"])
        kit=random.choice(MG42["Kit"])
    elif "DP27" in gun:
        muz=random.choice(DP27["Muzzle"])
        bar=random.choice(DP27["Barrel"])
        optic=DP27["Optic"]
        stock=random.choice(DP27["Stock"])
        under=random.choice(DP27["Underbarrel"])
        mag=random.choice(DP27["Magazine"])
        ammo=random.choice(DP27["Ammo Type"])
        grip=random.choice(DP27["Rear Grip"])
        prof=random.choice(DP27["Proficiency"])
        kit=random.choice(DP27["Kit"])
    elif "Type 11" in gun:
        muz=random.choice(Type11["Muzzle"])
        bar=random.choice(Type11["Barrel"])
        optic=Type11["Optic"]
        stock=random.choice(Type11["Stock"])
        under=random.choice(Type11["Underbarrel"])
        mag=random.choice(Type11["Magazine"])
        ammo=random.choice(Type11["Ammo Type"])
        grip=random.choice(Type11["Rear Grip"])
        prof=random.choice(Type11["Proficiency"])
        kit=random.choice(Type11["Kit"])
    elif "Bren" in gun:
        muz=random.choice(Bren["Muzzle"])
        bar=random.choice(Bren["Barrel"])
        optic=Bren["Optic"]
        stock=random.choice(Bren["Stock"])
        under=random.choice(Bren["Underbarrel"])
        mag=random.choice(Bren["Magazine"])
        ammo=random.choice(Bren["Ammo Type"])
        grip=random.choice(Bren["Rear Grip"])
        prof=random.choice(Bren["Proficiency"])
        kit=random.choice(Bren["Kit"])

# Marksman
    elif "M1 Garand" in gun:
        muz=random.choice(M1_Grand["Muzzle"])
        bar=random.choice(M1_Grand["Barrel"])
        optic=M1_Grand["Optic"]
        stock=random.choice(M1_Grand["Stock"])
        under=random.choice(M1_Grand["Underbarrel"])
        mag=random.choice(M1_Grand["Magazine"])
        ammo=random.choice(M1_Grand["Ammo Type"])
        grip=random.choice(M1_Grand["Rear Grip"])
        prof=random.choice(M1_Grand["Proficiency"])
        kit=random.choice(M1_Grand["Kit"])
    elif "SVT-40" in gun:
        muz=random.choice(SVT["Muzzle"])
        bar=random.choice(SVT["Barrel"])
        optic=SVT["Optic"]
        stock=random.choice(SVT["Stock"])
        under=random.choice(SVT["Underbarrel"])
        mag=random.choice(SVT["Magazine"])
        ammo=random.choice(SVT["Ammo Type"])
        grip=random.choice(SVT["Rear Grip"])
        prof=random.choice(SVT["Proficiency"])
        kit=random.choice(SVT["Kit"])
    elif "G-43" in gun:
        muz=random.choice(G43["Muzzle"])
        bar=random.choice(G43["Barrel"])
        optic=G43["Optic"]
        stock=random.choice(G43["Stock"])
        under=random.choice(G43["Underbarrel"])
        mag=random.choice(G43["Magazine"])
        ammo=random.choice(G43["Ammo Type"])
        grip=random.choice(G43["Rear Grip"])
        prof=random.choice(G43["Proficiency"])
        kit=random.choice(G43["Kit"])

# Sniper
    elif "Type 99" in gun:
        muz=random.choice(Type99["Muzzle"])
        bar=random.choice(Type99["Barrel"])
        optic=Type99["Optic"]
        stock=random.choice(Type99["Stock"])
        under=random.choice(Type99["Underbarrel"])
        mag=random.choice(Type99["Magazine"])
        ammo=random.choice(Type99["Ammo Type"])
        grip=random.choice(Type99["Rear Grip"])
        prof=random.choice(Type99["Proficiency"])
        kit=random.choice(Type99["Kit"])
    elif "3-Line Rifle" in gun:
        muz=random.choice(_3Line["Muzzle"])
        bar=random.choice(_3Line["Barrel"])
        optic=_3Line["Optic"]
        stock=random.choice(_3Line["Stock"])
        under=random.choice(_3Line["Underbarrel"])
        mag=random.choice(_3Line["Magazine"])
        ammo=random.choice(_3Line["Ammo Type"])
        grip=random.choice(_3Line["Rear Grip"])
        prof=random.choice(_3Line["Proficiency"])
        kit=random.choice(_3Line["Kit"])
    elif "Kar98k" in gun:
        muz=random.choice(Kar98["Muzzle"])
        bar=random.choice(Kar98["Barrel"])
        optic=Kar98["Optic"]
        stock=random.choice(Kar98["Stock"])
        under=random.choice(Kar98["Underbarrel"])
        mag=random.choice(Kar98["Magazine"])
        ammo=random.choice(Kar98["Ammo Type"])
        grip=random.choice(Kar98["Rear Grip"])
        prof=random.choice(Kar98["Proficiency"])
        kit=random.choice(Kar98["Kit"])
    elif "Gorenko Anti-Tank Rifle" in gun:
        muz=random.choice(Anti_Tank["Muzzle"])
        bar=random.choice(Anti_Tank["Barrel"])
        optic=Anti_Tank["Optic"]
        stock=random.choice(Anti_Tank["Stock"])
        under=random.choice(Anti_Tank["Underbarrel"])
        mag=random.choice(Anti_Tank["Magazine"])
        ammo=random.choice(Anti_Tank["Ammo Type"])
        grip=random.choice(Anti_Tank["Rear Grip"])
        prof=random.choice(Anti_Tank["Proficiency"])
        kit=random.choice(Anti_Tank["Kit"])

# Piston
    elif "Ratt" in gun:
        muz=random.choice(Ratt["Muzzle"])
        bar=random.choice(Ratt["Barrel"])
        optic=Ratt["Optic"]
        stock=random.choice(Ratt["Stock"])
        under=random.choice(Ratt["Underbarrel"])
        mag=random.choice(Ratt["Magazine"])
        ammo=random.choice(Ratt["Ammo Type"])
        grip=random.choice(Ratt["Rear Grip"])
        prof=random.choice(Ratt["Proficiency"])
        kit=random.choice(Ratt["Kit"])
    elif "Top Break" in gun:
        muz=random.choice(TopBreak["Muzzle"])
        bar=random.choice(TopBreak["Barrel"])
        optic=TopBreak["Optic"]
        stock=random.choice(TopBreak["Stock"])
        under=random.choice(TopBreak["Underbarrel"])
        mag=random.choice(TopBreak["Magazine"])
        ammo=random.choice(TopBreak["Ammo Type"])
        grip=random.choice(TopBreak["Rear Grip"])
        prof=random.choice(TopBreak["Proficiency"])
        kit=random.choice(TopBreak["Kit"])
    elif "1911" in gun:
        muz=random.choice(_1911["Muzzle"])
        bar=random.choice(_1911["Barrel"])
        optic=_1911["Optic"]
        stock=random.choice(_1911["Stock"])
        under=random.choice(_1911["Underbarrel"])
        mag=random.choice(_1911["Magazine"])
        ammo=random.choice(_1911["Ammo Type"])
        grip=random.choice(_1911["Rear Grip"])
        prof=random.choice(_1911["Proficiency"])
        kit=random.choice(_1911["Kit"])
    elif "Klauser" in gun:
        muz=random.choice(Klauser["Muzzle"])
        bar=random.choice(Klauser["Barrel"])
        optic=Klauser["Optic"]
        stock=random.choice(Klauser["Stock"])
        under=random.choice(Klauser["Underbarrel"])
        mag=random.choice(Klauser["Magazine"])
        ammo=random.choice(Klauser["Ammo Type"])
        grip=random.choice(Klauser["Rear Grip"])
        prof=random.choice(Klauser["Proficiency"])
        kit=random.choice(Klauser["Kit"])
    elif "Machine Pistol" in gun:
        muz=random.choice(MachinePistol["Muzzle"])
        bar=random.choice(MachinePistol["Barrel"])
        optic=MachinePistol["Optic"]
        stock=random.choice(MachinePistol["Stock"])
        under=random.choice(MachinePistol["Underbarrel"])
        mag=random.choice(MachinePistol["Magazine"])
        ammo=random.choice(MachinePistol["Ammo Type"])
        grip=random.choice(MachinePistol["Rear Grip"])
        prof=random.choice(MachinePistol["Proficiency"])
        kit=random.choice(MachinePistol["Kit"])

# Launcher
    elif "M1 Bazooka" in gun:
        muz=""
        bar=""
        optic=""
        stock=""
        under=""
        mag=""
        ammo=""
        grip=""
        prof=""
        kit=""
    elif "Panzerchreck" in gun:
        muz=""
        bar=""
        optic=""
        stock=""
        under=""
        mag=""
        ammo=""
        grip=""
        prof=""
        kit=""
    elif "Panzerfaust" in gun:
        muz=""
        bar=""
        optic=""
        stock=""
        under=""
        mag=""
        ammo=""
        grip=""
        prof=""
        kit=""
    elif "MK11 Launcher" in gun:
        muz=""
        bar=""
        optic=""
        stock=""
        under=""
        mag=""
        ammo=""
        grip=""
        prof=""
        kit=""

# Mele
    elif "Combat Sheid" in gun:
        muz=""
        bar=""
        optic=""
        stock=""
        under=""
        mag=""
        ammo=""
        grip=""
        prof=""
        kit=""
    elif "Knife" in gun:
        muz=""
        bar=""
        optic=""
        stock=""
        under=""
        mag=""
        ammo=""
        grip=""
        prof=""
        kit=""

# Just to be safe
    else:
        muz=""
        bar=""
        optic=""
        stock=""
        under=""
        mag=""
        ammo=""
        grip=""
        prof=""
        kit=""
    
    att_all = str(muz),str(bar),"Optic # "+str(optic),str(stock),str(under),str(mag),str(ammo),str(grip),str(prof),str(kit)
    string_att = ' | '.join(att_all)

    return string_att
