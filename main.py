# main.py

import argparse
from language_translation_tool.translator import translate_text
from language_translation_tool.exceptions import TranslationError

def main():
    parser = argparse.ArgumentParser(description="Language Translation Tool")
    parser.add_argument("text", type=str, help="The text to be translated")
    parser.add_argument("source_language", type=str, help="The source language code (e.g., 'en' for English)")
    parser.add_argument("target_language", type=str, help="The target language code (e.g., 'es' for Spanish)")
    
    args = parser.parse_args()
    
    try:
        translated_text = translate_text(args.text, args.source_language, args.target_language)
        print(f"Translated text: {translated_text}")
    except TranslationError as e:
        print(f"An error occurred during translation: {e}")

if __name__ == "__main__":
    main()
