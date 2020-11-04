# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from packages.scrape_college import CollegeScrape
#
class ActionProvideGuidance(Action):

    def name(self) -> Text:
        return "action_provide_guidance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        obj = CollegeScrape(tracker.get_slot('stream'),tracker.get_slot('location'),
                            tracker.get_slot('grades'))
        
        response = obj.fetch_list_on_guidance()
        dispatcher.utter_message(text=str(response))

        return []

