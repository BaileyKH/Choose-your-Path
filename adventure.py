#Adventure Game
#Name Input / Start

name = input("Quick, Doc! They are waking up! Hey there adventurer, it looks like you took a pretty rough tumble down that hill, my name is Bailey, what's yours? ")

answer = input("\n" + "Well " + name + " I know you have to get to it, the Doc fixed you right up and the road is just that way, good luck! " + "*You get up and start walking on the path and come to a cross road, would you like to go left or right?* ")

if answer == "right":
    answer = input("\n" + "You come upon a large river with a very flimsy bridge connecting each side, would you like to cross the bridge or swim through the river? *Please type bridge or swim*")
    if answer == "bridge":
        answer = input("You made it across the bridge! Oh no! You have been greeted by a giant mutant bear! Would you like to try and fight the bear or run away? *Please type fight or run* ")
        if answer == "fight":
            answer = input("You manage to fight off the bear giving you the opportunity to escape! You've run into deep into the forest, would you like to set up camp or keep walking? *Please type camp or walk* ")
            if answer == "camp":
                answer = input("Camping out was a smart play, you set up camp, re-fuel and set out again when the sun came up. You continued your journey until you reached the end of the forest line, you are greeted by a group of travelers and they ask if you'd like to stay awile or continue on your way *Please type stay or coninue*")
                if answer == "continue":
                    print("You made it to your destination! You celebrate with a nice warm fire in your cambin and some delicious soup and wine. YOU WIN")

                elif answer == "stay":
                    print("The travelers happen to be very poor and decide your golden necklace is worth more to them than your life, so they tie you to a near by tree and leave you for the beasts of the forest. YOU LOSE")

                else:
                    print("It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")
                    

            elif answer == "walk":
                print("You attempted to keep walking into the night and unfortunatly caught frostbite. YOU LOSE")

            else:
                print("It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")

        elif answer == "run":
            print("You attempt to run, but the bear manages to catch you on your escape and eats you for dinner. YOU LOSE")

        else:
            print("It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")


    elif answer == "swim":
        print("You attempted to swim across the water, but were vicously eaten by a mutant aligator. YOU LOSE")

    else:
        print("It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")

elif answer == "left":
    answer = input("\n" + "You have come up to a large opening to the forest, would you like venture into it or attempt to go all the way aroud? *Please type enter forest or go around")


else:
    print("It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")