from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R       
    return round(speed) 

test = ["We then generate text which is randomly produced but has the same distribution of letter groups as the input text. The result depends greatly on the source text ...",
        "My name is Shreyas Pachpute.", "Welcome to Shree Ram Laboratory."]
test1 = r.choices(test)
print("***** Typing Speed *****")
print(test1)
print()
print()
time1 = time()
testInput = input("Enter: ")
time2 = time()

print("Speed: ", speed_time(time1, time2, testInput), "w/sec")
print("Error: ", mistake(test1, testInput))