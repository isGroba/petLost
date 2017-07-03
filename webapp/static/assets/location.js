var coor = document.getElementById('coor').innerHTML;
var list_coor = coor.split(',',2);
function initMap() {
    var uluru = new google.maps.LatLng(list_coor[0],list_coor[1]);
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: uluru,
    });
    var marker = new google.maps.Marker({
        position: uluru,
        map: map,
        animation: google.maps.Animation.BOUNCE,
    });
}