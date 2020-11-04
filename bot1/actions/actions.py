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

class ActionProvideScope(Action):
    def name(self) -> Text:
        return "action_provide_scope"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        noStream = {'Music':"Here are some undergrad courses for music: \n Diploma in Music \n B.A. (Music) \n B.F.A (Music) \n B.P.A (Music) \n You can refer this link for more details: \n https://www.examsplanner.in/career-in-music/",
                    'Drawing': "Here are some undergrad courses for drawing: \n Diploma in Drawing \n B.A. (Drawing) \n B.F.A. (Drawing) \n You can refere this link for more details: \n https://www.sarvgyan.com/courses/drawing-painting"}

        stream = {'Science':"Here are some undergrad courses with Science: \n B.Sc. \n B.E. \n B.Tech \n M.B.B.S. \n B.Pharm \n B.H.M.S. \n For more details click on the link: \n https://www.sarvgyan.com/courses/science-courses",
                    'Arts':"Here are some undergrad courses with Arts: \n B.A.\n L.L.B. \n B.M.M \n B.F.D. \n For more details click on the link below: \n https://www.upgrad.com/blog/career-options-after-12th-arts/",
                    'Commerce': "Here are some undergrad courses with Commerce: \n B.Comm. \n B.M.S. \n B.B.A \n B.Economics \n For more details click on the link below: \n https://www.collegedekho.com/articles/career-options-after-12th-commerce-courses-and-eligibility/"}

        if tracker.get_slot("nostream") == None:
            dispatcher.utter_message(text=str(stream[tracker.get_slot("stream").capitalize()]))
        else:
            dispatcher.utter_message(text=str(noStream[tracker.get_slot("nostream").capitalize()]))

        return []
