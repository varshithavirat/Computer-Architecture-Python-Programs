#!/usr/bin/env python
# coding: utf-8

# In[1]:


def to_binary(number):
    return format(number & 0xFF, '08b')


def signed_value(binary):
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value


def perform_operation(a, b, operator):
    if operator == "+":
        result = a + b
        binary_result = int(to_binary(a), 2) + int(to_binary(b), 2)
        overflow = (a >= 0 and b >= 0 and result > 127) or \
                   (a < 0 and b < 0 and result < -128)
    else:
        result = a - b
        binary_result = int(to_binary(a), 2) + int(to_binary(-b), 2)
        overflow = (a >= 0 and b < 0 and result > 127) or \
                   (a < 0 and b >= 0 and result < -128)

    print(f"\nExpression: ({a}) {operator} ({b})")
    print("First operand :", to_binary(a))
    print("Second operand:", to_binary(b))
    print("Result in decimal:", result)
    print("Result in binary :", to_binary(result))
    print("Arithmetic overflow:", "Yes" if overflow else "No")


perform_operation(45, 19, "+")
perform_operation(-35, -12, "-")



# In[ ]:




