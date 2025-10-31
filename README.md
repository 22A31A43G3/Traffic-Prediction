# Traffic Prediction  

##  Project Overview  
This project aims to predict traffic conditions using historical traffic and weather data. The goal is to forecast traffic flow so that urban planners, commuters, or app-developers can leverage those predictions to improve routing, reduce congestion, and plan better infrastructure.

##  Tech Stack & Tools  
- Language: **Python** (100 %)  
- Data handling: Pandas, NumPy  
- Modeling & Analysis: scikit-learn, pickle to save the model
- Web / App: `traffic_app.py` streamlit is used 
- Files & modules:  
  - `locs.py` — handles location data consists dictionary for lat and lon of locations  
  - `style.py` — defines visual styles  
  - `traffic script.py` — used to collect the traffic data and weather data from the api  
  - `traf_model` — traffic-prediction model 
  - `weather_model` — weather-prediction model  
  - `traffic_data.csv` — dataset used for modeling 

##  Dataset  
- The dataset `traffic_data.csv` is included in the repo.  
- It contains historical traffic observations (and possibly weather features) mapped to location(s) and timestamps.   

##  Model & Approach  
- The models is in the repo `traf_model` and `weather_model`.  
- Approach: Use historical traffic data + weather features (via `weather_model`) to forecast future traffic volumes congestion levels.  
- decision tree regressor is used for the predictions  
- achieved 0.91 accuracy for new data for traffic prediction and 0.99 for weather prediction

##  How to Run  
1. Clone the repo:  
   ```bash
   git clone https://github.com/22A31A43G3/Traffic-Prediction.git
   cd Traffic-Prediction
