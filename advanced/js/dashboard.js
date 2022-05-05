var labels = [1, 2, 3, 4, 5, 6, 7];

var data = {
  labels,
  datasets: [{
    label: 'Sales data',
    data: [0, 5, 6, 8, 25, 9, 24],
    fill: true,
    borderColor: 'rgb(75, 192, 192)',
    tension: 0.5
  },{
    label: 'Purchases data',
    data: [0, 3, 1, 2, 8, 1, 5],
    fill: true,
    borderColor: '#0d6efd',
    tension: 0.5
  }]
};

var config = {
    type: 'line',
    data,
    options: {}
};
var ctx = document.getElementById("myChart");

var theChart = new Chart(ctx, config);