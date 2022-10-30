#types of variables ==>local variable,global variable
#local variables
"""
local variables are the variables which are define inside the class
its scope within the function itself
you cannot access outside the function
even parameters are local variable
"""
#global variable
"""
are the variables which are define outside the function
Its scope throughout the python class
"""


rno=90              #global variable
def info():
    name = "Bava"   #local variable
    global address
    address = "chennai"
    print(f"Hi{rno},{name},{address}")
    return name
data = info() #object creation
print(data)
print("Rno: ",rno)
print("Address: ",address)

