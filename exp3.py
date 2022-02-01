import folium
import os
import json

# Create map object
m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

# Global tooltip
tooltip = 'Click For More Info'

# Create custom marker icon


# Vega data
vis = os.path.join('data', 'vis.json')

# Geojson Data
overlay = os.path.join('data', 'overlay.json')

# Create markers
folium.Marker([42.363600, -71.099500],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(m),
folium.Marker([42.333600, -71.109500],
              popup='<strong>Location Two</strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([42.377120, -71.062400],
              popup='<strong>Location Three</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='purple')).add_to(m),
folium.Marker([42.374150, -71.122410],
              popup='<strong>Location Four</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m),



# Circle marker
folium.CircleMarker(
    location=[42.466470, -70.942110],
    radius=50,
    popup='My Birthplace',
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(m)

# Geojson overlay


# Generate map
m.save('map.html')