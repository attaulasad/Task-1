# language_translation_tool/translator.py

import requests
from .config import Config
from .exceptions import InvalidLanguageError, APIError
from .logger import setup_logger

logger = setup_logger()

def translate_text(text, source_language, target_language):
    if not source_language or not target_language:
        logger.error("Invalid language code provided")
        raise InvalidLanguageError("Source or target language code is missing or invalid")
    
    params = {
        'q': text,
        'source': source_language,
        'target': target_language,
        'key': Config.API_KEY
    }
    
    try:
        logger.info(f"Sending translation request: {text} from {source_language} to {target_language}")
        response = requests.get(Config.TRANSLATE_URL, params=params)
        response.raise_for_status()
        translation = response.json()['data']['translations'][0]['translatedText']
        logger.info(f"Translation successful: {translation}")
        return translation
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        raise APIError(f"An error occurred with the API request: {e}")
