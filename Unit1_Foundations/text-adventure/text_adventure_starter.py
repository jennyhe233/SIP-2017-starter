start = '''
You are in your bedroom. You hear a scary noise. "

You can stay in your bed, or you can leave your room to investigate.
'''


print(start)

#First: STAY or LEAVE bedroom
print("Type 'Stay' to stay in your room,  'leave' to leave your room")
user_input = input()
if user_input == "stay":
    print("You decide to stay in the comfort of your bed. You wait a very long time, until you die...") # finished the story by writing what happens

elif user_input == "leave":
    print("You choose to leave your room, and you hear another noise. What do you do? Go back to your room, or investigate?  ...") # finished the story writing what happens

    #Second: GO BACK to room or INVESTIGATE noise
    print("Type 'Go back' to return to your room, 'investigate' to see what the noise was")
    user_input = input()
    if user_input == "go back":
        print("You decide to go back to your room. You wait a very long time, until you die...") # finished the story by writing what happens

    elif user_input == "investigate":
        print("You see a random man ! Do you go and hide in your room, or call him?  ...") # finished the story writing what happ

        #third: GO BACK to room or CALL out to the man
        print("Type 'Go back' to go to your room,  'call' to call out to the man")
        user_input = input()
        if user_input == "go back":
            print("You decide to go back to your room. You wait a very long time in your bed, until you die...") # finished the story by writing what happens

        elif user_input == "call":
            print("You call out to the man. Meanwhile, you think whether he is a good or bad guy?  ...") # finished the story writing what happens


            #four: GOOD or BAD guy ?
            print("Type 'good' if you think he is a good guy,  'bad' if you think he is a bad guy")
            user_input = input()
            if user_input == "good":
                print("You keep walking towards the man, getting closer, until the man kills you.") # finished the story by writing what happens

            elif user_input == "bad":
                print("You turn around and run out of your house. You either call for help, or run out to street...") # finished the story writing what happens

                #five
                print("Type 'help' to call for help, 'run' to silentlyrun out into the street")
                user_input = input()
                if user_input == "help":
                    print("You call out for help but nobody hears you. But the man hears you. He finds and kills you. THE END") # finished the story by writing what happens

                elif user_input == "run":
                    print("You run out into the street, making minimal noise. On your left, there is a car approaching. On your right, you see a man. ...") # finished the story writing what happens
                    #six
                    print("Type 'left' to go to the car, 'right' to go to the man. ")
                    user_input = input()
                    if user_input == "right":
                        print("You come cloose to the person. It turns out it is the man trying to kill you. So he kills you. You die." )
                    elif user_input == "left":
                        print("You get in the car, then you safe. Good Ending." )
