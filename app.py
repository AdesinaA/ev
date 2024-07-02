#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import numpy  as np
import folium
from folium import Marker
from folium.plugins import MarkerCluster
import streamlit as st 

StreamlitPatcher().jupyter() 


# In[51]:


ev_stations_df  = pd.read_csv("/Users/adesinasmac/Downloads/ev_stations.csv")


# In[52]:


ev_stations_df.head()


# In[55]:


ev_stations_df.columns


# In[57]:


locations_df = ev_stations_df[ev_stations_df["Latitude"].notnull() & ev_stations_df["Longitude"].notnull()]
Charlotte_NC_locations_df = locations_df[(locations_df["State"] == "NC") & (locations_df["City"] == "Charlotte")]
Charlotte_NC_locations_df.head()


# In[59]:


charlotte_map = folium.Map(location=[35.227, -80.843], tiles="openstreetmap", zoom_start=11)


for idx, row in Charlotte_NC_locations_df.iterrows():
    Marker(location=[row["Latitude"], row["Longitude"]],
           popup=row["Street Address"]).add_to(charlotte_map)

charlotte_map


# In[61]:


NC_locations_df = locations_df[(locations_df["State"] == "NC")]
NC_locations_df.head()


# In[69]:


nc_map = folium.Map(location=[35.5908438, -79.7628341], tiles="openstreetmap", zoom_start=7)

mc = MarkerCluster()
for idx, row in NC_locations_df.iterrows():
    mc.add_child(Marker(location=[row["Latitude"], row["Longitude"]],
                        popup=row["Street Address"]))

nc_map.add_child(mc)

nc_map


# In[ ]:




