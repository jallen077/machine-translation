"""This is the translator file that
translates from English to French of English to German"""

# Make sure the appropriate libraries are installed
# pip3 install pandas
# pip3 install ibm_watson

# import the language translator from IBM watson
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize

APIKEY_LT = 'Kskj1fkMImGgrz6yKRqs5nKaEwM66xc2M-JR9Og_nUym'
URL_LT = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/666072d2-3b1a-4286-9a6f-8207468989a9'

VERSION_LT='2018-05-01'

TEXT_TO_TRANSLATE = "This is a test."

# Create the language translator object
authenticator = IAMAuthenticator(APIKEY_LT)
language_translator = LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
language_translator.set_service_url(URL_LT)
#language_translator

# get a list of the languages that the service can identify, currently outputs the list


json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

"""
# use the method translate, this will translate the text
# this case is english to spanish en-es
# for english to french use en-fr
# for english to german use en-de
translation_response = language_translator.translate(\
    text=TEXT_TO_TRANSLATE, model_id='en-es')
translation_response

# the result is a dictionary
translation=translation_response.get_result()
print(translation)
print("^^^ This is the result as a Python Dictionary")

# get the actual translation as a string as follows
spanish_translation =translation['translations'][0]['translation']
print(spanish_translation)
print("^^^This is the result as a string")

# can translate back to english as follows
translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

# and get the actual string
translation_eng=translation_new['translations'][0]['translation']
print(translation_eng)
print("^^^ And this is translated back into English")
"""

def english_to_french(text_input):
    """
    This function translates from english to french
    """
    # use the method translate, this will translate the text
    translation_response = language_translator.translate(\
        text=text_input, model_id='en-fr')

    # the result is a dictionary
    translation=translation_response.get_result()

    # get the actual translation as a string as follows
    french_translation =translation['translations'][0]['translation']

    return french_translation

english_to_french(TEXT_TO_TRANSLATE)


def english_to_german(text_input):
    """
    this function translates english to german
    """
        # use the method translate, this will translate the text
    translation_response = language_translator.translate(\
        text=text_input, model_id='en-ga')

    # the result is a dictionary
    translation=translation_response.get_result()

    # get the actual translation as a string as follows
    german_translation =translation['translations'][0]['translation']

    return german_translation

english_to_german(TEXT_TO_TRANSLATE)
