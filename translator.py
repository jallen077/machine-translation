# pull in the information from the API training section

#import the language translator from IBM watson
from ibm_watson import LanguageTranslatorV3

apikey_lt = 'Kskj1fkMImGgrz6yKRqs5nKaEwM66xc2M-JR9Og_nUym'
url_lt = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/666072d2-3b1a-4286-9a6f-8207468989a9' 

version_lt='2018-05-01'


# Create the language translator object
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
#language_translator

# get a list of the languages that the service can identify, currently outputs the list
from pandas import json_normalize

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")


# use the method translate, this will translate the text
# this case is english to spanish en-es
# for english to french use en-fr
# for english to german use en-de
translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
translation_response

# the result is a dictionary
translation=translation_response.get_result()
translation

# get the actual translation as a string as follows
spanish_translation =translation['translations'][0]['translation']
spanish_translation 

# can translate back to english as follows
translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

# and get teh actual string
translation_eng=translation_new['translations'][0]['translation']
translation_eng


def english_to_french(text_input):
    """
    This function translates from english to french
    """
    return 

def english_to_german(text_input):
    """
    this function translates english to german
    """
    return