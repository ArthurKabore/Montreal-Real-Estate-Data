import pyspark
import numpy as np
import pandas as pd
from pyspark.sql import SparkSession
import logging

logging.basicConfig(level=logging.DEBUG)

pd.options.display.max_rows = 9999

df = pd.read_csv('Outputs/dirty_data.csv', sep='delimiter', header=None, engine='python')

df_arrays = df[0]
clean_list = []

for line in df_arrays:
    line = line.split()
    list_values, city, value, sqft, bath, bed, rooms,  price  = [], "", "", 0, 0, 0, 0, 0

    if "Montréal" in line:
        i = 0
        while line[i][0] != "$":
            i += 1
        price = int(line[i][1:].replace(",", ""))
    else:
        continue
    
    # Sqft of property
    if "sqft" in line:
        size = line.index("sqft")
        sqft = int(line[size - 1].replace(",", ""))

        if len(line[size + 1]) == 4:
            year = line[size + 1]
        else:
            year = 0
    else:
        sqft = 0
        year = 0

    # Room details
    if "bathroom" in line:
        bath = line[line.index("bathroom") - 1]
    elif "bathrooms" in line:
        bath = line[line.index("bathrooms") - 1]
    else:
        bath = 0

    if "bedrooms" in line:
        bed = line[line.index("bedrooms") - 1]
    elif "bedroom" in line:
        bed = line[line.index("bedroom") - 1]
    else:
        bed = 0

    if "rooms" in line and "powder" not in line:
        rooms = line[line.index("rooms") - 1]
    else:
        rooms = 0

    # City 
    if "Montréal" in line:
        value = line[line.index("Montréal") + 1]
        if value == "(Le":
            city = value + line[line.index("Montréal") + 2].replace(",", "")
            city = city[1:-1]
        elif "/" in value:
            city = ""
            i = 1
            while value[i] != "/":
                city += value[i]
                i += 1
        else:
            city = value.replace(")", "")[1:]
            city = value.replace(",", "")[1:-1]
    else:
        city = "None"

    list_values.append(city)
    list_values.append(rooms)
    list_values.append(bed)
    list_values.append(bath)
    list_values.append(price)
    list_values.append(sqft)
    list_values.append(year)
    clean_list.append(list_values)

df = pd.DataFrame(clean_list, columns = ['City', 'Rooms','Bedrooms', 'Bathrooms', 'Price', 'Sqft', 'Year'])

print(df)

#df.to_csv("snow_data.csv", encoding='utf-8', index=False)
