"""
Sk PL Lexer
2023
"""

import re
class Lexer(object):
    def __init__(self , source:str):
        self.source = source
    def Tokenizer(self):
        """
        Identify A Word To Be A Token , Then Append it Into A List :
        `variable x : 3; Result = [ [VAR_DECLARATION, 'variable'] , ['IDENTIFIER' , x] . . . ] `\n
        Token List By Default Is An Empty Array
        """
        #Default
        Tokens = []
        #Strip The Code From New Line Breaks
        Source_Code = self.source.split()
        Source_Index = 0
        #Loop for Every Items
        while Source_Index < len(Source_Code):
            Word = Source_Code[Source_Index]
            #VARIABLE
            if Word == "variable": 
                Tokens.append(['VAR_DECLARATION' , Word])
            #IDENTIFIER
            elif re.match('[a-z]' , Word) or re.match('[A-Z]' , Word):
                if Word[len(Word) - 1 ] == ";":
                    Tokens.append(['IDENTIFIER' , Word[0:len(Word) - 1]])
                else:
                    Tokens.append(['IDENTIFIER' , Word])
            #INTEGER
            elif re.match('[0-9]' , Word):
                if Word[len(Word) - 1] == ";":
                    Tokens.append(['INTEGER' , Word[0:len(Word) - 1]])
                else:
                    Tokens.append(['INTEGER' , Word])
            #OPERATOR
            elif Word in ":/*=-+":
                Tokens.append(['OPERATOR' , Word])
            #END
            if Word[len(Word) - 1] == ";":
                Tokens.append(['STATEMENT_END' , ';'])
            #INCREMENT INDEX TO GO TO THE NEXT TOKEN
            Source_Index += 1
        return Tokens