var results;
var qos;


$(document).ready(function() {

  console.log("ready")
  function get_data_bandwidth() {
    url = "http://localhost:"+port+"/get_all_results";
    request = $.get(url, function(data_bandwidth) {
        results = JSON.parse(data_bandwidth)
        console.log(JSON.parse(data_bandwidth));
      })
      .fail(function() {
        alert( "error" );
      });
  }

  function get_qos() {
    url = "http://localhost:"+port+"/get_desired_qos";
    request = $.get(url, function(data_qos) {
      qos = JSON.parse(data_qos)
      console.log(qos);
    })
    .fail(function() {
      alert( "error" );
    });
  }

  get_data_bandwidth();

  google.charts.load('current', {'packages':['corechart']});
  google.charts.setOnLoadCallback(drawChart);

  function drawChart() {
    var data_bandwidth = new google.visualization.DataTable();
    data_bandwidth.addColumn('datetime','Date');
    data_bandwidth.addColumn('number', 'Download');
    data_bandwidth.addColumn('number', 'Upload');

    var data_latency = new google.visualization.DataTable();
    data_latency.addColumn('datetime','Date');
    data_latency.addColumn('number', 'Google DSN ping');
    data_latency.addColumn('number', 'SpeedNet ping');

    for (var key in results) {
        if (key === 'length' || !results.hasOwnProperty(key)) continue;
        var value = results[key];
        var single_result = [new Date(value.time), value.download, value.upload];
        console.log(value.time);
        data_bandwidth.addRows([single_result])
        single_result = [new Date(value.time), parseInt(value.latency_google), parseInt(value.latency_speednet)];
        console.log(value.time);
        data_latency.addRows([single_result])
    }

    var options1 = {
      title: 'Bandwidth',
      curveType: 'function',
      legend: { position: 'bottom' }
    };

    var options2 = {
      title: 'Latency',
      curveType: 'function',
      legend: { position: 'bottom' }
    };

    get_qos();

    var chart1 = new google.visualization.LineChart(document.getElementById('bandwidth_chart'));
    var chart2 = new google.visualization.LineChart(document.getElementById('latency_chart'));
    chart1.draw(data_bandwidth, options1);
    chart2.draw(data_latency, options2);
  }


  //console.log(results);

  // get_data_bandwidth();

});
