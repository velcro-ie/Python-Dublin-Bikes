# got help for creating the json string from
# http://www.tutorialspoint.com/json/json_python_example.htm
# http://stackoverflow.com/questions/23255512/creating-nested-json-structure-with-multiple-key-values-in-python-from-json

import sqlite3 as lite
import json
#import sys


def GetData(Day, TimeSlot):
    ''' Get the data for the given time and day and return it in json format
    
    Fetch the data for the relevant date and time from the database.  The values returned are an 
    average of the values for the given time + a half hour.'''
    ###########################
    #    Declare Variables    #
    ###########################
    con = lite.connect('bikes.db')
    date_time = getDate(Day)    #get the date of our data
    NumberList = []             #List to hold the stand numbers
    Data_String = []            #json string for return

    # format the to and from date fields.
    fromDateTime = date_time + TimeSlot + ":00"
    toDateTime = date_time +GetEndTime(TimeSlot)      
    
    with con:
        NumberList = con.execute("SELECT number, lat, longit, stands, AVG(av_bikes), address FROM json WHERE  time between '" + fromDateTime + "' and '" + toDateTime +"' GROUP BY number;")   #get the list of station numbers
            
        for Entry in NumberList:
            #Entry[0] = station number
            #Entry[1] = Latitude
            #Entry[2] = Longitude
            #Entry[3] = Stands in the Station
            #Entry[4] = Average of bikes in the station for the given time
            #Entry[5] = address
            
            #set the colour of the pins.
            percentage = 100 * float(Entry[4])/float(Entry[3])
            if percentage == 0:
                colour = "red"
            elif percentage < 33:
                colour = "yellow"
            elif percentage < 66:
                colour = "orange"
            else:
                colour = "green"
            
            #build the json string
            Data_String.append({'lat':Entry[1],
                                'lon': Entry[2],
                                'color': colour,
                                'address': Entry[5]})
            
    json_data = json.dumps(Data_String)
    con.close()
    return json_data

def getDate(Day):
    '''set the date to the date in our database'''
    if Day == "Monday":
        date_time = "2016-03-07 "
    elif Day == "Tuesday":
        date_time = "2016-03-08 "
    elif Day == "Wednesday":
        date_time = "2016-03-09 "
    elif Day == "Thursday":
        date_time = "2016-03-10 "
    elif Day == "Friday":
        date_time = "2016-03-11 "
    elif Day == "Saturday":
        date_time = "2016-03-05 "
    elif Day == "Sunday":
        date_time = "2016-03-06 "
    else:
        return "Not a valid day."  
    return date_time

def GetEndTime(TimeSlot):
    '''Calculate the end time for the search'''
    TimeBits =  TimeSlot.split(":")
    if TimeBits[1] == "30":
        # add an hour
        TimeBits[0] = str(int(TimeBits[0]) +1)
        if len(TimeBits[0]) == 1:
            TimeBits[0] = "0" + TimeBits[0]
        returnTime = TimeBits[0] + ":00:00"
    else:
        #add a half hour
        returnTime = TimeBits[0] + ":30:00"
    return returnTime

