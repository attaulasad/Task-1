# tests/test_translator.py

import unittest
from language_translation_tool.translator import translate_text
from language_translation_tool.exceptions import InvalidLanguageError

class TestTranslator(unittest.TestCase):
    
    def test_translation(self):
        # Mocking the API response could be done here
        translated_text = translate_text("Hello", "en", "es")
        self.assertEqual(translated_text, "Hola")  # Assuming the translation is correct
    
    def test_invalid_language_code(self):
        with self.assertRaises(InvalidLanguageError):
            translate_text("Hello", "", "es")

if __name__ == "__main__":
    unittest.main()
