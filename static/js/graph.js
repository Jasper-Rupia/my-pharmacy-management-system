
var ctx = document.getElementById("myChart").getContext("2d");

// var gradient = ctx.crateLinearGradient(0, 0, 0, 400);
// gradient.addColorStop(0, "rgba(58, 123, 213, 1)");
// gradient.addColorStop(1, "rgba(0, 213, 255, 0.3)");

var labels = ['SUN', 'SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON'];

var data = {
  labels,
  datasets: [{
    label: 'Sales data',
    data: [0, 5, 6, 8, 25, 9, 24],
    fill: true,
    borderColor: 'rgb(75, 192, 192, 1)',
    backgroundColor: 'rgb(75, 192, 192, 0.1)',
    pointBackgroundColor: 'rgb(0, 0, 0, 0.5)',
    tension: 0.3
  },{
    label: 'Purchases data',
    data: [0, 3, 1, 2, 8, 1, 5],
    fill: true,
    borderColor: 'rgb(13, 110, 253)',
    backgroundColor: 'rgb(13, 110, 253, 0.1)',
    pointBackgroundColor: 'rgb(0, 0, 0, 0.5)',
    tension: 0.3
  }]
};

var config = {
    type: 'line',
    data,
    options: {
      responsive: true,
      radius: 3,
      hitRadius: 5,
      hoverRadius: 7,
      scales: {
        y: {
          ticks: {
            callback: function(value){
              return "Tsh " + value;
            }
          }
        }
      }
    }
};

var theChart = new Chart(ctx, config);