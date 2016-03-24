from adapt.intent import IntentBuilder
from input_engine import input_engine

class navigation_engine:
    def __init__(self, input_engine):
        self.input_engine = input_engine

        navigation_keywords = [
            "go",
            "walk",
            "run"
        ]
        self.input_engine.register_entity(navigation_keywords, "NavigationKeyword")

        navigation_direction = [
            "north",
            "east",
            "south",
            "west",
            "up",
            "down",
            "left",
            "right",
            "straight",
            "back"
        ]
        self.input_engine.register_entity(navigation_direction, "NavigationDirection")

        navigation_object = [
            "wall",
            "street",
            "person",
            "enemy"
        ]
        self.input_engine.register_entity(navigation_object, "NavigationObject")

        navigation_intent = IntentBuilder("NavigationIntent")\
            .require("NavigationKeyword")\
            .require("NavigationDirection")\
            .optionally("NavigationObject")\
            .build()

        self.input_engine.register_intent(navigation_intent)

    def to_string(self, intent):
        """Parses an intent to a string"""
        string = intent.get("NavigationKeyword") + "ing " + intent.get("NavigationDirection") + "."
        if not intent.get("NavigationObject") == None:
            string += " Dealing with " + intent.get("NavigationObject")
        return string
