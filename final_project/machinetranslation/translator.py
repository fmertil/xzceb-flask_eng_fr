 #!/usr/bin/env python
"""Module providingFunction printing python version."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

def translator_instance(apikeys, urls):
    """ instance of the IBM Watson Language translator """
    global language_translator
    authenticator = IAMAuthenticator(apikeys)
    language_translator = LanguageTranslatorV3(
        version = '2018-05-01',
        authenticator = authenticator)
    language_translator.set_service_url(urls)
    return language_translator


def englishToFrench(englishText):
    """ Translate from English to French """
    translation = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText


def frenchToEnglish(frenchText):
    """ Translate from French to English """
    translation = language_translator.translate(text = frenchText, model_id='fr-en').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

apikey = os.environ['apikey']
url = os.environ['url']
language_translator = translator_instance(apikey, url)