from typing import Text
import time
import random
import os
import re
from urllib.request import urlopen

#main shit
#---------------------------------------------------------------
def mainpart():
    armourtype = "no armour"
    saveto = ""
    AC = 10
    Shield = ""
    looppusher = 1
    Sbonus = 0
    Dbonus = 0
    CObonus = 0
    Ibonus = 0 
    Wbonus = 0
    CHbonus = 0
    bufferint = 0
    npchpdt = 0
    dietype = 0
    npchpda = 0
    npchp = 0
    q = 0
    v = 0
    Sbuff = 0
    Dbuff = 0
    CObuff = 0
    Ibuff = 0
    Wbuff = 0
    CHbuff = 0
    Sstat = 0
    Dstat = 0
    COstat = 0
    Istat = 0
    Wstat = 0
    CHstat = 0
    npcname = "placeholder"
    rases = []
    cwd = os.getcwd()
    cwdirt  = cwd + "\\RacialBonuses.txt"
    #files = os.listdir(cwd)
#finding the stats
#--------------------------------------------------------------
    print("loaded")
    print("I'll need some info to build your npc")
    print("first, what is your npc's name? ")
    npcname = input()
    time.sleep(1)
    with open(cwdirt) as f:
        rases = f.readlines()
    races = [h[:-1] for h in rases]
    print("(note: there are 68 races you can chose from as found on https://summoninggrounds.com/5e-racial-stat-bonus-chart/)")
    #Btxt = input("please type the file path of the RacialBonus.txt now, make sure to include 2 slashes not just 1  ")
    print("What race is ", npcname, "? (Is case sensitive so look at the website to see how its written, also there are no spaces)", sep='')
    npcrace = input()
    #print(rases)
    #print(races[0])
    howmanyarepicked = 0
    while(looppusher == 1):
        if(npcrace == races[v] and v < 442):
            Sbonus2 = int(races[v+1])
            Dbonus2 = int(races[v+2])
            CObonus2 = int(races[v+3])
            Ibonus2 = int(races[v+4])
            Wbonus2 = int(races[v+5])
            CHbonus2 = int(races[v+6])
            break
        elif(npcrace != races[v]):
            v=v+7
        elif(npcrace == races[v] and v == 442):
            CHbonus2 = 2
            print("You chose Changeling, you can pick to add 1 to S, D, CO, I, or W. Type 1 of those letters to add the +1 to it")
            CustomBonus = input()
            if(CustomBonus == 'S'):
                Sbonus2 = 1
                break
            elif(CustomBonus == 'D'):
                Dbonus2 = 1
                break
            elif(CustomBonus == 'CO'):
                CObonus2 = 1
                break
            elif(CustomBonus == 'I'):
                Ibonus2 = 1
                break
            elif(CustomBonus == 'W'):
                Wbonus2 = 1
                break
            else:
                print("please type an S, D, CO, I, or W")
        elif(npcrace == races[v] and v == 449):
            CObonus2 = 2
            print("You chose Simic Hybrid, you can pick to add 1 to S, D, I, W, or CH. Type 1 of those letters to add the +1 to it")
            CustomBonus = input()
            if(CustomBonus == 'S'):
                Sbonus2 = 1
                break
            elif(CustomBonus == 'D'):
                Dbonus2 = 1
                break
            elif(CustomBonus == 'CH'):
                CObonus2 = 1
                break
            elif(CustomBonus == 'I'):
                Ibonus2 = 1
                break
            elif(CustomBonus == 'W'):
                Wbonus2 = 1
                break
            else:
                print("please type an S, D, I, W, or CH")
        elif(npcrace == races[v] and v == 456):
            CObonus2 = 2
            print("You chose Warforged, you can pick to add 1 to S, D, I, W, or CH. Type 1 of those letters to add the +1 to it")
            CustomBonus = input()
            if(CustomBonus == 'S'):
                Sbonus2 = 1
                break
            elif(CustomBonus == 'D'):
                Dbonus2 = 1
                break
            elif(CustomBonus == 'CH'):
                CObonus2 = 1
                break
            elif(CustomBonus == 'I'):
                Ibonus2 = 1
                break
            elif(CustomBonus == 'W'):
                Wbonus2 = 1
                break
            else:
                print("please type an S, D, I, W, or CH")
        elif(npcrace == races[v] and v == 463):
            CHbonus2 = 2
            print("You chose Half-Elf, you can pick to add 1 to S, D, CO, I, or W. Type 2 of those letters to add the +1 to it")
            CustomBonus = input()
            if(CustomBonus == 'S'):
                Sbonus2 = 1
                howmanyarepicked = howmanyarepicked + 1
            elif(CustomBonus == 'D'):
                Dbonus2 = 1
                howmanyarepicked = howmanyarepicked + 1
            elif(CustomBonus == 'CO'):
                CObonus2 = 1
                howmanyarepicked = howmanyarepicked + 1
            elif(CustomBonus == 'I'):
                Ibonus2 = 1
                howmanyarepicked = howmanyarepicked + 1
            elif(CustomBonus == 'W'):
                Wbonus2 = 1
                howmanyarepicked = howmanyarepicked + 1
            elif(howmanyarepicked == 2):
                break
            else:
                print("please type an S, D, CO, I, or W")
        elif(npcrace == races[v] and v == 442):
            CHbonus2 = 2
            print("You chose Variant Human, you can pick to add 1 to S, D, CO, I, W, CH. Type 2 of those letters to add the +1 to it")
            CustomBonus = input()
            if(CustomBonus == 'S'):
                Sbonus2 = 1
                howmanyarepicked = howmanyarepicked + 1
            elif(CustomBonus == 'D'):
                Dbonus2 = 1
                howmanyarepicked = howmanyarepicked + 1
            elif(CustomBonus == 'CO'):
                CObonus2 = 1
                howmanyarepicked = howmanyarepicked + 1
            elif(CustomBonus == 'I'):
                Ibonus2 = 1
                howmanyarepicked = howmanyarepicked + 1
            elif(CustomBonus == 'W'):
                Wbonus2 = 1
                howmanyarepicked = howmanyarepicked + 1
            elif(howmanyarepicked == 2):
                break
            else:
                print("please type an S, D, CO, I, or W")
    print("Alright you've picked ", npcrace, " you will recieve the following buffs", sep='')
    print("Str +", Sbonus2)
    print("Dex +", Dbonus2)
    print("Con +", CObonus2)
    print("Int +", Ibonus2)
    print("Wis +", Wbonus2)
    print("Cha +", CHbonus2)
    time.sleep(.5)
    print("Next we can find the S.D.CO.I.W.CH")
    time.sleep(1)
    print("First step, add any stat bonuses")
    print("so if you have a +2 to a stat you would write '2'. If there is no bonus type in '0'")
    print("type in the numerical bonus for strength")
    Sbonus = input()
    print("type in the numerical bonus for dexterity")
    Dbonus = input()
    print("type in the numerical bonus for constitution")
    CObonus = input()
    print("type in the numerical bonus for intelligence")
    Ibonus = input()
    print("type in the numerical bonus for wisdom")
    Wbonus = input()
    print("type in the numerical bonus for charisma")
    CHbonus = input()
    print("now the stats will be randomized")
    Sstat = random.randint(3,18)
    Sstat = Sstat + int(Sbonus) + Sbonus2
    time.sleep(1)
    Sbuff = (Sstat-10)//2
    print(npcname, "'s strength is", Sstat, "; which is a +", Sbuff," bonus")
    Dstat = random.randint(3,18)
    Dstat = Dstat + int(Dbonus) + Dbonus2
    time.sleep(1)
    Dbuff = (Dstat-10)//2
    print(npcname,"'s dexterity is", Dstat, "; which is a +", Dbuff, " bonus")
    print(npcname, " also has a +",Dbuff," to initiative")
    COstat = random.randint(3,18)
    COstat = COstat + int(CObonus) + CObonus2
    time.sleep(1)
    CObuff = (COstat-10)//2
    print(npcname, "'s constitution is", COstat, "; which is a +", CObuff, " bonus")
    Istat = random.randint(3,18)
    Istat = Istat + int(Ibonus) + Ibonus2
    time.sleep(1)
    Ibuff = (Istat-10)//2
    print(npcname, "'s intelligence is", Istat, ";which is a +", Ibuff, " bonus")
    Wstat = random.randint(3,18)
    Wstat = Wstat + int(Wbonus) + Wbonus2
    time.sleep(1)
    Wbuff = (Wstat-10)//2
    print(npcname, "'s wisdom is", Wstat, "; which is a +", Wbuff," bonus")
    CHstat = random.randint(3,18)
    CHstat = CHstat + int(CHbonus)  + CHbonus2
    time.sleep(1)
    CHbuff = (CHstat-10)//2
    print(npcname, "'s charisma is", CHstat, "; which is a +", CHbuff," bonus")
    time.sleep(.75)
#proficiency
#---------------------------------------------------------------------------------
    proflist = []
    x2 = 0
    x = int(x2)
    whatprof = 0
    print("secondly you can apply profiency to any skill(s) you want")
    print("the skills will be written like this 'skill name(what stat it's infulenced by) the number that you type to give proficiency.")
    print("for example 'Stealth(Dex) 17'")
    print("Firstly what proficiency bonus does ", npcname, " have", sep='')
    profbonus = input()
    print("Secondly how many proficiencys do you want ", npcname, " to have?", sep = '')
    howmanyprof2 = input()
    howmanyprof = int(howmanyprof2)
    print("here is a list of all the skills")
    print("'Acrobatics(Dex) 1', 'Animal Handling(Wis) 2', 'Arcana(Int) 3'")
    time.sleep(.1)
    print("'Athletics(Str) 4, 'Deception(Cha) 5', 'History(Int) 6")
    time.sleep(.1)
    print("'Insight(Wis) 7', 'Intimidation(Cha) 8', 'Investigation(Int) 9'")
    time.sleep(.1)
    print("'Medicine(Wis) 10', 'Nature(Int) 11', 'Perception(Wis) 12 ")
    time.sleep(.1)
    print("'Performance(Cha) 13', 'Persuasion(Cha) 14', 'Religion(Int) 15")
    time.sleep(.1)
    print("'Sleight Of Hand(Dex) 16', Stealth(Dex) 17','Survival(Wis) 18")
    time.sleep(1)
    #print(howmanyprof)
    while(looppusher == 1):
        print("What proficiency do you want ", npcname, " to have?", sep = '')
        whatprof2 = input()
        whatprof = int(whatprof2)
        print(whatprof)
        if(whatprof == 1):
            print("Adding 'Acrobatics to ", npcname, sep='')
            proflist.append("Acrobatics")
            x=x+1
        if(whatprof == 2):
            print("Adding 'Animal Handling' to ", npcname, sep='')
            proflist.append("Animal Handling")
            x=x+1
        if(whatprof == 3):
            print("Adding 'Arcana' to ", npcname, sep='')
            proflist.append("Arcana")
            x=x+1
        if(whatprof == 4):
            print("Adding 'Athletics' to ", npcname, sep='')
            proflist.append("Athletics")
            x=x+1
        if(whatprof == 5):
            print("Adding 'Deception' to ", npcname, sep='')
            proflist.append("Deception")
            x=x+1
        if(whatprof == 6):
            print("Adding 'History' to ", npcname, sep='')
            proflist.append("History")
            x=x+1
        if(whatprof == 7):
            print("Adding 'Insight' to ", npcname, sep='')
            proflist.append("Insight")
            x=x+1
        if(whatprof == 8):
            print("Adding 'Intimidation' to ", npcname, sep='')
            proflist.append("Intimidation")
            x=x+1
        if(whatprof == 9):
            print("Adding 'Investigation' to ", npcname, sep='')
            proflist.append("Investigation")
            x=x+1
        if(whatprof == 10):
            print("Adding 'Medicine' to ", npcname, sep='')
            proflist.append("Medicine")
            x=x+1
        if(whatprof == 11):
            print("Adding 'Nature' to ", npcname, sep='')
            proflist.append("Nature")
            x=x+1
        if(whatprof == 12):
            print("Adding 'Perception' to ", npcname, sep='')
            proflist.append("Perception")
            x=x+1
        if(whatprof == 13):
            print("Adding 'Performance' to ", npcname, sep='')
            proflist.append("Performance")
            x=x+1
        if(whatprof == 14):
            print("Adding 'Persuasion' to ", npcname, sep='')
            proflist.append("Persuasion")
            x=x+1
        if(whatprof == 15):
            print("Adding 'Religion' to ", npcname, sep='')
            proflist.append("Religion")
            x=x+1
        if(whatprof == 16):
            print("Adding 'Sleight of Hand' to ", npcname, sep='')
            proflist.append("Sleight of Hand")
            x=x+1
        if(whatprof == 17):
            print("Adding 'Stealth' to ", npcname, sep='')
            proflist.append("Stealth")
            x=x+1
        if(whatprof == 18):
            print("Adding 'Survival' to ", npcname, sep='')
            proflist.append("Survival")
            x=x+1
        elif(whatprof >= 19):
            print("That is not a number between 1-18")
        elif(x == howmanyprof):
            print("You've now decided your proficiency(s)")
            break
    if(howmanyprof > 1 and howmanyprof < 19):
        print('Great! ', npcname, " has a +", profbonus, " in ", proflist, sep='')
    elif(howmanyprof >= 19):
        print("Hoof ", npcname, " has a whole lot of proficiency and they get a +", profbonus, " to ", proflist, sep='')
    elif(howmanyprof <= 0):
        print(npcname, " has no proficiencies, but thats okay")
        
#finding the hp
#------------------------------------------------------------------
    while(looppusher == 1):
        print("next I'll need the hit die type [4,6,8,10,12,20, or 100]")
        npchpdt = input()
        if(npchpdt == "4"):
            dietype = dietype + 4
            time.sleep(.75)
            print("you have selected a d",dietype, sep = '')
            break
        elif(npchpdt == "6"):
            dietype = dietype + 6
            time.sleep(.75)
            print("you have selected a d",dietype, sep = '')
            break
        elif(npchpdt == "8"):
            dietype = dietype + 8
            time.sleep(.75)
            print("you have selected a d",dietype, sep = '')
            break
        elif(npchpdt == "10"):
            dietype = dietype + 10
            time.sleep(.75)
            print("you have selected a d",dietype, sep = '')
            break
        elif(npchpdt == "12"):
            dietype = dietype + 12
            time.sleep(.75)
            print("you have selected a d",dietype, sep = '')
            break
        elif(npchpdt == "20"):
            dietype = dietype + 20
            time.sleep(.75)
            print("you have selected a d",dietype, sep = '')
            break
        elif(npchpdt == "100"):
            dietype = dietype + 100
            time.sleep(.75)
            print("you have selected a d",dietype, sep = '')
            break
        else:
            print("please put a number in the brackets")

    time.sleep(1)
    print("then, enter the amount of hit dice")
    npchpda = input()
    time.sleep(1)
    while(q!=int(npchpda)):
        bufferint = random.randint(1,dietype)
        npchp = npchp + bufferint
        q = q + 1
    npchp = npchp + CObuff
    print(npcname, "'s HP is ", npchp)
#AC
#-------------------------------------------------------------
    print("next I'll caclulate your NPC's AC")
    print("a list of armour will show up and to select one simply type the name of the armour (case sensitive)")
    print("if you want no armour tpye in 'no armour'")
    print("'leather armour' 11AC+D Light")
    time.sleep(.1)
    print("'padded armour' 11AC+D Light")
    time.sleep(.1)
    print("'breastplate' 14AC+D (up to +2) Medium")
    time.sleep(.1)
    print("'halfplate' 15AC+D (up to +2) Medium")
    time.sleep(.1)
    print("'chainmail' 16AC Heavy")
    time.sleep(.1)
    print("'plate' 18AC Heavy")
    time.sleep(1)
    
    while(looppusher == 1):
        print("choose an armour type")
        armourtype = input()
        if(armourtype == "leather armour"):
            AC = 11 + Dbuff
            print("you have selected 'leather armour' which gives ", npcname, " an AC of ", AC )
            break
        elif(armourtype == "padded armour"):
            AC = 11 + Dbuff
            print("you have selected 'padded armour' which gives ", npcname, " an AC of ", AC )
            break
        elif(armourtype == "breastplate"):
            AC = 14 + Dbuff
            if(AC > 16):
                AC = 16
            elif(AC < 14):
                AC = 14
                print("you have selected 'breastplate' which gives ", npcname, " an AC of ", AC )
            break
        elif(armourtype == "halfplate"):
            AC = 15 + Dbuff
            if(AC > 17):
                AC = 17
            elif(AC < 13):
                AC = 13
            print("you have selected 'halfplate' which gives ",npcname, " an AC of ", AC )
            break
        elif(armourtype == "chainmail"):
            AC = 16 
            print("you have selected 'chainmail' which gives ",npcname, " an AC of ", AC )
            break
        elif(armourtype == "plate"):
            AC = 18 
            print("you have selected 'plate' which gives ",npcname, " an AC of ", AC )
            break
        elif(armourtype == "no armour"):
            AC = 10 + Dbuff
            time.sleep(.25)
            print("you have selected 'no armour' which does not provide any AC buffs giving", npcname, " and AC of ", AC)
            break
        else:
            print("make sure you have typed in the name correctly (remember it's case and space sensitive)")
    time.sleep(.5)
    while(looppusher == 1):
        print("would you like to add a shield, this add +2 AC (y/n)")
        Shield = input()
        if(Shield == "y"):
            AC = AC + 2
            print("ok, adding a shield now ", npcname, " now has an AC of ", AC)
            break
        elif(Shield == "n"):
            print("ok, no shield will be added ", npcname,"'s AC is still ", AC)
            break
        else:
            print("please type a 'y' or a 'n'")
#save to .txt
#------------------------------------------------------------
    ConSbuff = str(Sbuff)
    ConDbuff=str(Dbuff)
    ConCObuff=str(CObuff)
    ConIbuff=str(Ibuff)
    ConWbuff=str(Wbuff)
    ConCHbuff=str(CHbuff)
    ConSstat=str(Sstat)
    ConDstat=str(Dstat)
    ConCOstat=str(COstat)
    ConIstat=str(Istat)
    ConWstat=str(Wstat)
    ConCHstat= str(CHstat)
    ConAC = str(AC)
    ConNpchp = str(npchp)
    ConProfBonus = str("+" + profbonus)
    Conproflist  = str(proflist)
    line1 = npcname + "'s HP is " + ConNpchp
    line2 = npcname + "'s hit die are d" + npchpdt + "s"
    line3 = npcname + " has a " + ConSstat + " in Strength, which gives" + npcname + " a strength modifer of " + ConSbuff
    line4 = npcname + " has a " + ConDstat + " in Dexterity, which gives" + npcname + " a dexterity modifer of " + ConDbuff + " and hence has a initative bonus of " + ConDbuff
    line5 = npcname + " has a " + ConCOstat + " in Constitution, which gives" + npcname + " a constitution modifer of +" + ConCObuff
    line6 = npcname + " has a " + ConIstat + " in Intellegence, which gives" + npcname + " a intellegence modifer of +" + ConIbuff
    line7 = npcname + " has a " + ConWstat + " in Wisdom, which gives" + npcname + " a wisdom modifer of " + ConWbuff
    line8 = npcname + " has a " + ConCHstat + " in Charisma, which gives" + npcname + " a charisma modifer of " + ConCHbuff
    line9 = npcname + " has " + ConAC + "AC because they have " + armourtype + " and a shield"
    line9alt =  npcname + " has " + ConAC + "AC because they have " + armourtype + " and no shield"
    line8_5 = npcname + "'s proficiencies are " + Conproflist + " with a bonus of" + ConProfBonus

    while(looppusher == 1):
        print("would you like to say to .txt (y/n)")
        saveto = input()
        if(saveto == "y"):
            print("please type in the directory you want [ex. C:\\Users\\Joe\\DnD]")
            dirt = input()
            os.chdir(dirt)
            print('writing to "NPCStats.txt"')
            text_file = open("NPCStats.txt", "w")
            text_file.write(line1)
            text_file.write('\n')
            text_file.write(line2)
            text_file.write('\n')
            text_file.write(line3)
            text_file.write('\n')
            text_file.write(line4)
            text_file.write('\n')
            text_file.write(line5)
            text_file.write('\n')
            text_file.write(line6)
            text_file.write('\n')
            text_file.write(line7)
            text_file.write('\n')
            text_file.write(line8)
            text_file.write('\n')
            text_file.write(line8_5)
            text_file.write('\n')
            if(Shield == "y"):
                text_file.write(line9)
            else:
                text_file.write(line9alt)
            text_file.close()
            print("saved 'NPCStats.txt' in ", dirt, sep = '')
            break
        elif(saveto == "n"):
            print("ok! The stats will not be saved to a .txt file")
            break
        else:
            print("please type a 'y' or a 'n'")
#loading stuff
#---------------------------------------------------------------
def loadingtext(): 
    print ("loading")
    time.sleep(.5)
    print ("loading.")
    time.sleep(.5)
    print ("loading..")
    time.sleep(.5)
    print ("loading...")
    time.sleep(.5)
#welcome Text
#----------------------------------------------------------------
looppusher2 = 1
restart = ""
while(looppusher2 == 1):
    print ("Welcome To DnD NPC stat generator v1.5.5")
    print ("this program lets you create random stats for NPC's in DnD")
    #opening
    #----------------------------------------------------------------
    while(looppusher2 == 1):
        print("press the 's' key to start")
        start_key = input()
        if start_key == ("s"):
            loadingtext()
            time.sleep(.5)
            loadingtext()
            mainpart()
            print("Thanks for using DnD NPC stat generator v1.5.5")                
    #thanks_for_using
    #-----------------------------------------------------------------