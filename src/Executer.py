from Lexer import Lexer
from Parser import Parser

def Main():
    """
    function : Main() , Takes No Parametre \n
    Its The Core Of The Sk Language It Contains \n
    Two Objects : (Lexer , Parser) ; 
    """
    FileName = input("Enter Your File Name (Note : It Must End With .sk) :")
    if FileName.endswith('.sk'):
        import os
        #File Opening:
        Content = ""
        with open(FileName , 'r') as file:
            Content = file.read()
        #Initializer:
        L = Lexer(Content)
        tokens = L.Tokenizer()
        P = Parser(tokens)
        print(P.Parse())
        with open('Output.py' , 'w') as Output:
            Output.write(P.Parse())
        os.system('py Output.py')
#START:
Main()