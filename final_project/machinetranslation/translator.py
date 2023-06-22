"""Function to translate between EN/FR"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """English to French"""
    return MyMemoryTranslator('en','fr').translate(english_text)

def french_to_english(french_text):
    """French to English"""
    return MyMemoryTranslator('fr','en').translate(french_text)
