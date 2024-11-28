options=["start", "stop", "exit"]

state=input("What do you want to do?")
if state.lower() in options:
    while state != "exit":
        if state =="start":
            print("Car started... Ready to go")
            state=input("What do you want to do?")
        elif state =="stop":
            print("Car stopped...")
            state=input("What do you want to do?")
        else:
            print("Exiting...")
            break
else:
    print("I can't understand")