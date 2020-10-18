// from data.js
var tableData = data;

// select tbody 
tbody = d3.select("tbody")
// console.log("something")

// loop through table using poject entries
function displayData(something) {
    tbody.text("")
    something.forEach(function (sighting) {
        new_tr = tbody.append("tr")
        Object.entries(sighting).forEach(function ([key, value]) {
            new_td = new_tr.append("td").text(value)
        })
    })
}

displayData(tableData)
// console.log("something")


// Select the button
var submit = d3.select("#submit");

submit.on("click", function () {
    console.log("something")

    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Select the input element and get the raw HTML node
    var dateInput = d3.select("#datetime");
    var cityInput = d3.select("#city");
    var stateInput = d3.select("#state");
    var countryInput = d3.select("#country");
    var shapeInput = d3.select("#shape");

    // Get the value property of the input element
    console.log(dateInput.property("value"));
    console.log(cityInput.property("value"));
    console.log(stateInput.property("value"));
    console.log(countryInput.property("value"));
    console.log(shapeInput.property("value"));

    //Make a filter and display filtered data
    var filtered = tableData.filter(sighting => {
        return (sighting.datetime === dateInput.property("value") || !dateInput.property("value")) &&
            (sighting.city === cityInput.property("value") || !cityInput.property("value")) &&
            (sighting.state === stateInput.property("value") || !stateInput.property("value")) &&
            (sighting.country === countryInput.property("value") || !countryInput.property("value")) &&
            (sighting.shape === shapeInput.property("value") || !shapeInput.property("value"))
    })

    displayData(filtered);
});

var filterInputs = d3.selectAll('.form-control');

// Make a function to clears fields and object
function clear() {
    filters = {};

    // Sets every input field to empty
    filterInputs._groups[0].forEach(entry => {
        if (entry.value != 0) {
            d3.select('#' + entry.id).node().value = "";
        }
    });
};

var clearall = d3.select("#clear");

// Clear upon click clears fields
clearall.on('click', function () {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Clears input fields
    clear()
});