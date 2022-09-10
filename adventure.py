#Adventure Game
#Name Input / Start

name = input("Quick, Doc! They are waking up! Hey there adventurer, it looks like you took a pretty rough tumble down that hill, my name is Bailey, what's yours? ")

answer = input("\n" + "Well " + name + " I know you have to get to it, the Doc fixed you right up and the road is just that way, good luck! " + "*You get up and start walking on the path and come to a cross road, would you like to go left or right?* ")

if answer == "right":
    answer = input("\n" + "You come upon a large river with a very flimsy bridge connecting each side, would you like to cross the bridge or swim through the river? *Please type bridge or swim*")
    if answer == "bridge":
        answer = input("\n" + "You made it across the bridge! Oh no! You have been greeted by a giant mutant bear! Would you like to try and fight the bear or run away? *Please type fight or run* ")
        if answer == "fight":
            answer = input("\n" + "You manage to fight off the bear giving you the opportunity to escape! You've run into deep into the forest, would you like to set up camp or keep walking? *Please type camp or walk* ")
            if answer == "camp":
                answer = input("\n" + "Camping out was a smart play, you set up camp, re-fuel and set out again when the sun came up. You continued your journey until you reached the end of the forest line, you are greeted by a group of travelers and they ask if you'd like to stay awile or continue on your way *Please type stay or continue*")
                if answer == "continue":
                    print("\n" + "You made it to your destination! You celebrate with a nice warm fire in your cabin and some delicious soup and wine. YOU WIN")

                elif answer == "stay":
                    print("\n" + "The travelers happen to be very poor and decide your golden necklace is worth more to them than your life, so they tie you to a near by tree and leave you for the beasts of the forest. YOU LOSE")

                else:
                    print("\n" + "It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")
                    

            elif answer == "walk":
                print("\n" + "You attempted to keep walking into the night and unfortunatly caught frostbite. YOU LOSE")

            else:
                print("\n" + "It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")

        elif answer == "run":
            print("\n" + "You attempt to run, but the bear manages to catch you on your escape and eats you for dinner. YOU LOSE")

        else:
            print("\n" + "It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")


    elif answer == "swim":
        print("\n" + "You attempted to swim across the water, but were vicously eaten by a mutant aligator. YOU LOSE")

    else:
        print("\n" + "It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")

elif answer == "left":
    answer = input("\n" + "You have come up to a large opening in the forest, would you like venture into it or attempt to go all the way aroud? *Please type enter forest or go around* ")
    if answer == "forest":
        print("\n" + "You started walking into the forest and were immediatly approached by a lost villager who hasn't eaten in weeks, looks like you are dinner! YOU LOSE")

    elif answer == "go around":
        answer = input("\n" + "You attempted to walk all the way around the forest, but on your way you ran into some travelers who offered to take you almost all the way to your destination, would you like to accept or decline their offer? *Please type accept or decline* ")
        if answer == "accept":
            answer = input("\n" + "They welcome you with open arms and help you put all your things in the cart. You just about make it to your drop off when a group of thieving knomes raid the group. Some members are tring to fight back while others are attempting to flee, will you fight or run? *Please type fight or run* ")
            if answer == "fight":
                answer = input("\n" + "You gather up all your strength and team up with the rest of the group defeating the raiders. They spared one of them leaving their fate up to you, will you let them leave or leave them to parish? *Please type live or die* ")
                if answer == "live":
                    answer = input("\n" "The rest of the group is grateful for your help and allowing them to take the last raider to be imprisoned and questioned, to show their appreciation they offer to take you the full way to your destination, will you go with them or walk? *Please type ride along or walk* ")
                    if answer == "ride along":
                        print("\n" "The group takes you right up to the gates and helps you with all of your things. You celebrate with a big pint infront of a nice cozy fire. YOU WIN")
                    elif answer == "walk":
                        print("\n" + "You enjoy the rest of your stroll in piece, finally arriving and celebrate with a much needed rest. YOU WIN")
                    else:
                        print("\n" + "It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")

                elif answer == "die":
                    print("\n" + "disappointed. YOU LOSE")

                else:
                    print("\n" + "It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")

            elif answer == "run":
                print("\n" + "You attempted to run, but the raiders catch up and decide to make an example of you. YOU LOSE")

            else:
                print("\n" + "It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")

        elif answer == "decline":
            print("\n" + "You decide to decline their generous offer and continue on your path, eventually you run out of food and are stuck in the middle of no where. YOU LOSE")

        else:
            print("\n" + "It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")

    else:
        print("\n" + "It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")
    

else:
    print("\n" + "It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")