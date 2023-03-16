import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2023-03-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL)


def english_to_french(englishtext):
    """
    Translates English text to French.
    Args:
        englishtext (str): The English text to translate.
    Returns:
        str: The French translation of the input text.
    """
    if englishtext == '':
        return 'Invalid input'
    else:
        translation = language_translator.translate(
            text=englishtext,
            model_id='en-fr').get_result()
        french_text = translation['translations'][0]['translation']
        return french_text


def french_to_english(frenchtext):
    """
    Translates French text to English.
    Args:
        frenchtext (str): The French text to translate.
    Returns:
        str: The English translation of the input text.
    """
    if frenchtext == '':
        return 'Invalid input'
    else:
        translation = language_translator.translate(
            text=frenchtext,
            model_id='fr-en').get_result()
        english_text = translation['translations'][0]['translation']
        return english_text