from accessDB import GetData

#This code is to test our Accessdb.py file to ensure that it is returning a json string after parsing the db.

#       Call the function  

ent_day = input("Enter the day: ")
ent_time = input("Enter the time: ")
#ent_day = "Monday"
#ent_time = "21:00"
output = GetData(ent_day, ent_time)
print ("the output is: ", output)

#additionally we have incorporated try/catch statements in our main.py file to ensure our file is working.