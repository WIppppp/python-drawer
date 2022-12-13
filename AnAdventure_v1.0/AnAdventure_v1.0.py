import random
import time

# ----------------------------------
# Events

E1 = "You are infront of a tree."
E2 = "A Goblin threathens you with robbing your gold!\n"
E3 = "A Troll is triying to step on you\n"
E4 = "A KingRat Tries to bite you\n"


Dialogues = ["You feel hungry, but your adventure hunger is more", "You see a bird on a tree", "*whistles*", "You see a worm digging to hide into the ground", "You feel good", "You try to whistle, you fail."]
Shop_Dialogues = ["Howdy young traveler, Welcome to my shop. Here are my offers...", "Heya, Here are the things i sell", "... Thy things are right there.", "HEY HEY HEY HEY HEY HEY HEY HEY, things are under there"]
# ----------------------------------

# Enemies

class Goblin:
    Name = "Goblin"
    HP = 30 # 0-30
    DMG = 4
    Money = 20
    XP = 5

class Troll:
    Name = "Troll"
    HP = 60 # 0-60
    DMG = 13
    Money = 50
    XP = 20

class KingRat:
    Name = "KingRat"
    HP = 15
    DMG = 4
    Money = 5
    XP = 3
# Shops

shop0 = {
    "Wooden Sword": "A hard wood sword (100 Money)",
    "Stick": "A hard wood sword (20 Money)",
    "Bandage": "Can cure wounds (40 Money)"
}

shop1 = {
    "Wooden Sword": "A hard wood sword (150 Money)",
    "Stick": "A hard wood sword (15 Money)",
    "Bandage": "Can cure wounds (20 Money)"
}

shop2 = {
    "Wooden Sword": "A hard wood sword (80 Money)",
    "Stick": "A hard wood sword (40 Money)",
    "Bandage": "Can cure wounds (120 Money)"
}

shop3 = {
    "Wooden Sword": "A hard wood sword (30 Money)",
    "Stick": "A hard wood sword (0 Money)",
    "Bandage": "Can cure wounds (100 Money)"
}

# Objects

all_objs = {
    "Wooden Sword": "A hard wood sword (7 Dmg)",
    "Stick": "A hard wood sword (4 Dmg)",
    "Bare Hands": "Your bare hands (3 Dmg)",
    "Bandage": "Can cure wounds (20+ HP)"
}

# ----------------------------------
class Player:
    HP = 100 # 0-100
    Power = 100 # 0-100
    LV = 1 # 0-25
    XP = 0 # 0-25
    Money = 0 # 0-inf
    Holding = "Wooden Sword"
    Buffs = {
        
    }
    Inventory = {
        "Wooden Sword": "A hard wood sword (7 Dmg)",
        "Bandage": "Can cure wounds (20+ HP)",
        "Stick": "A hard wood sword (4 Dmg)"

    }

def Ingame():
    current_event = ""
    print("Use WASD to move!")


    while True:

        command = input("\n>> ")
        if current_event == "":
            pass

        elif current_event == "E1":
            if command == "W":
                print("Theres a tree infront you! You cant move foward.")
                continue
            elif command == "A" or command == "S" or command == "D":
                current_event = ""
                pass
            else:
                pass
        else:
            pass

        if command == "W" or command == "A" or command == "S" or command == "D":
            event = random.randrange(0,25)
            if event == 1:
                current_event = "E1"
                print(E1)
            if event == 2:
                current_event = "E2"
                print(E2)
                time.sleep(2)
                Combat(Goblin)
            if event == 3:
                current_event = "E3"
                print(E3)
                time.sleep(2)
                Combat(Troll)
            if event == 4:
                current_event = "E4"
                print(E4)
                time.sleep(2)
                Combat(KingRat)
            else:
                dialogue_prob = random.randrange(0,6)
                print(Dialogues[dialogue_prob])
                time.sleep(1)
        elif command == "Commands":
            print("-- Command List --\n\nW, A, S, D - Movement\ninventory - Opens the inventory\nhold (object in inventory) - Makes you hold the object you want\nstats - Shows you Power, Level and HP\nrest - Restores your power\nuse (object in inventory) - Uses an object\nshop - You walk to a nearby shop to buy things\nsave - Opens save\'s menu")
        
        elif command == "inventory":
            inv_len = len(Player.Inventory)
            print("-"*15)
            print("{}/10 Space used in backpack\n".format(inv_len))
            for obj in Player.Inventory:
                print(obj, "-", Player.Inventory[obj])
            print("-"*15)

        elif "hold" in command:
            if "Wooden Sword" in command:
                for obj in Player.Inventory:
                    if obj == "Wooden Sword":
                        Player.Holding = "Wooden Sword"
                        print("Equipped Wooden Sword")
                        break
                    else:
                        print("Object not found in the inventory!\n")
                        break

            elif "Stick" in command:
                for obj in Player.Inventory:
                    if obj == "Stick":
                        Player.Holding = "Stick"
                        print("Equipped Stick")
                        break
                    else:
                        print("Object not found in the inventory!\n")
                        break
                
            elif "Bare Hands" in command:
                Player.Holding = "Bare Hands"
                print("Sucefully equipped Bare Hands")
                continue
            else:
                print("Unknown Object!")
                continue

        elif command == "stats":
            print("-"*15)
            print("\nHP: {}\nPower: {}\nLV: {}\nXP: {}\nMoney: {}\nActually holding: {}\n".format(Player.HP, Player.Power, Player.LV, Player.XP, Player.Money, Player.Holding))
            print("-"*15)

        elif command == "rest":
            Player.Power = 100
            print("You lay down at the ground, You see the skies and suddently fall asleep...")
            time.sleep(5)
            print("Minutes later you wake up with your power restored and prepared to go into the adventure again.")
            continue

        elif "use" in command:
            if "Bandage" in command:
                if Player.HP == 100:
                    print("You already have max health!")
                    continue
                else:
                    pass
                Player.HP = Player.HP + 20
                if Player.HP > 100:
                    Player.HP = 100
                else:
                    pass
                Player.Inventory.pop("Bandage")
                print("You used a Bandage, You have {} HP now.".format(Player.HP))
            elif command == "use":
                print("Write something to use.")
            else:
                pass
        elif command == "shop":
            print("You walk to the most nearby shop...")
            # time.sleep(5)
            shop_select = random.randrange(0,4)

            if shop_select == 0:
                print(Shop_Dialogues[shop_select], "\n")
                print("-"*15)
                for obj in dict(shop0):
                    print(obj, "-",shop0[obj])
                print("\n","-"*15)
                shopping("shop0")

            elif shop_select == 1:
                print(Shop_Dialogues[shop_select], "\n")
                print("-"*15)
                for obj in dict(shop1):
                    print(obj, "-",shop2[obj])
                print("\n","-"*15)
                shopping("shop1")

            elif shop_select == 2:
                print(Shop_Dialogues[shop_select], "\n")
                print("-"*15)
                for obj in dict(shop2):
                    print(obj, "-",shop2[obj])
                print("\n","-"*15)
                shopping("shop2")

            elif shop_select == 3:
                print(Shop_Dialogues[shop_select], "\n")
                print("-"*15)
                for obj in dict(shop3):
                    print(obj, "-",shop3[obj])
                print("\n","-"*15)
                shopping("shop3")

            else:
                pass
        
        #elif command == "save":
        #    savemenu()

        elif command == "combat rat":
            Combat(KingRat)
        elif command == "combat goblin":
            Combat(Goblin)
        elif command == "combat troll":
            Combat(Troll)
        elif command == "exit":
            exit()

        else:
            print("Unknown command!  Write \"Commands\" for more info!")
            continue

def Combat(enemy):

    class current_enemy:
        name = enemy.Name
        hp = enemy.HP
        total_hp = enemy.HP
        dmg = enemy.DMG
        money = enemy.Money
        xp = enemy.XP

    print("-"*15)
    print("A {} jumps into the battle!".format(current_enemy.name))
    print("-"*15,'\n')

    if Player.Holding == "Bare Hands":
        attack_dmg = 3
        sup_attack_dmg = 6
    elif Player.Holding == "Stick":
        attack_dmg = 4
        sup_attack_dmg = 8
    elif Player.Holding == "Wooden Sword":
        attack_dmg = 7
        sup_attack_dmg = 14
    else:
        print("Error 404 PLAYER.HOLDING = N/A")

    while True:

        if Player.HP <= 0:
            if Player.Money < current_enemy.money:
                print("You got defeated by {}...\nYou are so poor that the {} feels bad for you and dosent robs you".format(current_enemy.name, current_enemy.name))
                Player.HP = 1
                return 0
            else:
                Player.Money = Player.Money - current_enemy.money
                print("You got defeated by {}...\nAnd the {} robs you {} coins...".format(current_enemy.name, current_enemy.name, current_enemy.money))
                Player.HP = 1
                return 0
        else:
            pass

        if current_enemy.hp <= 0:
            Player.Money = Player.Money + current_enemy.money
            Player.XP = Player.XP + current_enemy.xp
            if IsLVUP(Player.LV, Player.XP) == True:
                print("You defeated the {}!\nYou got {} money from it!\n\nYou leveled up to level {}!".format(current_enemy.name, current_enemy.money,Player.LV))
                return 1
            else:
                print("You defeated the {}!\nYou got {} money from it!\n\n+{}xp".format(current_enemy.name, current_enemy.money, current_enemy.xp))
                return 1
        else:
            pass

        if Player.HP > 100:
            Player.HP = 100
        else:
            pass

        if Player.Power > 100:
            Player.Power = 100
        else:
            pass


        def_def = False
        command = input("What you do?\n\nattack - Normal Attack ({} dmg)\nsupattack - You do a stronger attack ({} dmg)\nheal - You heal yourself (+5hp)(+4Power)\ndefend - You try to defend yourself\nPower left: {}\nHP Left: {}\n\n>> ".format(attack_dmg, sup_attack_dmg, Player.Power, Player.HP))
        if command == "attack":
            if Player.Power < 3:
                print("You dont have enough power to attack!")
                continue
            current_enemy.hp = current_enemy.hp - attack_dmg
            Player.Power = Player.Power - 3
            if current_enemy.hp < 0:
                current_enemy.hp = 0
            else:
                pass
            print("-"*15)
            print("You hit {} Damage!".format(attack_dmg))
            print("The {} HP {}/{} ".format(current_enemy.name, current_enemy.hp, current_enemy.total_hp))
            print("-"*15)
            
        elif command == "supattack":
            if Player.Power < 10:
                print("You dont have enough power to perform a super attack!")
                continue
            Player.Power = Player.Power - 10
            current_enemy.hp = current_enemy.hp - sup_attack_dmg
            print("-"*15)
            print("You hit {} Damage!".format(sup_attack_dmg))
            print("The {} HP {}/{} ".format(current_enemy.name, current_enemy.hp, current_enemy.total_hp))
            print("-"*15)

        elif command == "heal":
            if Player.HP >= 100:
                print("You already have 100 HP")
                hp_cmd = 0
                pass
            else:
                hp_cmd = 1
                Player.HP = Player.HP + 5
                Player.Power = Player.Power + 4
                print("You restored 5 HP and 4 Power!")
                print("You now have {} HP".format(Player.HP))
            if Player.Power >= 100:
                print("You already have 100 power!")
                pw_cmd = 0
            else:
                pw_cmd = 1
                Player.Power = Player.Power + 4
            if hp_cmd == 0 and pw_cmd == 0:
                continue
            else:
                pass

        elif command == "defend":
            def_chance = random.randrange(0,6)
            if def_chance < 4:
                def_def = True
            else:
                def_def = False
                def_msg = "You couldnt defend!\n"
        elif command == "kill":
            current_enemy.hp = 0
        else:
            print("Unknown Command!")
            continue
        if command == "defend":
            if def_def == False:
                print(def_msg)
            else:
                pass
        else:
            pass    

        if def_def == True:
            print("You sucessfully defended yourself! and the {} hit no damage!".format(current_enemy.name))
            pass
        else:
            Player.HP = Player.HP - current_enemy.dmg
            print("The {} hit {} Damage!\n".format(current_enemy.name,current_enemy.dmg))

def IsLVUP(actual_level, current_xp):
    
    max_xp = actual_level * 25

    if current_xp >= max_xp:
        Player.XP = 0
        Player.LV = Player.LV + 1
        return True
    
    elif current_xp < max_xp:
        return False
    else:
        print("Error.")

def savemenu():

    file_exists_check = ("")

    while True:
        try:
            file_exists_check = open("savefile_1.py", "r")
        except FileNotFoundError:
            save1name = "EMPTY"
        


        try:
            file_exists_check = open("savefile_2.py", "r")
        except FileNotFoundError:
            save2name = "EMPTY"
        


        try:
            file_exists_check = open("savefile_3.py", "r")
        except FileNotFoundError:
            save3name = "EMPTY"
        



        print("-- SAVE MENU --")
        print("\n  SAVE1 - {}\n  SAVE2 - {}\n  SAVE3 - {}".format(save1name, save2name, save3name))
        time.sleep(1)
        want_save_or_load = input("\n You want to load a file or save your progress into one?  To go back type \"back\"\n\n>> ")
        if want_save_or_load == "save":
            save_file = input("\n In what file you want to save your file? (e.g 1)\n>>")
            if not save_file == "1" or save_file == "2" or save_file == "3":
                print("Unknown Command!")
                continue
            else:
                try:
                    save_file_ = open(("savefile_{}.py".format(save_file)), "x")
                except FileExistsError:
                    overwrite = input("This file already exists and contains data, do you want to overwrite it anyways? Y/N\n>> ")
                    if overwrite == "Y":
                        pass
                    elif overwrite == "N":
                        continue
                    else:
                        print("Unknown Command!")
                        continue
            save_file_ = open("savefile_{}.py".format(save_file), "w")
            save_name = input("Insert a name to identify your save\n>>")

            save_file_.write("""
            # SAVE{} - {}

            class Player:
                HP = {} # 0-100
                Power = {} # 0-100
                LV = {} # 0-25
                XP = {} # 0-25
                Money = {} # 0-inf
                Holding = {}
                Buffs = {}
                Inventory = {}
            """.format(save_file, save_name, Player.HP, Player.Power, Player.LV, Player.XP, Player.Money, Player.Holding, Player.Buffs, Player.Inventory))
            save_file_.close()
            print("Save sucessful.")
            return

        elif want_save_or_load == "load":
            load_file = input("\n What file you want to load? (e.g 1)\n>>")
            if load_file == "1":
                try:
                    import savefile_1.py as sv1
                    Player = sv1.Player
                except ModuleNotFoundError:
                    print("SAVE 1 File doesn't exists!")
                    continue
                print("Sucessfully loaded SAVE 1!")

            elif load_file == "2":
                try:
                    import savefile_2.py as sv2
                    Player = sv2.Player
                except ModuleNotFoundError:
                    print("SAVE 2 File doesn't exists!")
                    continue
                print("Sucessfully loaded SAVE 2!")
            elif load_file == "3":
                try:
                    import savefile_3.py as sv3
                    Player = sv3.Player
                except ModuleNotFoundError:
                    print("SAVE 1 File doesn't exists!")
                    continue
                print("Sucessfully loaded SAVE 3!")
            else:
                print("Unknown command!")
                continue
        
        elif want_save_or_load == "back":
            return
        else:
            print("Unknown Command!")
            continue

def shopping(shop):
    if shop == "shop0":
        Wooden_Sword = random.randrange(100,201)
        Stick = random.randrange(20,41)
        Bandage = random.randrange(40,81)
        
        while True:
            wachu_wanna_buy_mate = input("So anything you wanna buy? (e.g Wooden Sword)\n>> ")
            if wachu_wanna_buy_mate == "Wooden Sword":

                if shop_ifs(Wooden_Sword, wachu_wanna_buy_mate) == 0:
                    continue
                else:
                    return

            elif wachu_wanna_buy_mate == "Stick":

                if shop_ifs(Wooden_Sword, wachu_wanna_buy_mate) == 0:
                    continue
                else:
                    return

            elif wachu_wanna_buy_mate == "Bandage":

                if shop_ifs(Wooden_Sword, wachu_wanna_buy_mate) == 0:
                    continue
                else:
                    return

            elif wachu_wanna_buy_mate == "back":
                return
            else:
                print("Unknown Command!\n")

    elif shop == "shop1":
        Wooden_Sword = random.randrange(150,301)
        Stick = random.randrange(15,31)
        Bandage = random.randrange(20,41)
        
        while True:

            wachu_wanna_buy_mate = input("So anything you wanna buy? (e.g Wooden Sword)\n>> ")
            if wachu_wanna_buy_mate == "Wooden Sword":

                if shop_ifs(Wooden_Sword, wachu_wanna_buy_mate) == 0:
                    continue
                else:
                    return

            elif wachu_wanna_buy_mate == "Stick":

                if shop_ifs(Wooden_Sword, wachu_wanna_buy_mate) == 0:
                    continue
                else:
                    return

            elif wachu_wanna_buy_mate == "Bandage":

                if shop_ifs(Wooden_Sword, wachu_wanna_buy_mate) == 0:
                    continue
                else:
                    return

            elif wachu_wanna_buy_mate == "back":
                return
            else:
                print("Unknown Command!\n")

# 80,40,120 | 30,0,100

    elif shop == "shop2":

        Wooden_Sword = random.randrange(80,161)
        Stick = random.randrange(40,81)
        Bandage = random.randrange(120,241)
        
        while True:
            wachu_wanna_buy_mate = input("So anything you wanna buy? (e.g Wooden Sword)\n>> ")
            if wachu_wanna_buy_mate == "Wooden Sword":

                if shop_ifs(Wooden_Sword, wachu_wanna_buy_mate) == 0:
                    continue
                else:
                    return

            elif wachu_wanna_buy_mate == "Stick":

                if shop_ifs(Wooden_Sword, wachu_wanna_buy_mate) == 0:
                    continue
                else:
                    return

            elif wachu_wanna_buy_mate == "Bandage":

                if shop_ifs(Wooden_Sword, wachu_wanna_buy_mate) == 0:
                    continue
                else:
                    return

            elif wachu_wanna_buy_mate == "back":
                return
            else:
                print("Unknown Command!\n")
# 80,40,120 | 30,0,100
    elif shop == "shop3":
        Wooden_Sword = random.randrange(30,61)
        Stick = 0
        Bandage = random.randrange(100,201)
        
        while True:
            wachu_wanna_buy_mate = input("So anything you wanna buy? (e.g Wooden Sword)\n>> ")
            if wachu_wanna_buy_mate == "Wooden Sword":

                if shop_ifs(Wooden_Sword, wachu_wanna_buy_mate) == 0:
                    continue
                else:
                    return

            elif wachu_wanna_buy_mate == "Stick":

                if shop_ifs(Wooden_Sword, wachu_wanna_buy_mate) == 0:
                    continue
                else:
                    return

            elif wachu_wanna_buy_mate == "Bandage":

                if shop_ifs(Wooden_Sword, wachu_wanna_buy_mate) == 0:
                    continue
                else:
                    return

            elif wachu_wanna_buy_mate == "back":
                return
            else:
                print("Unknown Command!\n")

def shop_ifs(item, ubuyd):
    while True:

        for i in Player.Inventory:
            if i == ubuyd:
                print("You already have this item in your inventory.")
                return 0

        if Player.Money < item:
            print("You are too poor to buy this")
            return 0

        elif len(Player.Inventory) >= 10:
            print("Your inventory is full.")
            return 0
        else:
            Player.Money  = Player.Money - item
            Player.Inventory["{}".format(ubuyd)] = "A hard wood sword (7 Dmg)"
            print("Thanks for buying a {}!".format(ubuyd))
            return 1
                    
Ingame()