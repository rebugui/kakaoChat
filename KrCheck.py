# -*- coding: utf-8 -*-

from hanspell import spell_checker
input = "안녕하세여 양우혁임미다."
input_convert = input.replace('.','.#').split('#')

input_list =  [""]
output_list = [""]

for i in input_convert:
    print(i)
    if len(input_list[-1]) + len(i) < 500:
        input_list[-1] += i
    else:
        input_list.append(i)

result = spell_checker.check(input_list)

print(result.checked)