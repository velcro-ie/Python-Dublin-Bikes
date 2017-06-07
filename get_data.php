<?php

    $servername = "localhost";
    $username = "root";
    $password = "Pctdaya18!";
    $dbname = "project";

    //connect to mysql db
    $conn = mysqli_connect($servername, $username, $password, $dbname) or die("Could not connect");

    //connect to the project database
    mysqli_select_db($conn, $dbname);

    //download the json data from jcdecaux
    file_put_contents("json_file", fopen("https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=a9b774842c905dfd63c581f714f3c6a211425993", 'r'));

    //read the json file contents
    $jsondata = file_get_contents('json_file');

    //convert json object to php associative array
    $data = json_decode($jsondata, true);

    for($x = 0; $x < sizeof($data); $x++) {
        $number = $data[$x]['number'];
        $name = mysqli_real_escape_string($conn, $data[$x]["name"]);
        $address = mysqli_real_escape_string($conn, $data[$x]['address']);
        $lat = $data[$x]['position']['lat'];
        $longit = $data[$x]['position']['lng'];
        $banking = $data[$x]['banking'];
        $bonus = $data[$x]['bonus'];
        $status = $data[$x]['status'];
        $con_name = $data[$x]['contract_name'];
        $stands = $data[$x]['bike_stands'];
        $av_stands = $data[$x]['available_bike_stands'];
        $av_bikes = $data[$x]['available_bikes'];
        $updated = $data[$x]['last_update'];
        $date = date('Y-m-d H:i:s');

        //insert into mysql table
        $sql = "INSERT INTO json(number, name, address, lat, longit, banking, bonus, status, con_name, stands, av_stands, av_bikes, updated, time)
        VALUES('$number', '$name', '$address', '$lat', '$longit', '$banking', '$bonus', '$status', '$con_name', '$stands', '$av_stands', '$av_bikes', '$updated', '$date')";

        if(!mysqli_query($conn, $sql))
        {
                die('Query Error : ' . mysqli_error($conn));
        }
    }
?>




