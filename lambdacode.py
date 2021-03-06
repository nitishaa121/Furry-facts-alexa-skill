from __future__ import print_function
import random

breedfactdict = {
    "Pomeranian": "despite their small size, pomeranians descended from large sled dogs " \
                  "and used to weigh over twenty pounds compared to their current weight around seven pounds. ",
    "poodle": "poodles hesitate to go out when it's raining not because they're scared of " \
              "rain but because they have very good hearing and are sensitive to the sound of rainfall. ",
    "pug": "in 2009, a pug name chester ludlow got his mba degree from rochville online " \
           "university. ",
    "Siberian husky": "a husky's howl can be heard upto ten miles or sixteen kilometers away. ",
    "Doberman": "the first dobermann was bred by a tax collector that felt he needed " \
                 "protection in the shadier parts of his town. ",
    "golden retriever": "american presidents ford and raegan both had a golden retriever " \
                        "as a pet while in office. ",
    "great Dane": "When great danes are born they weigh about one or two pounds but can grow " \
                  "to one hundred pounds in just six months. ",
    "chihuahua": "like human babies, chihuahuas are born with molera, a soft spot on their skull. " \
                 "unlike human babies, chihuahuas may have the spot for their whole life. ",
    "chow chow": "chow chows are known for their distinctive purplish tongues and lips. " \
                 "next time you see a chow chow, sneak a peek in its mouth!",
    
}


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_responseCard(title, cardOutput, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': cardOutput
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome to Furry Facts"
    speech_output = "Welcome to Furry Facts. " \
                    "You can learn about different canine breeds, " \
                    "including Pugs, Poodles and many more " \
                    " by saying Alexa tell me about pugs for example"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Some popular breeds to learn about are the " \
                    "Siberian Husky, Chihuahua, or Chow Chows. Please " \
                    " choose a breed to learn about. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def getBreedFact(intent, session):
    session_attributes = {}
    breed = ""
    if 'Breed' in intent['slots']:
        if 'value' in intent['slots']['Breed']:
            breed = intent['slots']['Breed']['value']
            print(breed)
            try:
                value = breedfactdict[breed]
                card_title = "Fact for " + breed
                card_output = "Did you know that " + str(value) + " "
                speech_output = "Did you know that " + str(value) + \
                            " Cool, right? You can ask about another breed if you would like "
            # If the user either does not reply to the welcome message or says something
            # that is not understood, they will be prompted again with this text.
                reprompt_text = "Some popular breeds to learn about are the " \
                            "Siberian Husky, Chihuahua, or Chow Chows. Please " \
                            " choose a breed to learn about. "
                should_end_session = False
                return build_response(session_attributes, build_speechlet_responseCard(
                card_title, card_output, speech_output, reprompt_text, should_end_session))
            except:
                card_title = "Oops, we dont know this Breed"
                speech_output = "Oops, sorry. We dont know about this breed yet. You can learn about different " \
                        "canine breeds, including Pugs, Poodles and many more"
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
                reprompt_text = "Some popular breeds to learn about are the " \
                        "Siberian Husky, Chihuahua, or Chow Chows. Please " \
                        " choose a breed to learn about. "
                should_end_session = False
                return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))
        else:
            card_title = "Please Select a Breed"
            speech_output = "You can learn about different canine breeds, " \
                            "including Pugs, Poodles and many more " \
                            " by saying Alexa tell me about pugs for example. "
            # If the user either does not reply to the welcome message or says something
            # that is not understood, they will be prompted again with this text.
            reprompt_text = "Some popular breeds to learn about are the " \
                            "Siberian Husky, Chihuahua, or Chow Chows. Please " \
                            " choose a breed to learn about. "
            should_end_session = False
            return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text,should_end_session))
    else:
        card_title = "Please Select a Breed"
        speech_output = "Please tell me the name of your chosen breed. You can learn about different " \
                        "canine breeds, including Pugs, Poodles and many more"
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = "Some popular breeds to learn about are the " \
                        "Siberian Husky, Chihuahua, or Chow Chows. Please " \
                        " choose a breed to learn about. "
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "See you soon! "
    speech_output = "Thank you for using Furry Facts. " \
                    "Have a great day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "MyBreedIsIntent":
        return getBreedFact(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

