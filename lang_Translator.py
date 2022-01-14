# -*- coding: utf-8 -*-
from _typeshed import OpenTextModeUpdating
from googletrans import Translator

def lang_Translator(input_text):

    translator = Translator()    
    lang = translator.detect(input_text).lang

    if lang == 'kr':
        output_text = translator.translate(input_text, src=lang, dest='en')    
    else:
        output_text = translator.translate(input_text, src=lang, dest='kr')
    
    print(output_text)
    return output_text
