from sympy import init_printing, sympify, solve
init_printing()


errors = ['SINTAX ERROR', 'EXPRESSION ERROR']


def interpret(filename: str):
    data = dict()
    data["exps"] = {}
    data["sols"] = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            s = line.split()
            if s != []:
                if s[0] == 'exps': 
                    if s[2][0] == '{' and s[-1][-1] == '}':
                        string = line[line.find('{')+1: line.find('}')]
                        string1 = string.split(', ')
                        exec(f'data["exps"]["{s[1]}"]= []')
                        for el in string1: exec(f'data["exps"]["{s[1]}"].append({el})')     
                    else: print(errors[0])  
                else:
                    if s[0] == 'solve':
                        if s[1][0] == '{' and s[-1][-1] == '}':
                            keys = ''.join(s[1:])
                            keys = keys.replace('{', '')
                            keys = keys.replace('}', '')
                            keys = keys.split(',')
                            for key in data["exps"].keys():
                                data["sols"][key] = {}
                                for k in keys:
                                    if key == k: 
                                        for el in data["exps"][key]:
                                            try:
                                                exp = sympify(el)
                                                roots = solve(exp)
                                                data["sols"][key][el] = roots
                                            except Exception as e: 
                                                print(e)
                        else: print(errors[0]) 
                    elif s[0] == 'out': 
                        if s[2][0] == '{' and s[-1][-1] == '}':
                            
                            keys = ''.join(s[2:])
                            keys = keys.replace('{', '')
                            keys = keys.replace('}', '')
                            keys = keys.split(',')

                            if s[1] == 'sols':
                                key = s[1]
                                print('EXPPRESSION | EXPRESSION | ROOTS\n   NAME')
                                for k in keys: 
                                    for e in data[key][k].keys(): print(f'{k} | {e} | ({str(data[key][k][e])[1:-1]})')
                                print('--------------------------------')
                            elif s[1] == 'exps':
                                key = s[1]
                                print('EXPRESSION | EXPRESSIONS\n   NAME')
                                for k in keys: print(f'{k} | {", ".join(data[key][k])}')
                                print('--------------------------------')
                            else: print(errors[0])
                        else: print(errors[0])
                    elif s == []: pass
                    else: print(errors[0])

interpret('IvaPet\\1.math')