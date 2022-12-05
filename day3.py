print("Welcome to treasure island")
print("Your mission is to find the treasure")
cross_road = input("You're at a cross road. Where do you wanna go. type 'Left' or 'rIght'? ")
if cross_road == "Left" or cross_road == "left":
    print("You come to a lake. There is an island in the middle of the lake")
    cross = input('Type wait "wait" to wait for a boat. Type "swim" to swim accross')
    if cross == "wait":
        print("You arrrived at the island unharmed")
        color = input("There is a house with three doors. One red, one yellow and one blue. Which color do you choose? ")
        if color == "red":
            print("It is a room full of fire. You diee")
        elif color == "yellow":
            print("You found the treasure! You win")
        elif color == "blue":
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over")