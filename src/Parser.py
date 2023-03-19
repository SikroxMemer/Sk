from Variable import ToPython

"""
### Sk Programming Language Parser
2023 Made By Mohamed Lafrouh
"""

class Parser(object):
    def __init__(self , tokens):
        self.tokens = tokens
        self.token_index = 0
        self.transpiled_code = ""

    def Parse(self):
        while self.token_index < len(self.tokens):
            token_type = self.tokens[self.token_index][0]
            token_value = self.tokens[self.token_index][1]
            
            if token_type == "VAR_DECLARATION" and token_value == "variable":
                self.Parse_Variable_Declaration(self.tokens[self.token_index:len(self.tokens)])

            self.token_index = self.token_index + 1
        return(self.transpiled_code)

    def Parse_Variable_Declaration(self , token_stream):
        tokens_checked = 0
        name           = ""
        operator       = ""
        value          = ""
        function       = ""
        l_pattern      = ""
        value2         = ""
        r_pattern      = ""


        for token in range(0 , len(token_stream)):
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]
            if token_type == "STATEMENT_END":
                break
            elif token == 1 and token_type == "IDENTIFIER":
                name = token_value
            elif token == 1 and token_type != "IDENTIFIER":
                print(f"ERROR : Invalid Variable {token_value}")
                quit()
            elif token == 2 and token_type == "OPERATOR":
                operator = token_value
            elif token == 2 and token_type != "OPERATOR":
                print(f"ERROR : Can't Assingne The Value {token_value}")
                quit()
            elif token == 3 and token_type in ['STRING' , 'INTEGER' , 'IDENTIFIER' , 'BOOLEAN']:
                value = token_value
            elif token == 3 and token_type not in ['STRING' , 'INTEGER' , 'IDENTIFIER' , 'BOOLEAN']:
                print(f"ERROR : Variable Value Is Not Correct : {token_value}")
                quit()

            elif token == 4 and token_type in ['BULTIN_SHOW' , 'BULTIN_ADD' , 'BULTIN_REMOVE' , 'BULTIN_STATE' , 'BULTIN_CREATE']:
                function = token_value
            elif token == 5 and token_type == ['LEFT_PATERN']:
                l_pattern = token_value
            elif token == 6 and token_type in ['INTEGER' , 'IDENTIFIER']:
                value2 = token_value
            elif token_value == 7 and token_type == ['RIGHT_PATERN']:
                r_pattern = token_value

            tokens_checked += 1

        varObj = ToPython()
        
        self.transpiled_code += varObj.transpile(name=name,operator=operator,value=value,l_pattern=l_pattern,r_pattern=r_pattern,function=function,value2=value2)
        
        self.token_index += tokens_checked