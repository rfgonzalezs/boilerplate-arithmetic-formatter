import re
def arithmetic_arranger(problems, Bool = None):
    control = True
    num = []
    cant_dig = []
    res_sum = []
    cont0 = 0
    cont1 = 2
    split_num = re.findall("[\d\w]{1,5}",str(problems))
    op = re.findall("[\+\-\*\/]",str(problems))
    for i in split_num:
        if len(op) >= 6: #Error Situation 1
            arranged_problems = "Error: Too many problems."
            control = False
            break
        for j in op: #Error Situation 2
            if j == '/':
                arranged_problems = "Error: Operator must be '+' or '-'."
                control = False
                break
        try:
            int(i)
        except: #Error Situation 3
            arranged_problems = "Error: Numbers must only contain digits."
            control = False
            break
        if (len(i) >= 5): #Error Situation 4
            arranged_problems = "Error: Numbers cannot be more than four digits."
            control = False
            break
        else:
            cant_dig.append(len(i))
            num.append(int(i))
    if control != False:
        for i in range(0,len(cant_dig),2):
            if i == 0:
                if cant_dig[i] == 1:
                    Row1 = ' '*(cant_dig[i+1]+1)+str(num[i])    
                    Row2 = '\n'+(op[cont0])+(' ')+str(num[i+1])
                    lin = str('-'*(cant_dig[i]+cant_dig[i+1]+1))
                else:

                    if cant_dig[i+1] == 1:
                        Row1 = (' '*(cant_dig[i]))+str(num[i])
                        Row2 = '\n'+(op[cont0])+(' '*(cant_dig[i]))+str(num[i+1])
                        lin = '-'*(cant_dig[i]+cant_dig[i+1]+1)
                    else:
                        Row1 = (' '*(cant_dig[i+1]))+str(num[i])
                        Row2 = '\n'+(op[cont0])+(' '*(cant_dig[i]-1))+str(num[i+1])
                        lin = '-'*(cant_dig[i]+cant_dig[i+1])                
            else:
                if cant_dig[i] == 1:
                    if cant_dig[i] < cant_dig[i+1]:
                        Row1 = Row1+(' '*9)+str(num[i])
                    else:
                        Row1 = Row1+(' '*6)+str(num[i])
                else:
                    if cant_dig[i] == 2:
                        Row1 = Row1+(' '*6)+str(num[i])
                    else:
                        Row1 = Row1+(' '*6)+str(num[i])
            if cant_dig[i] == 4:
                if cant_dig[i+1] == 1:
                    Row2 = Row2+(' '*4+op[cont0])+(' '*(cant_dig[i]))+str(num[i+1])
                    lin = lin+' '*4+str('-'*(cant_dig[i]+cant_dig[i+1]+1))                    
                if cant_dig[i] == cant_dig[i+1]:
                    Row2 = Row2+(' '*4+op[cont0])+(' '*1)+str(num[i+1])
                    lin = lin+' '*4+str('-'*(cant_dig[i]+2))
            if cant_dig[i] == cant_dig[i+1]:
                if cant_dig[i] == 1:
                    Row2 = Row2+(' '*4+op[cont0])+(' '*(cant_dig[i]))+str(num[i+1])
                    lin = lin+' '*4+str('-'*(cant_dig[i]+cant_dig[i+1]+1)) 
                if cant_dig[i] == 2:
                    Row2 = Row2+(' '*4+op[cont0])+(' '*(cant_dig[i]-1))+str(num[i+1])
                    lin = lin+' '*4+str('-'*(cant_dig[i]+cant_dig[i+1]))
            if cant_dig [i] < cant_dig[i+1]:
                if cant_dig[i+1] == 4:
                    Row2 = Row2+(' '*4+op[cont0])+(' '*(1))+str(num[i+1])
                    lin = lin+' '*4+str('-'*(cant_dig[i+1]+2))
            else:
                if cant_dig[i] == 3:
                    Row2 = Row2+(' '*4+op[cont0])+(' '*(cant_dig[i]-1))+str(num[i+1])
                    lin = lin+' '*4+str('-'*(cant_dig[i]+cant_dig[i+1]))                               
            cont0 += 1
        arranged_problems = Row1+Row2+'\n'+lin
    if (Bool == True):
        for i in range(0, len(op)):#addition or subtraction of the values arranged above
            if i == 0:
                if op[i] == '+':
                    res_sum.append(num[i]+num[i+1])
                else:
                    res_sum.append(num[i]-num[i+1])
                arranged_problems =arranged_problems+'\n'+' '*1+str(res_sum[i])#+'\t'
            else:
                if op[i] == '+':
                    res_sum.append(num[cont1]+num[cont1+1])
                else:
                    res_sum.append(num[cont1]-num[cont1+1])
                cont1 += 2 
                if res_sum[i] < 0:
                    arranged_problems = arranged_problems+' '*5+str(res_sum[i])#+'\t'
                else:
                    arranged_problems = arranged_problems+' '*6+str(res_sum[i])#+'\t'
    return arranged_problems#string of organized values

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])) 
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])) 
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)) 
#print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))    
#print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))    
#print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))

"""  11      3801      1      123         1
 \n+  4    - 2999    + 2    +  49    - 9380
 \n----    ------    ---    -----    ------"""