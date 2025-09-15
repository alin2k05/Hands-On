import time

clock=time.strftime('%H:%M:%S')
print(clock)


hour=int(time.strftime('%H'))
#print(hour)


if (5<=hour<12):
    print("good morning")

elif (12<=hour<18):
    print("good afternoon")

else:
    print("good night")