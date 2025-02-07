from modules import *


try:
    print(sum(1,u))

except IndentationError:
    print("Indentation error only enter the number")
except NameError:
    print("name is not defined only enter the number")  
except SyntaxError:
    print("Syntax error only enter the number")    

except Exception as e:
    print("Error: ",e)

else:
    print("No error")   
finally:
    print("This is finally block")  