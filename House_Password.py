input_data = ('1Aa1Aa1Aa')
password = True
condition_A_Z = 0
condition_a_z = 0
condition_0_9 = 0
if 64 >= len(input_data) >= 10:
    for i in range(len(input_data)):
        if input_data[i].isalpha():
            if input_data[i].isupper():
                password = True
                condition_A_Z += 1
                continue
            elif input_data[i].islower():
                password = True
                condition_a_z += 1
                continue
        elif input_data[i].isalnum():
            password = True
            condition_0_9 += 1
            continue
        else:
            password = False
            break
else:
    password = False
if (password == True) and (condition_A_Z >= 1) and (condition_a_z >= 1) and (condition_0_9 >= 1):
    password = True
else:
    password = False
print(password)