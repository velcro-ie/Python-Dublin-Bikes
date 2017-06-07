## Description
---------------
Dublin Bikes v1.0 allows users to view available bicycles at any Dublin city bike station at any day and time.

This is a project carried out in UCD as part of module COMP30670 as part of the course work leading
to a M.Sc in Computer Science. The project has been supervised by Dr. Aonghus Lawlor.


## Dependencies
---------------
Python 3.4 or higher
Sqlite 3.11.1
Flask 0.10.1


## Downloading
--------------
The Dublin Bikes project can be downloaded from the public git repository:
git@git.ucd.ie:veldies/dublinbikes.git

The database file 'dump.sql' is required to run the application. The file is publicly available and may be downloaded
at the link below and should be placed in the static directory of the user's local git repository for this project.
 
https://drive.google.com/file/d/0B8mqe-7ZzOvsb1drcXZQLVZHMEU/view?usp=sharing


## Gathering Data
-----------------
We created a php script(get_data.php) to run on an Amazon Web Server running Ubuntu Server.
We configured a cron job to run the script every 5 minutes.

The script retrieved the data from the Dublin Bikes API in JSON format.
The JSON data was then read into a mysql database consisting of one table using the following schema:

json_id int(11)
number int(11)
name varchar(75)
address varchar(75)
lat decimal(9,6)
longit decimal(9,6)
banking tinyint(1)
bonus tinyint(1)
status varchar(25)
con_name varchar(75)
stands int(11)
av_stands int(11)
av_bikes int(11)
updated bigint(20)
time datetime

We added the additional field 'datetime' to capture the exact time of our data capture as Dublin Bikes 
API data may be delayed by several minutes.

For production and testing we chose to use SQlite because of its small footprint, 
its ability to handle large datasets easily (we gathered 250,000 rows of data) and its use
of the SQL language. We perfomed a SQL dump from our mySQL database. However, we met with 
compatibility issues when trying to import our dump file into SQlite and we had to format
our dump file before importing it into SQlite. 


## Running the Application
---------------------------
To start the application run the main.py file. Note that line 17 of main.py contains a path reference to the local copy of
dump.sql. Users should ensure that they insert the correct path to their local copy of this file. Running main.py starts
the Flask web server application. We start Flask in debug mode ("app.run(debug=True)") to view any errors which may arise
and after a few moments we receive a message to our browser console that our web server is up and running. 
(See gallery image "startup.png" in the documents submitted with the project).

Dublin Bikes data is contained in our local file dump.sql. We need to create a database containing this data 
in order to execute our queries later. Our first function call creates a database 'bikes.db' in sqlite on our
local machine. We use error checking to check that the creation of the database runs smoothly.

The user then proceeds to the site's homepage. In our case, using Flask, we browse to http://127.0.0.1:5000 
(gallery image "homepage.png").


## Functionality
----------------
The homepage allows the user to view data on the availability of bicycles at each of Dublin City Council's free 
bike stands. Information is presented on a map of the city using colour-coded markers. Different colour markers 
indicate different levels of bicycle availability and a legend is presented on the left of the page to help the
user understand the colour scheme.

The user selects a day and time from the selection bars on the left. Time selection is divided into half-hour intervals. 
When the use hits "Go", the map is populated with availability markers for each bike station (gallery image "markers.png").
Hovering over a marker shows the name of the street for that bike station. As an added feature, the map shows bicycle 
lanes accross the city to allow the user to plan their journey safely. In addition, the user benefits from all the usual
features of Google maps including zoom and street view (gallery image "street_view.png").

Here we remind users that data presented to users is not real data time. Data is historical and is based on the data 
collected from Dublin Bikes from 4th to 10th March 2016. The data presented for a particular day and time to the user 
is represented as typical data for that day and time.

## Database Queries
-------------------

When the user selects a date and time on the homepage, the day and time are submitted to our running Flask application. 
The application calls the function GetData() with the date and time values. GetData() submits a query to our database 
'bikes.db' and the query returns values for the latitude, longitude, address, available bikes and number of bike stands 
of each bike station. 

From the last two pieces of data we calculate the percentage availability of bicycles. Based on 
the percentage availability of bikes, we assign a colour value from red (indicating low availability, i.e less than 33%) to
green (high availability, greater than 66%). 

Note that the values returned are an average of the values for the selected time plus a half hour. 
We could just as well have chosen to get data for the half hour before the selected time or for 15 minutes either side of 
the selected time.

Having obtained the data we need, the values for latitude, longitude, colour and address for each station are added to a JSON 
file (to facilitate javascript processing later) and returned to main.py.

## Testing
---------------
We carried out testing of our database queries using a dedicated test file testing.py. We did this by testing the function GetData() in 
accessDB.py with multiple day and time inputs and checked that the database query was successful in returning output as a json string.

## Data Representation
----------------------
With the data safely obtained in JSON format our Flask application then renders a new browser template 'markers.html'. Our 
new markup contains a javascript onload event which creates a Google map of Dublin. The event also calls a javascript function
markers() to populate the map with coloured markers based on the data in our JSON file. In addition, the map is layered with bicycle 
lane data for the city obtained using Google map layers. A check of our browser console shows that all pages have loaded successfully 
without any significant errors (gallery image "console 200_OK.png").


## Design and Theme
------------------------

For our homepage we implemented a colour scheme and theme favoured by Dublin City Council on their Dublin Bikes website 
(http://www.dublinbikes.ie/). Logos and fonts also closely mirror the parent website to create an overall impression of unity 
between the two websites. 


## Contacts
  --------

     o If you want to contact the developers about Dublin Bikes v1.0
       or have any questions about any of the above features please 
       send an email to any of the developers:
       <andrew.sweeney.1@ucdconnect.ie>
       <velda.conaty@ucdconnect.ie>
       <donovanJblaine@gmail.com>


## License
-----------
Dublin Bikes v1.0 is free software; you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation; either version 3 of the License, or (at your option) any later
version.

Dublin Bikes v1.0 is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE.  See the GNU General Public License for more details.