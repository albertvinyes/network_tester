var results;


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

  get_data_bandwidth();

  google.charts.load('current', {'packages':['corechart']});
  google.charts.setOnLoadCallback(drawChart);

  function drawChart() {
    var data_bandwidth = new google.visualization.data_bandwidthTable();
    data_bandwidth.addColumn('date','Date');
    data_bandwidth.addColumn('number', 'Download');
    data_bandwidth.addColumn('number', 'Upload');

    var data_latency = new google.visualization.data_bandwidthTable();
    data_latency.addColumn('date','Date');
    data_latency.addColumn('number', 'Google DSN ping');
    data_latency.addColumn('number', 'SpeedNet ping');

    for (var key in results) {
        if (key === 'length' || !results.hasOwnProperty(key)) continue;
        var value = results[key];
        single_result = [new Date(value.time), value.download, value.upload]
        console.log(single_result);
        data_bandwidth.addRows([single_result])
        // for (key in value) {
        //   console.log(key);
        //   console.log(value[key]);
        // }
    }

    var options = {
      title: 'Bandwidth',
      curveType: 'function',
      legend: { position: 'bottom' }
    };

    var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

    chart.draw(data_bandwidth, options);
  }


  //console.log(results);

  // get_data_bandwidth();

});
