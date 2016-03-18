import json
import sys

from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine

engine = IntentDeterminationEngine()
navigation_keywords = [
    "go",
    "walk",
    "run"
]

for nk in navigation_keywords:
    engine.register_entity(nk, "NavigationKeyword")

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
    engine.register_entity(nd, "NavigationDirection")

navigation_intent = IntentBuilder("NavigationIntent")\
    .require("NavigationKeyword")\
    .require("NavigationDirection")\
    .build()

engine.register_intent_parser(navigation_intent)

if __name__ == "__main__":
    while True:
        string = input("What do you want to do?\n")
        for intent in engine.determine_intent(string):
            if intent.get("confidence") > 0 and intent.get("intent_type") == "NavigationIntent":
                print(intent.get("NavigationKeyword"), "ing ", intent.get("NavigationDirection"), sep="")
