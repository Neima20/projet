document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay'
      },
      events: [
        {
          title: 'Example Event 1',
          start: '2024-07-01',
          color: 'blue'
        },
        {
          title: 'Example Event 2',
          start: '2024-07-05',
          color: 'green'
        }
        // Ajoutez plus d'événements au besoin
      ],
      dateClick: function(info) {
        var title = prompt('Enter event title:');
        if (title) {
          var eventData = {
            title: title,
            start: info.dateStr,
            color: 'bleu' // Couleur par défaut pour les nouvelles tâches
          };
          calendar.addEvent(eventData);
        }
      }
    });
    calendar.render();
  });
  