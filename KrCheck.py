# -*- coding: utf-8 -*-

from hanspell import spell_checker

def krcheck(input)
    input_convert = input.replace('.','.#').split('#')
    input_list =  [""]
    
    for i in input_convert:
        print(i)
        if len(input_list[-1]) + len(i) < 500:
            input_list[-1] += i
        else:
            input_list.append(i)
    
    result = spell_checker.check(input_list)

    return input_convert,result

def main():
    input = u'의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.'
    input_convert,result = krcheck(input)
    print(input_convert) 
    print(result) 


if __name__ == "__main__":
	main()