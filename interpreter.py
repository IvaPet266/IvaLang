import os


# data = ['fluc']

def interpret(filename: str):
    with open(filename, 'r') as f:
        for line in f.readlines():
            s = line.split()
            if s != []:
                if s[0] == 'flucs': 
                    if s[1][0] == '{' and s[-1][-1] == '}':
                        string = line[line.find('{')+1: line.find('}')]
                        data = dict()
                        string1 = string.split(', ')
                        string2 = list()
                        for i in range(len(string1)): string2.append(string1[i].split(': '))
                        for el in string2:
                            exec(f'data["{el[0]}"] = {el[1]}')       
                    print(3)
                else:
                    if s[0] != 'del' and s[0].find('.add') == -1:
                        exec(f'data["{s[0]}"] {" ".join(s[1:])}')
                        print(1)
                    elif s[0].find('.add') != -1:
                        exec(f'data["{s[0][:s[0].find(".add")]}"].append({s[0][s[0].find(".add")+5:]}')
                        print(2)
                    elif s[0] == 'del':
                        for x in s[1:]:
                            exec(f'del data["{x.replace(",", "")}"]')
                print(data)
         

interpret('IvaPet\y.iva')