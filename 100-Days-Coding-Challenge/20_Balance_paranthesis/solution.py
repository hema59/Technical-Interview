class solution:
    def __init__(self, s ):
        self.string = s
        self.size = len(s)
        self.open = ['[','{','(']
        self.close = [']','}',')']

    def is_balanced(self):
        if len(self.string) %2 != 0:
            return False
        stack = list(self.string)
        tstack = []
        while len(stack) >0 :
            t = stack.pop()
            if t in self.close:
                tstack.append(t)
            else:
                peek = tstack.pop()
                if t == '[' and peek != ']' : return False 
                if t == '{' and peek != '}' : return False 
                if t == '(' and peek != ')' : return False
        return True

    def format_paranthesis( self):
        if self.size == 0 : return ""
        if self.is_balanced() ==  True:
            return self.string

        formatted_string = []
        stack = list(self.string)
        t_stack = []
        while len(stack) > 0 :
            t = stack.pop(0)
            if t in self.open:
                formatted_string.append(t)
                t_stack.append(t)
            else:
                if t_stack == []:
                    continue
                peek = t_stack.pop()
                print("".join(formatted_string)," ,temp: ",t_stack," ,peek (0) -" ,peek)
                if peek == '[' : formatted_string.append(']')
                if peek == '{' : formatted_string.append('}')
                if peek == '(' : formatted_string.append(')')
        
        return "".join(formatted_string)

test_cases = { '1' : "(){{}}[{())}]",
                '2' : "",
                '3' :"[{()}]",
                '4' : "[[((({[(][)]})))]]]",
                '5' :"]"}
answers = { '1' : "(){{}}[{(())}]",
                '2' :"",
                '3' :"[{()}]",
                '4' :"[[((({ [()][()] })))]]]",
                '5' :'[]'}

for key in test_cases.keys():
    sol = solution(test_cases[key])
    if sol.format_paranthesis() == answers[key]:
        print("{} PASSED".format(key))
    else:
        print("{} FAILED".format(key))