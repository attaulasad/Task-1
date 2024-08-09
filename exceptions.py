# language_translation_tool/exceptions.py

class TranslationError(Exception):
    """Custom exception for translation errors"""
    pass

class InvalidLanguageError(TranslationError):
    """Raised when an invalid language code is provided"""
    pass

class APIError(TranslationError):
    """Raised when there's an error with the API request"""
    pass
