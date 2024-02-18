const googleMaps = () => {
    const listItems = document.querySelectorAll(".reminders-list-item");
  
    // Add click event listener to each list item
    listItems.forEach((item) => {
      item.addEventListener("click", () => {
        item.classList.toggle("checked");
      });
    });
  
    var mapProp = {
      center: new google.maps.LatLng(51.508742, -0.12085),
      zoom: 5,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
  };
  
  export default googleMaps;