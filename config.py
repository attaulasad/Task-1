# language_translation_tool/config.py

import os

class Config:
    API_KEY = os.getenv("GOOGLE_CLOUD_API_KEY", "your-default-api-key")
    TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2"
