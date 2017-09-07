$(document).ready(function() {
  console.log("ready")

  function get_data() {
    url = "http://localhost:"+port+"/get_all_results";
    request = $.get(url, function(data) {
        console.log(JSON.parse(data));
      })
      .fail(function() {
        alert( "error" );
      });
  }

  get_data()

  //console.log(results);

  // get_data();

});
