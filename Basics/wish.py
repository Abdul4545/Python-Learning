import time;

timestamp = time.strftime("%H:%M:%S")
print(timestamp)


hour = int(time.strftime('%H'))
if(hour > 4 and hour < 12) :
    print("Good Morning")
    
elif (hour >= 12 and hour <= 20):
    print("Good Evening")
    
else :
    print("Good Night")
    