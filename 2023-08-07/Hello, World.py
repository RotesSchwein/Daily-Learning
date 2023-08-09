print('"' + 'Hello, World!' + '"' + '\n' + '- Brian Kerningham (1978)')

variable = 10
print(variable)
# This is a comment. The machine ignores it
x = 5
y = 0.5
expression = x + y
print(expression)

multiline = """
    To Mr.President,
        정치를 대국적으로 하시오!        
"""

stringVariable = "MR.Roh"
intVariable = 523

print(f"This -> {intVariable} is a integer variable")
print(f"This -> {stringVariable} is a string variable")

def only_str(v: str):
    return print(v)

only_str("Mt.Fuji")
only_str(5896)

import torch

print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0))