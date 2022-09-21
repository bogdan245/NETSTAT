var jsonObj = JSON.parse(jsonstr);
var locations = [];

// iterate through json and get items and keys
for ( key in jsonObj){
    var offline = 0;
    var count = Object.keys(jsonObj[key]).length;

    var temp = jsonObj[key];

    for (val in temp);
     {
        //count which of them are OFFLINE and increase count. This covers the case is you have multiple equipemnts in the same location.
        if(temp[val] == "FALSE")
        {
            offline++;
        }
        // check each case and change color of specific id
        if(offline == count) //all offline
        {
            var element1 = document.getElementById(key);
            element1.style.fill = '#f95959' //red
        }

        if(offline == 0) //all online
        {
            var element2 = document.getElementById(key);
            element2.style.fill = '#9fd3c7' //green
        }

        if(offline < count && offline > 0) //just some equipments are offline in the same location
        {
            var element3 = document.getElementById(key);
            element3.style.fill = '#ffc93c' // yellow
        }

        if(count == 0) //no equipment
        {
            var element4 = document.getElementById(key);
            element4.style.fill = '#e3e3e3' //grey
        }
     }
}