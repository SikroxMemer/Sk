# Salty-Kore
<p align="center">
  <img src="./src/secret/1.png" style="height: 100px; width:100px;">
</p>

**Salty-Kore : Static Programming Language with python interpreter as a base executer but uses both a lexer and parser to devide tokens and assign them into different     roles**

>SYNTAX: 
```
variable name_of_variable : value Function ( value );
example :
variable x : 500 !SHOW ( x );
```
You must have spaces between words like ```!SHOW ( x );``` also
in strings use underscore _ to seperate between words ```"Hello_World"```

I didn't include too much but am preatty happy with it.

>PREDEFINED FUNCTIONS:
``` 
!SHOW
!ADD
!REMOVE
!CREATE
```

To execute , run file ```Run.py``` and enter the name of the file , ```Run.py``` will execute a file called ```Executer.py```
and it will create another python file called ```Output.py``` wich contains a python code .<br>
```file.sk``` is converted to python
<br><br>
**Note : if ```Output.py``` Exists , ```Executer.py``` Will re-write the file again.**<br>
If you want to understand more you can see here https://accu.org/journals/overload/26/145/balaam_2510/
Its a documentation about lexer and parser
>
