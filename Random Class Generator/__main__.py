from tkinter import *
import webbrowser
import attachments,lethals,perks,weapon

global blueP
global redP
global yellowP
global lethal_choice
global tac_choice
global weaponChoice
global attach

gun_mod = weapon.weapons()

def callback(url):
    webbrowser.open_new_tab(url)

def refresh():
    gun_mod= weapon.weapons()
    blueP.config(text =perks.bluePerk())
    redP.config(text=perks.redPerk())
    yellowP.config(text=perks.yellowPerk())
    lethal_choice.config(text=lethals.lethal())
    tac_choice.config(text=lethals.tac())
    weaponChoice.config(text=gun_mod)
    attach.config(text=attachments.rand_attachments(gun_mod))

window = Tk()
window.title("Vanguard Random Class Generator")
window.geometry("800x600+30+30")
window.resizable(False, False)
window.configure(bg = "#272727")

# Myself
xoqution_tag = Label(window, text ="twitch.tv/XOQution", font = ("verdana",10), fg = "#14A76C", bg = "#272727", cursor="hand2")
xoqution_tag.pack(pady=(4,0))
xoqution_tag.bind("<Button-1>",lambda e: callback("https://www.twitch.tv/xoqution"))

# Random Generated Wepons and Attachments Below
prim_weapon = Label(window,text="The gun you must use is...", font = "verdana", fg = "#272727", bg = "#FF652F")
prim_weapon.pack(fill = X,pady=(10,0))
weaponChoice = Label(window, font = "verdana",fg="white",bg="#272727", text=gun_mod)
weaponChoice.pack()
attach = Label(window,text = attachments.rand_attachments(gun_mod),font = "verdana",fg="white",bg="#272727", wraplength= 500)
attach.pack()


# Random Generated Perks below
perks_label = Label(window,text="Perks", font = "verdana", fg = "#272727",bg = "#FFE400")
perks_label.pack(fill = X,pady=(40,0))
blueP = Label(window,text=perks.bluePerk(),font="verdana",fg = "white",bg = "#272727")
blueP.pack()
redP = Label(window,text=perks.redPerk(),font="verdana",fg = "white",bg = "#272727")
redP.pack()
yellowP = Label(window,text=perks.yellowPerk(),font="verdana",fg = "white",bg = "#272727")
yellowP.pack()

# Random Generated Lethals and Tacticals Below
le = Label(window,text="Lethal and Tacticals", font = "verdana", fg = "#272727",bg = "#14A76C")
le.pack(fill = X,pady=(40,0))
lethal_choice = Label(window,text=lethals.lethal(),font="verdana",fg = "white",bg = "#272727")
lethal_choice.pack()
tac_choice = Label(window,text=lethals.tac(),font="verdana",fg = "white",bg = "#272727")
tac_choice.pack()

# Refresh and Exit
refresh_button = Button(window, text="Roll", font = "verdana", bg = "white", command=refresh, cursor="hand2")
refresh_button.pack(padx=220, side = LEFT)
exit_button = Button(window, text="Exit", command=window.destroy, font = "verdana", bg = "white", cursor="hand2")
exit_button.pack(padx=5, side = LEFT)

window.mainloop()