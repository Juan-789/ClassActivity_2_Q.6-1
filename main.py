"""
6. A car can cover a distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? Write a program that asks the user for  N the kilometers traveled per day and M the number of kilometers route. Calculate the number of days it will take to travel the route.

"""
nkms_travelled = int(input("How many kilometers do you travel in a day? "))
mNumberKmsOfRoute = int(input('How many Kilometers is the route? '))
numOfdays = mNumberKmsOfRoute // nkms_travelled
if mNumberKmsOfRoute % nkms_travelled != 0:
  numOfdays+=1 
print (f"it will take {numOfdays} days to travel!")