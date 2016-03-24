from input_engine import input_engine
from navigation import navigation_engine

if __name__ == "__main__":
    input_engine = input_engine()
    navigation_engine = navigation_engine(input_engine)
    while True:
        string = input("What do you want to do?\n")
        intent = input_engine.get_intent(string)
        if not intent == None:
            print(navigation_engine.to_string(intent))
