#use dir(folium) to list methods of folium, then use help(folium.method) for info on that

#import folium and jinja2 w/pip install
#install pandas
import folium
import pandas

#reads data from volcanoes and inputs it to DataFrame object named data
data = pandas.read_csv("volcanoes.txt")

#assigns variable lat to latitudes in list format
lat = list(data["LAT"])

#assigns variable lon to longitudes in list format
lon = list(data["LON"])

#assigns variable eleva to evelations of volcation in data in list format
eleva = list(data["ELEV"])

#assigns variable mt_name to names of volcanoes
mt_name = list(data["NAME"])

#assigns variable mt_location to names of locations
mt_location = list(data["LOCATION"])

def color_maker(elv):
    if elv > 0 and elv <=1000:
        return 'green'
    elif elv > 1001 and elv <= 3000:
        return 'orange'
    else:
        return 'red'

#assigns the map with location coords, start zoom, and default terain tiles
map = folium.Map(location=[35,127], zoom_start=6, min_zoom=2, tiles="Stamen Terrain")

#adds a feature group, such as Marker for ex.
feature_group_volcanoes = folium.FeatureGroup(name="volcanoes")

#we can use a for loop to add latitude, longitude and elevation to our map from our volcano data.
for lt, ln, elv, mountname, locat in zip(lat, lon, eleva, mt_name, mt_location):
    # adding objects(children)to map, and icon takes a folium method   called Icon
    feature_group_volcanoes.add_child(folium.CircleMarker(location=[lt, ln], radius= 6, popup="Name: %s, Location: %s, Meters: %s" %(mountname, locat, elv), fill_color=color_maker(elv), color='grey', fill_opacity=0.8))

feature_group_population = folium.FeatureGroup(name="population")

#passing GeoJSON to a new child
feature_group_population.add_child(folium.GeoJson(data=open('world_data.json', 'r', encoding='utf-8-sig').read(),
                                       style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
                                       else 'orange' if 15000000 <= x['properties']['POP2005'] < 30000000 else 'red'}))

map.add_child(feature_group_population)

#passing feature group to add_child
map.add_child(feature_group_volcanoes)

#toggle feature
map.add_child(folium.LayerControl())

#saves map to html file named Map1
map.save("Map1.html")

