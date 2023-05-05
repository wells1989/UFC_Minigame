money = 2000
fame = 0
wrestling = 0
striking = 0
grappling = 0

name = input("Welcome to the UFC Mini game. Please type your name. ")

style = input("What is your style? wrestling / striking / grappling: ").lower()

if style == "wrestling":
    wrestling += 10

elif style == "striking":
    striking += 10

elif style == "grappling":
    grappling += 10

else:
    print("Please choose your style")

print("You have saved up", money, "dollars and want to try to become a Mixed Martial Artist")
choice_location = input("Do you want to a/ compete locally ($200) or b/ move to the USA? ($1000) ").lower()

if choice_location == "a":
    money -= 200
    if money <= 0:
        quit()
    choice_gym = input("Pick a gym. You can choose a/ wrestling at Ian's ($50), b/ Muay Thai with All Powers ($50), or c/ Aikido with Johnny. ($70) ").lower()

    if choice_gym == "a":
        money -= 50
        if money <= 0:
            quit()
        wrestling += 50
        grappling += 25

    elif choice_gym == "b":
        money -= 70
        if money <= 0:
            quit()
        striking += 50

    elif choice_gym == "c":
        money -= 100
        if money <= 0:
            quit()
        striking += 25

    else:
        print("Please select (a /b / c) to continue. ")

elif choice_location == "b":
    money -= 1000
    if money <= 0:
        quit()
    choice_gym = input("Pick a gym. You can choose a/ AKA in California ($200), b/ The Blackzilians in Florida ($250), or c/ Jiu Jitsu with the Gracie's. ($250) ").lower()

    if choice_gym == "a":
        money -= 200
        if money <= 0:
            quit()
        wrestling += 50
        grappling += 50

    elif choice_gym == "b":
        money -= 250
        if money <= 0:
            quit()
        striking += 75
        wrestling += 25
        grappling += 25

    elif choice_gym == "c":
        money -= 250
        if money <= 0:
            quit()
        grappling += 75
        fame += 25

    else:
        print("Please select (a /b / c) to continue. ")

else:
    print("Please select a or b to continue. ")

import random
opponent_a_wrestling = random.randint(0,100)
opponent_a_striking = random.randint(0,100)
opponent_a_grappling = random.randint(0,100)

opponent_b_wrestling = random.randint(0,100)
opponent_b_striking = random.randint(0,100)
opponent_b_grappling = random.randint(0,100)

fight_choice = input("Choose a fight, either a/ against opponent a, or b/ against opponent b: ").lower()

if fight_choice == "a":
    if (wrestling + striking + grappling) > (opponent_a_grappling + opponent_a_striking + opponent_a_wrestling):
        print("You won the fight!")
        money += 5000
        fame += 50

    elif (wrestling + striking + grappling) < (opponent_a_grappling + opponent_a_striking + opponent_a_wrestling):
        print("You lost the fight!")
        money += 1000
        fame += 25

elif fight_choice == "b":
    if (wrestling + striking + grappling) > (opponent_b_grappling + opponent_b_striking + opponent_b_wrestling):
        print("You won the fight!")
        money += 5000
        fame += 50

    elif (wrestling + striking + grappling) < (opponent_b_grappling + opponent_b_striking + opponent_b_wrestling):
        print("You lost the fight!")
        money += 1000
        fame += 25

else:
    print("please select a fight, a or b")

print("You made", str(money), "$")
if fame < 25:
    print("You made some fans!")

else:
    print("You didn't make that many fans, maybe make different choices next time!")