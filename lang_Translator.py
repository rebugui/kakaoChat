# -*- coding: utf-8 -*-
from googletrans import Translator

def lang_Translator():

    input_text = "�ѱ�� �Է��ϸ� ����� ���ɴϴ�."
    translator = Translator()
    
    lang = translator.detect(input_text).lang

    if lang == 'kr':
        result = translator.translate(text1, src=lang, dest='en')    
    else:
        result = translator.translate(text1, src=lang, dest='kr')
    
    print(output_text)
#    return output_text
