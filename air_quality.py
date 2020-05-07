from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Simple Weather App")
root.geometry('600x150')

# declare label widgets 
myLabel = Label(root)
pm25Label = Label(root)
o3Label = Label(root)
no2Label = Label(root)

# Create Zipcode Lookup Function
def cityLookup():
    try:
        # request api from third party weather website
        api_request = requests.get("https://api.waqi.info/feed/" + cityEntry.get() + "/?token=7dc26ee6bbc8fd10f83cabe193346b0037a0080a")
        api = json.loads(api_request.content)

        # extract data from the json api and store them in variables
        city = api['data']['city']['name']
        overallQuality = api['data']['iaqi']['pm25']['v']
        pm25Quality = api['data']['iaqi']['pm25']['v']
        o3Quality = api['data']['iaqi']['o3']['v']
        no2Quality = api['data']['iaqi']['no2']['v']

        # according to each air quality measurements set category and its colour
        if overallQuality >= 0 and overallQuality <= 50:
            weather_colour = "#0C0"
            category = 'Good'
            myLabel.configure(foreground='black')
            pm25Label.configure(foreground='black')
            o3Label.configure(foreground='black')
            no2Label.configure(foreground='black')
        elif overallQuality >= 51 and overallQuality <= 100:
            weather_colour = "#FFFF00"
            category = 'Moderate'
            myLabel.configure(foreground='black')
            pm25Label.configure(foreground='black')
            o3Label.configure(foreground='black')
            no2Label.configure(foreground='black')
        elif overallQuality >= 101 and overallQuality <= 150:
            weather_colour = "#ff9900"
            category = 'Unhealthy for Sensitive Groups'
            myLabel.configure(foreground='black')
            pm25Label.configure(foreground='black')
            o3Label.configure(foreground='black')
            no2Label.configure(foreground='black')
        elif overallQuality >= 151 and overallQuality <= 200:
            weather_colour = "#FF0000"
            category = 'Unhealthy'
            myLabel.configure(foreground='white')
            pm25Label.configure(foreground='white')
            o3Label.configure(foreground='white')
            no2Label.configure(foreground='white')
        elif overallQuality >= 201 and overallQuality <= 300:
            weather_colour = "#990066"
            category = 'Very Unhealthy'
            myLabel.configure(foreground='white')
            pm25Label.configure(foreground='white')
            o3Label.configure(foreground='white')
            no2Label.configure(foreground='white')
        elif overallQuality >= 301:
            weather_colour = "#660000"
            category = 'Hazardous'
            myLabel.configure(foreground='white')
            pm25Label.configure(foreground='white')
            o3Label.configure(foreground='white')
            no2Label.configure(foreground='white')

        root.configure(background=weather_colour)
        
        # output each measurements to their own labels
        myLabel.configure(text=city + " Air Quality " + str(overallQuality) + " " + category, font=("Helverica", 20), background=weather_colour)
        myLabel.grid(row=1, column=0, pady=5, columnspan=2)

        pm25Label.configure(text="pm2.5 : " + str(pm25Quality), font=("Helverica", 15), background=weather_colour)
        pm25Label.grid(row=2, column=0, padx=40, columnspan=2, sticky=W)

        o3Label.configure(text="O3 : " + str(o3Quality), font=("Helverica", 15), background=weather_colour)
        o3Label.grid(row=3, column=0, padx=40, columnspan=2, sticky=W)

        no2Label.configure(text="NO2 : " + str(no2Quality), font=("Helverica", 15), background=weather_colour)
        no2Label.grid(row=4, column=0, padx=40, columnspan=2, sticky=W)

    except Exception as e:
        api = "Error..."

# create entry widget for taking user input for city name
# position with grid()
cityEntry = Entry(root)
cityEntry.grid(row=0, column=0, sticky=W+E+N+S)

# create search button that will pass the city name input to through cityLookup function
searchButton = Button(root, text="Lookup City", command=cityLookup)
searchButton.grid(row=0, column=1, sticky=W+E+N+S)

root.mainloop()