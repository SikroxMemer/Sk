"""
### Sk Programming Lanuage Lexer \n
2023 Made By Mohamed Lafrouh
"""

from Tokens import *
from Functions import *
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

            Format_Word = Word[0:len(Word) - 1]
            if Word == "variable": 
                Tokens.append(['VAR_DECLARATION' , Word])
            elif re.match('TRUE' , Word) or re.match('FALSE' , Word):
                if Word[len(Word) - 1] == ";":
                    Tokens.append(['BOOLEAN' , Format_Word])
                else:
                    Tokens.append(['BOOLEAN' , Word])
                    
            #IDENTIFIER

            elif re.match(IDENTIFIER , Word) or re.match(SECOND_IDENTIFIER , Word):
                if Word[len(Word) - 1 ] == ";":
                    Tokens.append(['IDENTIFIER' , Format_Word])
                else:
                    Tokens.append(['IDENTIFIER' , Word])

            #INTEGER

            elif re.match(INTEGER , Word):
                if Word[len(Word) - 1] == ";":
                    Tokens.append(['INTEGER' , Format_Word])
                else:
                    Tokens.append(['INTEGER' , Word])
            #STRING

            elif re.match(STRING, Word):
                if Word[len(Word) - 1] == ";":
                    Tokens.append(['STRING' , Format_Word])
                else:

                    Tokens.append(['STRING' , Word])

            #COMMENT

            if  re.match(COMMENT , Word):
                Tokens.append(['COMMENT' , Word])
            #OPERATOR

            elif Word in OPERATOR:
                Tokens.append(['OPERATOR' , Word])

            #FUNCTION:

            elif re.match(FUNCTION , Word):
                Tokens.append(['FUNCTION' , Word])

            #SHOW

            elif re.match(BULTIN_SHOW , Word):
                if Word[len(Word) - 1] == ";":
                    Tokens.append(['BULTIN_SHOW' , Format_Word])
                else:
                    Tokens.append(['BULTIN_SHOW' , Word])

            #ADD
            elif re.match(BULTIN_ADD , Word):
                if Word[len(Word) - 1] == ";":
                    Tokens.append(['BULTIN_ADD' , Format_Word])
                else:
                    Tokens.append(['BULTIN_ADD' , Word])
            
            #REMOVE
            elif re.match(BULTIN_REMOVE , Word):
                if Word[len(Word) - 1] == ";":
                    Tokens.append(['BULTIN_REMOVE' , Format_Word])
                else:
                    Tokens.append(['BULTIN_REMOVE' , Word])

            #STATE
            elif re.match(BULTIN_STATE , Word):
                if Word[len(Word) - 1] == ";":
                    Tokens.append(['BULTIN_STATE' , Format_Word])
                else:
                    Tokens.append(['BULTIN_STATE' , Word])
            
            #CREATE
            elif re.match(BULTIN_CREATE , Word):
                if Word[len(Word) - 1] == ";":
                    Tokens.append(['BULTIN_CREATE' , Format_Word])
                else:
                    Tokens.append(['BULTIN_CREATE' , Word])

            #PATTERS:
            elif Word == LEFT_PATERN:
                Tokens.append(['L_PATTERN' , Word])

            elif Word == RIGHT_PATERN:
                Tokens.append(['R_PATTERN' , Word])
            #END
            if Word[len(Word) - 1] == END:
                Tokens.append(['STATEMENT_END' , ';'])

            #INCREMENT INDEX TO GO TO THE NEXT TOKEN
            Source_Index += 1

        return Tokens