#Adventure Game
#Name Input / Start

name = input("Quick, Doc! They are waking up! Hey there adventurer, it looks like you took a pretty rough tumble down that hill, my name is Bailey, what's yours? ")

answer = input("\n" + "Well " + name + " I know you have to get to it, the Doc fixed you right up and the road is just that way, good luck! " + "*You get up and start walking on the path and come to a cross road, would you like to go left or right?* ")

if answer == "right":
    answer = input("\n" + "You come upon a large river with a very flimsy bridge connecting each side, would you like to cross the bridge or swim through the river? *Please type bridge or swim*")

elif answer == "left":


#else:
    #print("It seems you are very clumsy and take a pretty hard tumble, you are sent back to the beginning")