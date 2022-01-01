import random

lethals= ["Incendiary Gernade","Frag"," Gammon Bomb", "Throwing Knife", "Thermite","Demolition Charge","Molotov"]
tactical = ["Stun","Smoke","Stim","Gas Gernade","S-Mine", "Decoy"]

def lethal():
    in_game_lethal = random.choice(lethals)
    return in_game_lethal

def tac():
    in_game_tac = random.choice(tactical)
    return in_game_tac