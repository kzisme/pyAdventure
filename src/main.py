from input import navigation_engine

if __name__ == "__main__":
    input_engine = input_engine()
    while True:
        string = input("What do you want to do?\n")
        intent = navigation_engine.get_intent(string)
        if not intent == None:
            print(intent.get("NavigationKeyword"), "ing ", intent.get("NavigationDirection"), sep="")
            if not intent.get("NavigationObject") == None:
                print("Dealing with", intent.get("NavigationObject"))
