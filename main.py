# import libraries (already installed in virtual environment iss_venv)
import pandas as pd
import plotly.express as px
from time import sleep

def iss_plotter(x,y):
    # variable will store the url of the Open Notify API which has realtime ISS locations
    url = "http://api.open-notify.org/iss-now.json"

    df = pd.read_json(url)

    # the JSON we received has Latitude and Longitude in 2 different Rows, we need them in same row for plotly. Hence altering the dataframe.
    df['latitude'] =  df.loc['latitude','iss_position']
    df['longitude'] = df.loc['longitude','iss_position']
    df.reset_index(inplace = True)

    # drop the columns no longer required
    df = df.drop(['index', 'iss_position', 'message'], axis = 1)

    df.loc[1,'latitude'] = x
    df.loc[1, 'longitude'] = y

    # plot the latitude and longitude on a geographical scatter plot using plotly
    fig = px.scatter_geo(df, lat='latitude', lon='longitude', projection="natural earth")
    fig.show()

    if df.loc[0,'latitude'] == df.loc[1,'latitude'] and df.loc[0, 'longitude'] == df.loc[1, 'longitude']:
        print("ISS is flying over you right now")        
    
if __name__ == '__main__':
    lat = input('Enter your Latitide: ')
    lon = input('Enter your Longitude: ')
    try:
        iss_plotter(lat,lon)      
    except Exception as err:
        print(f"Thanks for using app./n Exit Code: {err}")
    