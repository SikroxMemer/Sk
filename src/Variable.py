"""
Sk Programming Language Convertor \n
2023 Made By Mohamed Lafrouh
"""

from Functions import *

class ToPython(object):
    def __init__(self):
        self.exec_string = ""
    def transpile(
                self , 
                name:str , 
                operator:str , 
                value:str , 
                function:str , 
                l_pattern:str , 
                value2:str , 
                r_pattern:str
            ):

        match operator:
            case ":":
                operator = "="

        match value:
            case 'TRUE':
                value = 'True'
            case 'FALSE':
                value = 'False'
            case _:
                value = value
        pass
    
        match value2:
            case 'TRUE':
                name = 'True'
            case 'FALSE':
                name = 'False'
            case _:
                value2 = value2
        
            
        #CONVER_ADD_TO_+
        if function == '!ADD':
            function = '+'
            l_pattern  , r_pattern= '' , ''
            return name+" "+operator+" "+ value+" "+ function+l_pattern+ ' ' + value2 + r_pattern+"\n"
        
        #CONVERT_REMOVE_TO_-
        elif function == '!REMOVE':
            function = '-'
            l_pattern  , r_pattern= '' , ''
            return name+" "+operator+" "+ value+" "+ function+l_pattern+ ' ' + value2 + r_pattern+"\n"
        
        #CONVERT_CREATE_TO_OPEN('FILE' , 'X')
        elif function == '!CREATE':
            function = f"\nopen({name} , 'x')"
            l_pattern  , r_pattern= '' , ''
            self.exec_string += name+" "+operator+" "+ value+" "+ function+l_pattern+ ' ' + r_pattern+ "\n"
            return self.exec_string
        #CONVERT_SHOW_TO_PRINT
        elif function == '!SHOW':
            return name+" "+operator+" "+ value+" "+ '\n' +'print('+value2+')'+"\n"
        else:
            self.exec_string += name+" "+operator+" "+ value+" "+ function+l_pattern+' ' +value2 +r_pattern+"\n"
        return self.exec_string
    