from hanspell import spell_checker
input = "안녕 하세요오오오오엉"
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

for i in result.checked:
    output_list.append(i)

print(output_list[i])