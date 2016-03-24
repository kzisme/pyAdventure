from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine

class input_engine:
    """Manages the intent engine and natural language input parser"""
    def __init__(self):
        self.engine = IntentDeterminationEngine()

    def register_entity(self, keywords, name):
        """Registers an intenty to be found in an input"""
        for k in keywords:
            self.engine.register_entity(k, name)

    def register_intent(self, intent):
        """Registers an intent that can be found in an input"""
        self.engine.register_intent_parser(intent)

    def get_intent(self, input_string):
        """Returns an intent from an input string if one is found"""
        intent = self.engine.determine_intent(input_string)
        for intent in self.engine.determine_intent(input_string):
            if intent.get("confidence") > 0:
                return intent
        return None
