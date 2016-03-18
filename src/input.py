from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine

class navigation_engine:
    def __init__(self):
        self.engine = IntentDeterminationEngine()
        navigation_keywords = [
            "go",
            "walk",
            "run"
        ]
        for nk in navigation_keywords:
            self.engine.register_entity(nk, "NavigationKeyword")

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
        for nd in navigation_direction:
            self.engine.register_entity(nd, "NavigationDirection")

        navigation_object = [
            "wall",
            "street",
            "person",
            "enemy"
        ]
        for no in navigation_object:
            self.engine.register_entity(no, "NavigationObject")

        navigation_intent = IntentBuilder("NavigationIntent")\
            .require("NavigationKeyword")\
            .require("NavigationDirection")\
            .optionally("NavigationObject")\
            .build()

        self.engine.register_intent_parser(navigation_intent)

    def get_intent(self, input_string):
        intent = self.engine.determine_intent(input_string)
        for intent in self.engine.determine_intent(input_string):
            if intent.get("confidence") > 0 and intent.get("intent_type") == "NavigationIntent":
                return intent
        return None
