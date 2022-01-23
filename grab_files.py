import os

directory  = "clips"      
stack = []

for i in os.listdir(directory):
    stack.append(os.path.abspath(i))
    
print(stack)
