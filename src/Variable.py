class ToPython(object):
    def __init__(self):
        self.exec_string = ""
    def transpile(self , name , operator , value):
        if operator == ":":
            operator = "="
        self.exec_string += name + " " + operator + " " + value + "\n"
        return self.exec_string