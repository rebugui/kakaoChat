# -*- coding: utf-8 -*-
from hanspell import spell_checker

def KrCheck(input):
    input_convert = input.replace('.','.#').split('#')
    input_list,output_text =  [""],[""]
    running_time = 0
    errors_count = 0

    for i in input_convert:
        if len(input_list[-1]) + len(i) < 500:
            input_list[-1] += i
        else:
            input_list.append(i)
    
    output_text = spell_checker.check(input_list)
    for output_text in output_text:
        errors_count = errors_count + int(output_text.errors)
        running_time = running_time + int(output_text.time)
        output_text.append(output_text.checked)
    

    output_text = ''.join(output_text)

    return output_text,errors_count,running_time
