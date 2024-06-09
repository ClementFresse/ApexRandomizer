# -*- coding: utf-8 -*-

###\/\/\/ IMPORTS \/\/\/###


import tkinter as tk
import datetime as dt
import time
import string
import random


###/\/\/\ IMPORTS /\/\/\###
###\/\/\/ DEFINITIONS \/\/\/###


# We need a list with all the legends and a list with all the weapons
legendList = ['-----ALTER----------------',
              '----------------ASH-------',
              '-----BALLISTIC------------',
              '--------BANGALORE---------',
              '---BLOODHOUND-------------',
              '-------------CATALYST-----',
              '-----CAUSTIC--------------',
              '-----------------CONDUIT--',
              '----CRYPTO----------------',
              '----------FUSE------------',
              '----GIBRALTAR-------------',
              '-------------HORIZON------',
              '------------LIFELINE------',
              '------LOBA----------------',
              '------------MAD-MAGGIE----',
              '---MIRAGE-----------------',
              '-------NEWCASTLE----------',
              '-------OCTANE-------------',
              '-----------PATHFINDER-----',
              '------RAMPART-------------',
              '------------REVENANT------',
              '---SEER-------------------',
              '-------------VALKYRIE-----',
              '-----VANTAGE--------------',
              '----------WATTSON---------',
              '----------------WRAITH----']

weaponList = ['------------HAVOC-RIFLE---',
              '-------VK47-FLATLINE------',
              '---HEMLOCK-BURST-AR-------',
              '-------------R301-CARBINE-',
              '---NEMESIS-BURST-AR-------',
              '------ALTERNATOR-SMG------',
              '--PROWLER-BURST-PDW-------',
              '------------R99-SMG-------',
              '-----VOLT-SMG-------------',
              '-------------C.A.R.-SMG---',
              '------DEVOTION-LMG--------',
              '-----------L-STAR-EMG-----',
              '-----M600-SPITFIRE--------',
              '--RAMPAGE-LMG-------------',
              '--------G7-SCOUT----------',
              '---TRIPLE-TAKE------------',
              '---------30-30-REPEATER---',
              '----BOCEK-COMPOUND-BOW----',
              '----------CHARGE-RIFLE----',
              '--LONGBOW-DMR-------------',
              '--KRABER-.50-CAL-SNIPER---',
              '-------------SENTINEL-----',
              '-------EVA-8-AUTO---------',
              '---------MASTIFF-SHOTGUN--',
              '----MOZAMBIQUE-SHOTGUN----',
              '------PEACEKEEPER---------',
              '-----------RE-45-AUTO-----',
              '----------------P2020-----',
              '---WINGMAN----------------']

def fillStrings(List,String,Length):
    """
    This function fill every string of a List with the String caracter\n
    so that every string has the defined Length.
    """
    for i in range(len(List)):
        while len(List[i])<=Length:
            List[i] = List[i]+String
    print(List)

def randomize():
    """
    This function selects the loadout at random and does a pretty cool animation.
    """
    for i in range(75):
        blabla = string.ascii_uppercase+string.digits+string.punctuation
        randomBlabla1 = ''.join(random.choice(blabla) for i in range(26))
        legendSelection.configure(text=randomBlabla1)
        randomBlabla2 = ''.join(random.choice(blabla) for i in range(26))
        weaponSelection.configure(text=randomBlabla2)
        time.sleep(0.05)
        root.update()
    legend = random.choice(legendList)
    legendSelection.configure(text=legend)
    weapon = random.choice(weaponList)
    weaponSelection.configure(text=weapon)
    timeNow = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    save = open("Choices list.txt","a")
    save.write(legend+" | "+weapon+" | "+timeNow+"\n")
    save.close()


###/\/\/\ DEFINITIONS /\/\/\###
###\/\/\/ CREATING THE APP \/\/\/###


root = tk.Tk()
root.configure(background="black")
root.geometry("900x350")
root.resizable(False, False)

# These voids are just here to space the widgets out
void1 = tk.Label(root, padx=30, pady=20, bg="black")
void1.grid(column=0, row=0)
void2 = tk.Label(root, padx=30, pady=20, bg="black")
void2.grid(column=2, row=0)
void3 = tk.Label(root, padx=30, pady=20, bg="black")
void3.grid(column=4, row=2)

# It ain't much but it's honest work
randomizeLegendButton = tk.Button(root, text="RANDOMIZE", command=randomize, font=("aptos", 20))
randomizeLegendButton.grid(column=1, row=1, columnspan=15)
legendSelectionTitle = tk.Label(root, text="Legend selection:", bg="black", fg="green", font=("aptos", 20))
legendSelectionTitle.grid(column=3, row=3)
legendSelection = tk.Label(root, text="--------------------------", bg="black", fg="green", font=("noto mono", 20),)
legendSelection.grid(column=5, row=3, columnspan=5)
weaponSelectionTitle = tk.Label(root, text="Weapon selection:", bg="black", fg="green", font=("aptos", 20))
weaponSelectionTitle.grid(column=3, row=4)
weaponSelection = tk.Label(root, text="--------------------------", bg="black", fg="green", font=("noto mono", 20))
weaponSelection.grid(column=5, row=4, columnspan=5)

root.mainloop()