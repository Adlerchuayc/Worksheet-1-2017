number = input("Please type in an integer or a float: ")
sig_fig = input("How many significant figures would you like? ")

def conv_a_str(a):
    b = ""
    for x in range(len(a)):
        b = b + str(a[x])
    return b

def positive_integer():
    a = []
    for i in range(len(number)):
        a.append(number[i])
    print(a)
    print(len(a))
    
    if len(a) == int(sig_fig):
        final_answer = number
    elif len(a) < int(sig_fig):
        a.append(".")
        while len(a) - 1 != int(sig_fig):
            a.append("0")
        final_answer = conv_a_str(a)
    else:
        b = 1
        while len(a) > int(sig_fig):
            if int(a[len(a) - 1]) < 5:
                a = a[:len(a) - 1]
            else:
                try:
                    while int(a[len(a) - b]) > 4:
                        b += 1
                    else:
                        c = str(int(a[len(a) - b]) + 1)
                        a = a[:len(a) - b]
                        a.append(c)
                except IndexError:
                    temp = a
                    a = ["1"]
                    a.append(temp)
                    break
                    #doesn't work properly
        while len(a) < len(number):
            a.append("0")
        final_answer = conv_a_str(a)

    print_value = "The value " + number + " rounded to " + sig_fig + " significant figures is: " + final_answer
    print(print_value)

def negative_integer():
    abs_number = str(abs(int(number)))
    a = []
    for i in range(len(abs_number)):
        a.append(abs_number[i])
    print(a)
    print(len(a))
    
    if len(a) == int(sig_fig):
        final_answer = abs_number
    elif len(a) < int(sig_fig):
        a.append(".")
        while len(a) - 1 != int(sig_fig):
            a.append("0")
        final_answer = conv_a_str(a)
    else:
        b = 1
        while len(a) > int(sig_fig):
            if int(a[len(a) - 1]) < 5:
                a = a[:len(a) - 1]
            else:
                try:
                    while int(a[len(a) - b]) > 4:
                        b += 1
                    else:
                        c = str(int(a[len(a) - b]) + 1)
                        a = a[:len(a) - b]
                        a.append(c)
                except IndexError:
                    temp = a
                    a = ["1"]
                    a.append(temp)
                    break
                    #doesn't work properly
        while len(a) < len(abs_number):
            a.append("0")
        final_answer = conv_a_str(a)

    print_value = "The value " + number + " rounded to " + sig_fig + " significant figures is: " + "-" + final_answer
    print(print_value)

def positive_float():
    nodec_number = number.replace(".", "")
    a = []
    for i in range(len(nodec_number)):
        a.append(nodec_number[i])
    print(a)
    print(len(a))

    if len(nodec_number) > int(sig_fig):
        dividend = len(nodec_number) - int(sig_fig)
    else:
        dividend = int(sig_fig) - len(nodec_number) + 1

    if len(a) == int(sig_fig):
        final_answer = number
    elif len(a) < int(sig_fig):
        while len(a) - 1 != int(sig_fig):
            a.append("0")
        final_answer = conv_a_str(a)
    else:
        b = 1
        while len(a) > int(sig_fig):
            if int(a[len(a) - 1]) < 5:
                a = a[:len(a) - 1]
            else:
                try:
                    while int(a[len(a) - b]) > 4:
                        b += 1
                    else:
                        c = str(int(a[len(a) - b]) + 1)
                        a = a[:len(a) - b]
                        a.append(c)
                except IndexError:
                    temp = a
                    a = ["1"]
                    a.append(temp)
                    break
                    #doesn't work properly
        while len(a) < len(nodec_number):
            a.append("0")
        final_answer = str(float(conv_a_str(a)) / float(10 ** dividend))

    print_value = "The value " + number + " rounded to " + sig_fig + " significant figures is: " + final_answer
    print(print_value)

    
    
#Function call
if "." not in number:
    if "-" not in number:
        positive_integer()
    else:
        negative_integer()
else:
    if "-" not in number:
        positive_float()
    else:
        negative_float()

