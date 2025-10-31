import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import seaborn as sns
import time
import requests
from datetime import datetime
import api
import style
import locs
API_KEY = api.api()
def get_traffic_level(current_speed, free_flow_speed):
    ratio = current_speed / free_flow_speed
    if ratio >= 0.85:
        return "Low"
    elif ratio >= 0.5:
        return "Medium"
    else:
        return "High"
style.style_for_st()
#-------------------------------------------------/styles------------------------------------------------------
df=pd.read_csv("traffic_data.csv")
df["area"]=df["area"].str.lower()
#-------------------------------------------------mappings------------------------------------------------------
locations=locs.lan_lot()
days={'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5,'Sunday': 6}
#-------------------------------------------------models---------------------------------------------------------
with open("traf_model","rb") as f:
    traf_model=pickle.load(f)
with open("weather_model","rb") as fl:
    weather_model=pickle.load(fl)
area=st.sidebar.selectbox("select area of visit:",df["area"].unique(),index=5)
hour=st.sidebar.multiselect("select hour of visit:",sorted(df["hour"].unique()),default=sorted(df["hour"].unique())[:5])
day=st.sidebar.selectbox("select day of visit:",["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
target_mapper={0:"Low",1:"Medium",2:"High"}
lat, lon = locations[area][0], locations[area][1]
url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point={lat},{lon}&unit=KMPH&key={API_KEY}"
response = requests.get(url)
url2= ("https://api.open-meteo.com/v1/forecast"f"?latitude={lat}&longitude={lon}&current_weather=true")
response2=requests.get(url2)
if response.text.strip(): 
    data = response.json()
    w_data=response2.json()
    temp=w_data["current_weather"]["temperature"]
    code=w_data["current_weather"]["weathercode"]
    wind=w_data["current_weather"]["windspeed"]
    current_speed = data['flowSegmentData']['currentSpeed']
    free_flow_speed = data['flowSegmentData']['freeFlowSpeed']
    traffic_level = get_traffic_level(current_speed, free_flow_speed)
pred=(weather_model.predict([[days[day],datetime.now().hour,locations[area][0],locations[area][1],code,wind]]))
st.sidebar.markdown("<div class='metric-card'><div class='metric-title'> Predicted Temp for Today</div>"
                    f"<div class='metric-value'>{int(pred)} °C</div></div>", unsafe_allow_html=True)

st.sidebar.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.sidebar.markdown(f"<div class='metric-card'><div class='metric-title'> Current Temp at <b>{area.title()}</b></div>"
                    f"<div class='metric-value'>{temp} °C</div></div>", unsafe_allow_html=True)

st.sidebar.markdown("<div class='divider'></div>", unsafe_allow_html=True)

color = {"Low":"#00c853", "Medium":"#ffb300", "High":"#e53935"}[traffic_level]
st.sidebar.markdown(f"""
<div class='metric-card' style='background: linear-gradient(135deg, {color}, #00000030);'>
<div class='metric-title'> Current Traffic Level</div>
<div class='metric-value'>{traffic_level}</div>
</div>
""", unsafe_allow_html=True)
#-------------------------------------------------/models-----------------------------------------------------------
#-------------------------------------------------visuals---------------------------------------------------------
st.html("<h1 align='center' class='title'>Traffic Predictor</h1>")
st.markdown("""---""")
filtered_df=df[(df["area"]==area)& (df["hour"].isin(hour))&(df["day"]==days[day])]
def visuals(df_filtered):
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Pie Chart by Area")
        fig,ax=plt.subplots(figsize=(2,2))
        fig.patch.set_alpha(0.0)
        ax.pie(df_filtered["traffic_level"].value_counts().values,
            labels=df_filtered["traffic_level"].unique(),
            colors=["green","orange","red"],
            textprops={"color":"white"},autopct='%1.1f%%',pctdistance=0.7)
        ax.set_title(area,color="white")
        st.pyplot(fig)
    with col2:
        st.subheader("Traffic Map by Area")
        fig, ax = plt.subplots()
        palette = {
            "Low": (0, 1, 0),     # Green
            "Medium": (1, 1, 0),  # Yellow
            "High": (1, 0, 0)     # Red
        }
        fig,ax=plt.subplots(figsize=(2,2))
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        # ax.set_xlim(0.0,6.0,)
        # ax.set_xticks(range(0,6,1))
        ax.set_xlabel("Categories", color="white")
        ax.set_ylabel("Values", color="white")
        ax.set_title(area,color="white")
        sns.countplot(data=df_filtered,x="traffic_level", ax=ax,hue="traffic_level",palette=palette)
        st.pyplot(fig)
#-------------------------------------------------visuals---------------------------------------------------------
st.html("<h1 align='center'>Overall Visuals</h1>")
st.subheader("Traffic Level On Each Day")
fig,ax=plt.subplots()
order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
palette = {"Low":"green", "Medium":"orange", "High":"red"}
fig.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
sns.countplot(data=df[df["area"]==area], x="day", hue="traffic_level", palette=palette,ax=ax)
ax.set_title(area,color="white")
ax.set_xlabel("day",color="white")
ax.set_ylabel("count",color="white")
ax.set_xticklabels(order)
st.pyplot(fig)
st.markdown("""---""")
visuals(df[(df["area"]==area)& df["hour"].isin(sorted(df["hour"].unique()))&(df["day"]==days[day])])
#-------------------------------------------------/visuals---------------------------------------------------------
#-------------------------------------------------predictions---------------------------------------------------------
preds=[]
for h in hour:
        pred=(traf_model.predict([[days[day],h,locations[area][0],locations[area][1]]]))
        preds.append(int(pred))
st.markdown("""---""")
st.html("<h1 align='center'>Prediction Values</h1>")
pred_container=st.container(border=True)
with pred_container:
    i=0
    col1,col2,col3,col4=st.columns(4)
    while i<len(hour):
        for col in [col1,col2,col3,col4]:
                with col:
                    st.subheader(f"At : {hour[i]}")
                    pred=(traf_model.predict([[days[day],hour[i],locations[area][0],locations[area][1]]]))
                    if int(pred)==0 or int(pred)==1:
                        st.success(f"pred: {target_mapper[int(pred)]}")
                    else:
                        st.warning(f"pred: {target_mapper[int(pred)]}") 
                    i+=1
                    if i>=len(hour):
                        break
                time.sleep(0.5)
#-------------------------------------------------/predictions---------------------------------------------------------
#-------------------------------------------------visuals---------------------------------------------------------
st.markdown("""<br>""",unsafe_allow_html=True)
st.html("<h1 align='center'>Prediction Visuals</h1>")
vis_container=st.container(border=True)
with vis_container:
    visuals(df[(df["area"]==area)&(df["hour"].isin(hour))&(df["day"]==days[day])])
#-------------------------------------------------/visuals---------------------------------------------------------
st.caption("Designed By Vamsi Krishna and Charan Teja")