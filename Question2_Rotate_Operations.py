#!/usr/bin/env python
# coding: utf-8

# In[3]:


def rotate_left(number, positions):
    print("\nROTATE LEFT WITHOUT CARRY (ROL)")
    print("Original number:", format(number, '08b'))

    for i in range(positions):
        msb = (number >> 7) & 1
        number = ((number << 1) & 0xFF) | msb
        print(f"After rotation {i + 1}: {format(number, '08b')}")

    print("Final result:", format(number, '08b'))


def rotate_left_carry(number, positions, carry):
    print("\nROTATE LEFT THROUGH CARRY (RCL)")
    print("Original number:", format(number, '08b'))
    print("Initial carry:", carry)

    for i in range(positions):
        old_msb = (number >> 7) & 1
        number = ((number << 1) & 0xFF) | carry
        carry = old_msb

        print(
            f"After rotation {i + 1}: "
            f"{format(number, '08b')}, Carry = {carry}"
        )

    print("Final result:", format(number, '08b'))
    print("Final carry:", carry)


binary_number = int('10110110', 2)

rotate_left(binary_number, 2)
rotate_left_carry(binary_number, 2, 0)


# In[ ]:




