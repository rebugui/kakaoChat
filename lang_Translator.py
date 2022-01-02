# -*- coding: utf-8 -*-
from googletrans import Translator

def lang_Translator(input_text):
    translator = Translator()

    if translator.detect(input_text).lang == 'kr':
        result = translator.translate(text1, src='kr', dest='en')    
    else:
        result = translator.translate(text1, src='en', dest='kr')
        
    return result
