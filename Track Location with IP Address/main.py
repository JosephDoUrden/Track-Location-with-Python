import geocoder
import folium

g = geocoder.ip("")

myAddress = g.latlng

myMap = folium.Map(location=myAddress, zoom_start=9)
folium.CircleMarker(location=myAddress, radius=50, popup="location").add_to(myMap)
folium.Marker(myAddress, popup="location").add_to(myMap)

myMap.save("myLocation.html")
