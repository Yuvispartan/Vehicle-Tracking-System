import folium
m = folium.Map(location=[11.0168, 76.9558])
m

from branca.element import Figure
fig=Figure(width=550,height=350)

m1=folium.Map(width=550,height=350,location=[11.0168, 76.9558],zoom_start=11,min_zoom=8,max_zoom=14)
fig.add_child(m1)
m1

fig2=Figure(width=550,height=350)
m2=folium.Map(location=[11.0168, 76.9558])
fig2.add_child(m2)
folium.TileLayer('Stamen Terrain').add_to(m2)
folium.TileLayer('Stamen Toner').add_to(m2)
folium.TileLayer('Stamen Water Color').add_to(m2)
folium.TileLayer('cartodbpositron').add_to(m2)
folium.TileLayer('cartodbdark_matter').add_to(m2)
folium.LayerControl().add_to(m2)
m2

fig3=Figure(width=550,height=350)
m3=folium.Map(location=[11.0168, 76.9558],tiles='cartodbpositron',zoom_start=11)
fig3.add_child(m3)

folium.Marker(location=[11.0703, 77.0852],popup='Default popup Marker1',tooltip='Click here to see Popup').add_to(m3)
folium.Marker(location=[11.0176, 76.9674],popup='<strong>Marker3</strong>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)
folium.Marker(location=[11.0346, 77.0156],popup='<h3 style="color:green;">Marker2</h3>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)
m3

fig4=Figure(height=350,width=550)
m4=folium.Map(location=[11.0168, 76.9558],tiles='cartodbpositron',zoom_start=11)
fig4.add_child(m4)

# Adding Custom Markers
folium.Marker(location=[11.0703, 77.0852],popup='Custom Marker 1',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='red',icon='none')).add_to(m4)
folium.Marker(location=[11.0176, 76.9674],popup='Custom Marker 2',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='green',prefix='glyphicon',icon='off')).add_to(m4)
folium.Marker(location=[11.0346, 77.0156],popup='Custom Marker 3',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='purple',prefix='fa',icon='anchor')).add_to(m4)
m4
'''
coords_1 = [[11.0703, 77.0852]]
coords_2 = [[11.0176, 76.9674]]
coords_3 = [[11.0346, 77.0156]]
'''
fig5=Figure(height=550,width=750)
m5=folium.Map(location=[11.0168, 76.9558],tiles='cartodbpositron',zoom_start=14)
fig5.add_child(m5)

f1=folium.FeatureGroup("Vehicle 1")
f2=folium.FeatureGroup("Vehicle 2")
f3=folium.FeatureGroup("Vehicle 3")

# Adding lines to the different feature groups
line_1=folium.vector_layers.PolyLine(coords_1,popup='<b>Path of Vehicle_1</b>',tooltip='Vehicle_1',color='blue',weight=10).add_to(f1)
line_2=folium.vector_layers.PolyLine(coords_2,popup='<b>Path of Vehicle_2</b>',tooltip='Vehicle_2',color='red',weight=10).add_to(f2)
line_3=folium.vector_layers.PolyLine(coords_3,popup='<b>Path of Vehicle_3</b>',tooltip='Vehicle_3',color='green',weight=10).add_to(f3)

f1.add_to(m5)
f2.add_to(m5)
f3.add_to(m5)
folium.LayerControl().add_to(m5)
m5