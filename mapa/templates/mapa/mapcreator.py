# -*- coding: utf-8 -*-

import folium
from folium.features import CustomIcon
from shapely.wkt import loads
import pandas as pd
import geopandas as gpd
from os.path import exists
from datetime import datetime as dt
from folium.map import *


tmp_df = pd.read_csv('db_all_db.csv', dtype={
                     'store_point': str, 'geometry': str}, encoding='utf-8')

tmp_df.store_point = tmp_df.store_point.str.decode('utf-8')

crs = {'init': 'epsg:4326'}

c_coords = (19.006626, -98.801924)

m = folium.Map(location=c_coords, zoom_start=6)

fg_acopio = FeatureGroup(name='Acopio')
fg_achosp = FeatureGroup(name='Acopio Hospital')
fg_reqvol = FeatureGroup(name='Requiero Voluntarios')
fg_alberg = FeatureGroup(name='Dar de Alta Albergue')
fg_derrum = FeatureGroup(name='Dar de Alta Derrumbe')
fg_danios = FeatureGroup(name=u'Dar de Alta Daños')
fg_revinm = FeatureGroup(name=u'Requiero de Revisión en mi Inmueble')
fg_blanco = FeatureGroup(name='Hospitales')

for id_, r in tmp_df.iterrows():
    color = 'white'
    if r['tipo'].encode('utf-8') == 'Acopio':
        color = 'blue'
        icon = folium.Icon(color=color, icon='none')
        fg_acopio.add_child(Marker([r['lat'], r['lon']],
                                   popup=r['suc'].title(), icon=icon))
    elif r['tipo'].encode('utf-8') == 'Acopio Hospital':
        color = 'white'
        icon = folium.Icon(color=color, icon='none')
        fg_achosp.add_child(Marker([r['lat'], r['lon']],
                                   popup=r['suc'].title(), icon=icon))
    elif r['tipo'].encode('utf-8') == 'Requiero Voluntarios':
        color = 'red'
        icon = folium.Icon(color=color, icon='none')
        fg_reqvol.add_child(Marker([r['lat'], r['lon']],
                                   popup=r['suc'].title(), icon=icon))
    elif r['tipo'].encode('utf-8') == 'Dar de Alta Albergue':
        color = 'green'
        icon = folium.Icon(color=color, icon='none')
        fg_alberg.add_child(Marker([r['lat'], r['lon']],
                                   popup=r['suc'].title(), icon=icon))
    elif r['tipo'].encode('utf-8') == 'Dar de Alta Derrumbe':
        color = 'black'
        icon = folium.Icon(color=color, icon='none')
        fg_derrum.add_child(Marker([r['lat'], r['lon']],
                                   popup=r['suc'].title(), icon=icon))
    elif r['tipo'].encode('utf-8') == 'Dar de Alta Daños':
        color = 'orange'
        icon = folium.Icon(color=color, icon='none')
        fg_danios.add_child(Marker([r['lat'], r['lon']],
                                   popup=r['suc'].title(), icon=icon))
    elif r['tipo'].encode('utf-8') == 'Requiero de Revisión en mi Inmueble':
        color = 'lightred'
        icon = folium.Icon(color=color, icon='none')
        fg_revinm.add_child(Marker([r['lat'], r['lon']],
                                   popup=r['suc'].title(), icon=icon))

    else:
        color = 'white'
        icon = folium.Icon(color=color, icon='none')
        fg_blanco.add_child(Marker([r['lat'], r['lon']],
                                   popup=r['suc'].title(), icon=icon))

# m.add_child(fg_acopio)
# m.add_child(fg_achosp)
# m.add_child(fg_reqvol)
# m.add_child(fg_alberg)
# m.add_child(fg_derrum)
# m.add_child(fg_danios)
# m.add_child(fg_revinm)
# m.add_child(fg_blanco)
# m.add_child(folium.map.LayerControl())

tmp_df = pd.read_csv('db_jot.csv', parse_dates=['timestamp'], dtype={
                     'store_point': str, 'geometry': str}, encoding='utf-8')

tmp_df.store_point = tmp_df.store_point.str.decode('utf-8')

crs = {'init': 'epsg:4326'}

for id_, r in tmp_df.iterrows():
    color = 'white'
    if r['tipo'].encode('utf-8') == 'Acopio':
        color = 'blue'
        icon = folium.Icon(color=color, icon='none')
        if (dt.now() - r['timestamp']).total_seconds() / 3600 < 4:
            fg_acopio.add_child(Marker([r['lat'], r['lon']],
                                       popup=r['suc'].title(), icon=icon))
    elif r['tipo'].encode('utf-8') == 'Acopio Hospital':
        color = 'white'
        icon = folium.Icon(color=color, icon='none')
        if (dt.now() - r['timestamp']).total_seconds() / 3600 < 24:
            fg_achosp.add_child(Marker([r['lat'], r['lon']],
                                       popup=r['suc'].title(), icon=icon))
    elif r['tipo'].encode('utf-8') == 'Requiero Voluntarios':
        color = 'red'
        icon = folium.Icon(color=color, icon='none')
        if (dt.now() - r['timestamp']).total_seconds() / 3600 < 4:
            fg_reqvol.add_child(Marker([r['lat'], r['lon']],
                                       popup=r['suc'].title(), icon=icon))
    elif r['tipo'].encode('utf-8') == 'Dar de Alta Albergue':
        color = 'green'
        icon = folium.Icon(color=color, icon='none')
        fg_alberg.add_child(Marker([r['lat'], r['lon']],
                                   popup=r['suc'].title(), icon=icon))
    elif r['tipo'].encode('utf-8') == 'Dar de Alta Derrumbe':
        color = 'black'
        icon = folium.Icon(color=color, icon='none')
        fg_derrum.add_child(Marker([r['lat'], r['lon']],
                                   popup=r['suc'].title(), icon=icon))
    elif r['tipo'].encode('utf-8') == 'Dar de Alta Daños':
        color = 'orange'
        icon = folium.Icon(color=color, icon='none')
        fg_danios.add_child(Marker([r['lat'], r['lon']],
                                   popup=r['suc'].title(), icon=icon))
    elif r['tipo'].encode('utf-8') == 'Requiero de Revisión en mi Inmueble':
        color = 'lightred'
        icon = folium.Icon(color=color, icon='none')
        if (dt.now() - r['timestamp']).total_seconds() / 3600 < 12:
            fg_revinm.add_child(Marker([r['lat'], r['lon']],
                                       popup=r['suc'].title(), icon=icon))

    else:
        color = 'white'
        icon = folium.Icon(color=color, icon='none')
        fg_blanco.add_child(Marker([r['lat'], r['lon']],
                                   popup=r['suc'].title(), icon=icon))

    # if ((dt.now() - r['timestamp']).total_seconds() / 3600 < 4 and (r['tipo'].encode('utf-8')
    # == 'Acopio' or r['tipo'].encode('utf-8') == 'Requiero Voluntarios')):
    #     m.add_child(marker)
    #
    # elif ((dt.now() - r['timestamp']).total_seconds() / 3600 < 24 and
    # (r['tipo'].encode('utf-8') == 'Acopio Hospital')):
    #     m.add_child(marker)
    #
    # elif ((dt.now() - r['timestamp']).total_seconds() / 3600 < 12 and
    # r['tipo'].encode('utf-8') == 'Requiero de Revisión en mi Inmueble'):
    #     m.add_child(marker)
    #
    # elif (r['tipo'].encode('utf-8') == 'Dar de Alta Albergue' or r['tipo'].encode('utf-8') ==
    # 'Dar de Alta Derrumbe' or r['tipo'].encode('utf-8') == 'Dar de Alta Daños'):
    #     m.add_child(marker)

m.add_child(fg_acopio)
m.add_child(fg_achosp)
m.add_child(fg_reqvol)
m.add_child(fg_alberg)
m.add_child(fg_derrum)
m.add_child(fg_danios)
m.add_child(fg_revinm)
m.add_child(fg_blanco)
m.add_child(folium.map.LayerControl())

# folium.LayerControl().add_to(m)
m.save('mapa.html')
