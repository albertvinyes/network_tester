
$(document).ready(function() {
  var result;

  function run_test() {
    url = "http://localhost:"+port+"/run_test";
    request = $.get(url, function(data_bandwidth) {
        result = JSON.parse(data_bandwidth)
        $("#download").html((result["download"]/1000000).toFixed(2) + " Mbps");
        $("#upload").html((result["upload"]/1000000).toFixed(2) + " Mbps");
        $("#latency_google").html(parseFloat(result["latency_google"]).toFixed(2) + " ms");
        $("#latency_speednet").html(parseFloat(result["latency_speednet"]).toFixed(2) + " ms");
        $("#modalTitle").html("Run at " + result["time"])
        $("#results-table").show();
      })
      .fail(function() {
        alert( "error" );
      })
      .always(function() {
        $("#progressBar").hide();
      });
  }

  $("#runTestButton").click(function() {
    $("#modalTitle").html("Running Network Speed Test")
    $("#results-table").hide();
    $("#progressBar").show();
    run_test();
  });

});
