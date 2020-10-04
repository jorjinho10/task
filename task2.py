# reverse input integer value, 12345->54321

def task_2(number):
    for i in range(10): #count power of 10 of input number
        z = number - (10**i)
        f = number/(10**i)
        l = i
        if z<=0:
            break

    c = number
    v = number
    rev_val = 0
    # rest_part = number
    for i in range(l):
        c = v
        v = c%(10**(l-i-1))
        m = c//(10**(l-i-1))
        rev_val = rev_val + m*(10**i)
        # rest_part = rest_part-m*(10**(l-i-1))
    
    print('Input value    = ',int(number))
    print('Reversed value = ',int(rev_val))   
        

    
print('Please set integer value and press Enter')

input_value = input()
input_value = int(input_value)
task_2(input_value)
