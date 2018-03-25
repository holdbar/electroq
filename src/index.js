import $ from 'jquery';
import 'fullcalendar';

$(document).ready(function(){

    $(".page2, .calendar-show, .page3").hide();
    $(".next").click(function(){
        $(".page1").hide();
        $(".page2, .calendar-show").show();
    });

    $(".back").click(function () {
        $(".page2, .calendar-show, .page3").hide();
        $(".page1").show();
    });

    $(".save").click(function () {
        $(".page2, .calendar-show").hide();
        $(".page3").show();
    });



});


/*fullCalendarAPI CONTENT*/
$(function() {

    // page is now ready, initialize the calendar...
    var calendarView = $('#calendar');

    $('#my-today-button').click(function() {
        $('#calendar').fullCalendar('today');
    });

    calendarView.fullCalendar({
        // put your options and callbacks here
        themeSystem: "bootstrap4",
        themeName: "Flatly",
        defaultView: "month",
        header: { // buttons for switching between views
            left: 'prevYear, prev,next, nextYear today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay',
        },
        buttonIcons: {
            prev: 'left-single-arrow',
            next: 'right-single-arrow',
            prevYear: 'left-double-arrow',
            nextYear: 'right-double-arrow'
        },
        themeButtonIcons: {
            prev: 'circle-triangle-w',
            next: 'circle-triangle-e',
            prevYear: 'seek-prev',
            nextYear: 'seek-next'
        },
        bootstrapGlyphicons: {
            close: 'glyphicon-remove',
            prev: 'glyphicon-chevron-left',
            next: 'glyphicon-chevron-right',
            prevYear: 'glyphicon-backward',
            nextYear: 'glyphicon-forward'
        },
        buttonText: {
            today:    'today',
            month:    'month',
            week:     'week',
            day:      'day',
            list:     'list'
        },
        navLinks: true, // can click day/week names to navigate views
        views: {
            month: { // name of view
                titleFormat: 'MMMM YYYY'
                // other view-specific options here
            }
        }
    })

});