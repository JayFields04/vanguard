import random

perk_One = ["Fortified", "Survival Training","Ninja","Dauntless","Ghost","Cold Blooded","Serpentine"]
perk_Two = ["Tracker","Radar","High Alert","Engineer","Forward Intel","Piercing Vision","Intuition"]
perk_Three = ["Double Time","Demolition","Lightweight","Overkill","Tactician","Scavenger"]

def bluePerk():
    in_game_perk_one = random.choice(perk_One)
    return in_game_perk_one

def redPerk():
    in_game_perk_two = random.choice(perk_Two)
    return in_game_perk_two

def yellowPerk():
    in_game_perk_three = random.choice(perk_Three)
    return in_game_perk_three