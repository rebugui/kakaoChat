# -*- coding: utf-8 -*-
from googletrans import Translator

#def lang_Translator():

input_text = "요건 한글이에영."
translator = Translator()

if translator.detect(input_text).lang == 'kr':
    output_text = translator.translate(input_text, src=translator.detect(input_text).lang, dest='en')    
else:
    output_text = translator.translate(input_text, src=translator.detect(input_text).lang, dest='kr')

print(output_text)
#    return output_text
