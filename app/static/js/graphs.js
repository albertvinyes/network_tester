var results;
var stats
var qos;
var URL;

$(document).ready(function() {
  console.log("document ready");
  var arr = window.location.href.split("/");
  var domain = arr[0] + "//" + arr[2];

  function get_data_bandwidth() {
    url = domain+"/get_all_results";
    request = $.get(url, function(data_bandwidth) {
        results = JSON.parse(data_bandwidth);
        draw_timelines();
      })
      .fail(function() {
        alert( "error" );
      });
  }

  function get_stats() {
    url = domain+"/get_stats";
    request = $.get(url, function(data_stats) {
      stats = JSON.parse(data_stats);
      draw_averages_charts();
    })
    .fail(function() {
      alert( "error" );
    });
  }

  function get_qos() {
    url = domain+"/get_desired_qos";
    request = $.get(url, function(data_qos) {
      qos = JSON.parse(data_qos)
    })
    .fail(function() {
      alert( "error" );
    });
  }

  function draw_averages_charts() {
    var a = parseInt(stats["max_download"]);
    var b = parseInt(stats["avg_download"]);
    var c = parseInt(stats["min_download"]);
    var down_data = google.visualization.arrayToDataTable([
       ['Download', 'bps'],
       ['Max', a],
       ['Avg', b],
       ['Min', c]
    ]);

    var down_options = {
      chart: {
        title: 'Download',
      },
      bars: 'vertical',
      vAxis: {direction: -1},
      legend: {position: 'none'},
      colors: ["#17a2b8"]
    };

    a = parseInt(stats["max_upload"]);
    b = parseInt(stats["avg_upload"]);
    c = parseInt(stats["min_upload"]);
    var up_data = google.visualization.arrayToDataTable([
       ['Upload', 'bps'],
       ['Max', a],
       ['Avg', b],
       ['Min', c]
    ]);

    var up_options = {
      chart: {
        title: 'Upload',
      },
      vAxis: {format: 'decimal'},
      legend: {position: 'none'},
      colors: ["#F19F4D"]
    };

    a = parseInt(stats["max_latency"]);
    b = parseInt(stats["avg_latency"]);
    c = parseInt(stats["min_latency"]);
    var lt_data = google.visualization.arrayToDataTable([
       ['Latency to Google', 'ms'],
       ['Max', a],
       ['Avg', b],
       ['Min', c]
    ]);

    var lt_options = {
      chart: {
        title: 'Latency',
      },
      bars: 'vertical',
      vAxis: {format: 'decimal'},
      vAxis: {direction: -1},
      hAxis: {direction: -1},
      legend: {position: 'none'},
      colors: ["#7570b3"]
    };

    var chart1 = new google.charts.Bar(document.getElementById('stats_download_chart'));
    chart1.draw(down_data, google.charts.Bar.convertOptions(down_options));

    var chart2 = new google.charts.Bar(document.getElementById('stats_upload_chart'));
    chart2.draw(up_data, google.charts.Bar.convertOptions(up_options));

    var chart3 = new google.charts.Bar(document.getElementById('stats_latency_chart'));
    chart3.draw(lt_data, google.charts.Bar.convertOptions(lt_options));

  }

  function draw_timelines() {
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
        var single_result = [new Date(value.time.replace(" ", "T")), value.download, value.upload];
        data_bandwidth.addRows([single_result])
        single_result = [new Date(value.time.replace(" ", "T")), parseInt(value.latency_google), parseInt(value.latency_speednet)];
        data_latency.addRows([single_result])
    }

    var options1 = {
      title: 'Bandwidth',
      curveType: 'function',
      hAxis: {
        title: 'Year',
        titleTextStyle: {color: '#333'},
        slantedText:true,
        slantedTextAngle:80
      },
      displayZoomButtons: false,
      explorer: {
        actions: ['dragToZoom', 'rightClickToReset'],
        axis: 'horizontal',
        keepInBounds: true,
        maxZoomIn: 4.0
      },
      colors: ['#17a2b8','#F19F4D'],
      thickness: 4,
      legend: { position: 'bottom' }
    };

    var options2 = {
      title: 'Latency',
      curveType: 'function',
      legend: { position: 'bottom' }
    };
    var chart1 = new google.visualization.AnnotationChart(document.getElementById('bandwidth_chart'));
    var chart2 = new google.visualization.AnnotationChart(document.getElementById('latency_chart'));
    chart1.draw(data_bandwidth, options1);
    chart2.draw(data_latency, options1);
  }

  function get_all_data() {
    get_data_bandwidth();
    get_stats();
    get_qos();
  }

  google.charts.load('current', {'packages':['corechart','line','annotationchart','bar']});
  google.charts.setOnLoadCallback(get_all_data)
});
