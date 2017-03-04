number = input("Please type in an integer or a float: ")
sig_fig = input("How many significant figures would you like? ")

# 0 is taken to be positive


def positive_integer():
    final_answer = ""
    a = number
    if len(a) == int(sig_fig):
        final_answer = number
    else:
        if len(a) < int(sig_fig):
            a = a + "."
            while len(a) - 1 != int(sig_fig):
                a = a + "0"
                final_answer = a
        else:
            b = 1
            while len(a) > int(sig_fig):
                if int(a[len(a) - 1]) < 5:
                    a = a[:len(a) - 1]
                    final_answer = a
                else:
                    while int(a[len(a) - b]) > 4:
                        b += 1
                    else:
                        c = str(int(a[len(a) - b]) + 1)
                        a = a[:len(a) - b] + c
                        final_answer = a
            while len(a) < len(number):
                a = a + "0"
                final_answer = a
    print_value = "The value " + number + " rounded to " + sig_fig + " significant figures is: " + final_answer
    print(print_value)
    
    
def negative_integer():
    final_answer = ""
    a = str(abs(int(number)))
    if len(a) == int(sig_fig):
        final_answer = number
    else:
        if len(a) < int(sig_fig):
            a = a + "."
            while len(a) - 1 != int(sig_fig):
                a = a + "0"
                final_answer = a
        else:
            b = 1
            while len(a) > int(sig_fig):
                if int(a[len(a) - 1]) < 5:
                    a = a[:len(a) - 1]
                    final_answer = a
                else:
                    while int(a[len(a) - b]) > 4:
                        b += 1
                    else:
                        c = str(int(a[len(a) - b]) + 1)
                        a = a[:len(a) - b] + c
                        final_answer = a
            while len(a) < len(number) - 1:
                a = a + "0"
                final_answer = a
    print_value = "The value " + number + " rounded to " + sig_fig + " significant figures is: " + "-" + final_answer
    print(print_value)


def positive_float():
    final_answer = ""
    a = number
    if len(a) - 1 == int(sig_fig):
        final_answer = number
    else:
        if len(a) - 1 < int(sig_fig):
            while len(a) - 1 != int(sig_fig):
                a = a + "0"
                final_answer = a
        else:
            a = a.replace(".", "")
            b = 1 + 1
            while len(a) > int(sig_fig):
                if int(a[len(a) - 1]) < 5:
                    a = a[:len(a) - 1]
                    final_answer = a
                else:
                    while int(a[len(a) - b]) > 4:
                        b += 1
                    else:
                        c = str(int(a[len(a) - b]) + 1)
                        a = a[:len(a) - b] + c
                        final_answer = a
            while len(a) < len(number) - 1:
                a = a + "0"
                final_answer = a
            final_answer = str(float(final_answer) / (10 ** float(sig_fig)))
    print_value = "The value " + number + " rounded to " + sig_fig + " significant figures is: " + final_answer
    print(print_value)


def negative_float():
    final_answer = ""
    a = str(abs(float(number)))
    if len(a) - 1 == int(sig_fig):
        final_answer = number
    else:
        if len(a) - 1 < int(sig_fig):
            while len(a) - 1 != int(sig_fig):
                a = a + "0"
                final_answer = a
        else:
            a = a.replace(".", "")
            b = 1 + 1
            while len(a) > int(sig_fig):
                if int(a[len(a) - 1]) < 5:
                    a = a[:len(a) - 1]
                    final_answer = a
                else:
                    while int(a[len(a) - b]) > 4:
                        b += 1
                    else:
                        c = str(int(a[len(a) - b]) + 1)
                        a = a[:len(a) - b] + c
                        final_answer = a
            while len(a) < len(number) - 1:
                a = a + "0"
                final_answer = a
            final_answer = str(float(final_answer) / (10 ** float(sig_fig)))
    print_value = "The value " + number + " rounded to " + sig_fig + " significant figures is: " + "-" + final_answer
    print(print_value)

    
##floats are messed up

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








##
##
###positive integers
##if "." not in number:
##    
##    sig_fig = input("How many significant figures would you like?     ")
##    
##
##    if (len(number) == int(sig_fig)):
##        final_answer = number
##
##    elif (len(number) < int(sig_fig)):
##        final_answer = number + str(".")
##        if (len(number) == int(sig_fig)):
##            done = False
##        while True:
##            final_answer = final_answer + str(0)
##        print(final_answer)
##
##    else:
##        a = number
##        b = []
##        for i in range(int(sig_fig)):
##            b.append(a[i])
##        final_answer = str(b)
##
##    print_value = "The value " + number + " rounded to " + sig_fig + " significant figures is: " + final_answer
## 
##    print(print_value)
##    ## rounding up and down? fix the print and the float ones too
