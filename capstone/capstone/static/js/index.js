import bulmaCalendar from '../../../mybulma/node_modules/bulma-calendar/'

// Initialize all input of type date
var calendars = bulmaCalendar.attach('[type="date"]', { startDate: new Date('10/24/2019') });

// Loop on each calendar initialized
for (var i = 0; i < calendars.length; i++) {
    // Add listener to date:selected event
    calendars[i].on('select', date => {
        console.log(date);
    });
}

// To access to bulmaCalendar instance of an element
var element = document.querySelector('#my-element');
if (element) {
    // bulmaCalendar instance is available as element.bulmaCalendar
    element.bulmaCalendar.on('select', function (datepicker) {
        console.log(datepicker.data.value());
    });
}