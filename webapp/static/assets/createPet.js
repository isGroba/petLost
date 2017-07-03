function initMap() {
    var uluru = new google.maps.LatLng(42.661073,-8.113604);
    var map = new google.maps.Map(document.getElementById('map'), {
      center: uluru,
      zoom: 15,
    });
    var marker = new google.maps.Marker({
    position: uluru,
    map: map,
    draggable: true,
    animation: google.maps.Animation.DROP,
    });
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        var pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
        marker.setPosition(pos);
        map.setCenter(pos);
      }, function() {
        handleLocationError(true, marker, map.getCenter());
      });
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, marker, map.getCenter());
    }
    marker.addListener('position_changed', function() {
      var new_pos = marker.getPosition();
      document.getElementById('id_location').value = new_pos.lat()+','+new_pos.lng();
});
}

function handleLocationError(browserHasGeolocation, marker, pos) {
  document.getElementById('id_location').value = pos.lat+','+pos.lng;
  marker.setPosition(pos);
  marker.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
}