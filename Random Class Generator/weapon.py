import random

def weapons():
    AR = ["STG", "Automaton", "Itra Burst","Bar"," AS44","MP-40","Volk","Cooper Carbine"]
    SMG = ["MP-40", "Sten", "M1928", "Owen Gun","Type 100", "PPSH-41"]
    Shotty = ["Einhorn Revolving", "Combat Shotgun","Gracey Auto", "Double Barrel"]
    LMG = ["MG42","DP27","Type 11","Bren"]
    Marksman = ["M1 Garand","SVT-40","G-43"]
    Sniper = ["Type 99","3-Line Rifle","Kar98k","Gorenko Anti-Tank Rifle"]
    Pistols = ["Ratt","Top Break","1911","Klauser","Machine Pistol"]
    Launchers = ["M1 Bazooka","Panzerchreck", "Panzerfaust", "MK11 Launcher"]
    Mele = ["Combat Sheild", "Knife"]
    
    allWepons = [AR,SMG,Shotty,LMG,Marksman,Sniper,Pistols,Launchers,Mele]
    weponCategory = allWepons.index(random.choice(allWepons))
    category = (allWepons[weponCategory])
    randomGun = random.choice(category)
    cat_gun_combo = ""

    if category == AR:
        cat_gun_combo= "AR: " + randomGun
    elif category == SMG:
        cat_gun_combo="SMG: "+ randomGun
    elif category == Shotty:
        cat_gun_combo="Shotgun: "+ randomGun
    elif category == LMG:
        cat_gun_combo="LMG: "+ randomGun
    elif category == Marksman:
        cat_gun_combo="Marksman: "+ randomGun
    elif category == Sniper:
        cat_gun_combo="Sniper: "+ randomGun
    elif category == Pistols:
        cat_gun_combo="Pistol: "+ randomGun
    elif category == Launchers:
        cat_gun_combo= "Launcher: "+ randomGun
    else:
        cat_gun_combo="Mele: "+ randomGun
        
    return cat_gun_combo

