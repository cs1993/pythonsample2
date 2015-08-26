__author__ = 'chandrashekhar'

string_input=raw_input("enter the list of string: ")
input_list=string_input.split()
max=input_list[0]
for i in range(1,len(input_list)):
    if len(max)<len(input_list[i]):
        max=input_list[i]
print max,len(max)