from hanspell import spell_checker
 
input = u‘안녕 하세요. 저는 한국인 입니다.’
 
input_convert = input.replace(‘.’,‘.#’).split(‘#’)
 
input_list =  [“”]
 
for i in input_convert:
    print(i)
    if len(input_list[–1]) + len(i) < 500:
        input_list[–1] += i
    else:
        input_list.append(i)  
 
result = spell_checker.check(input_list)
 
print(result[0].result)
 
# true