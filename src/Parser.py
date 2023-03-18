from Variable import ToPython

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
            elif token == 3 and token_type in ['STRING' , 'INTEGER' , 'IDENTIFIER']:
                value = token_value
            elif token == 3 and token_type not in ['STRING' , 'INTEGER' , 'IDENTIFIER']:
                print(f"ERROR : Variable Value Is Not Correct : {token_value}")
                quit()
            tokens_checked += 1
        varObj = ToPython()
        self.transpiled_code += varObj.transpile(name=name,operator=operator,value=value)
        self.token_index += tokens_checked