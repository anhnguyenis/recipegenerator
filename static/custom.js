$(document).ready(function(){
    $("#signUpForm").submit(function(){
        alert("Don't forget to like us on Facebook!");
    });
    $("#buttonTest").click(function(){
        alert("Don't forget to like us on Facebook");
    });
});


  function initMap() {
      var uluru = {lat: 51.508742, lng: -0.120850};
      var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: uluru
          });
      var marker = new google.maps.Marker({
          position: uluru,
          map: map
    });
  }
  function weightConverter(valNum) {
    document.getElementById("outputgrams").innerHTML=valNum*200.0;
  }
