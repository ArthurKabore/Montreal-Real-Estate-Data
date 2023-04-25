import pyspark
import numpy as np
import pandas as pd
from pyspark.sql import SparkSession

pd.options.display.max_rows = 9999

df = pd.read_csv('Outputs/dirty_data.csv', sep='delimiter', header=None, engine='python')

df_arrays = df[0]
clean_list = []

for line in df_arrays:
    line = line.split()
    list_values = []
    city = ""
    price = ""
    bath = ""
    bed = ""
    rooms = ""
    value = ""
    sqft = ""

    if "Montréal" in line:
        i = 0
        while line[i][0] != "$":
            i += 1
        price = line[i][1:]
    else:
        continue
    
    # Sqft of property
    if "sqft" in line:
        size = line.index("sqft")

        sqft = line[size - 1]

        if len(line[size + 1]) == 4:
            year = line[size + 1]
        else:
            year = "None"
    else:
        sqft = "None"
        year = "None"

    # Room details
    if "bathroom" in line:
        bath = line[line.index("bathroom") - 1]
    elif "bathrooms" in line:
        bath = line[line.index("bathrooms") - 1]
    else:
        bath = "None"

    if "bedrooms" in line:
        bed = line[line.index("bedrooms") - 1]
    elif "bedroom" in line:
        bed = line[line.index("bedroom") - 1]
    else:
        bed = "None"

    if "rooms" in line:
        rooms = line[line.index("rooms") - 1]
    else:
        rooms = "None"

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
    list_values.append(year)
    clean_list.append(list_values)

df = pd.DataFrame(clean_list, columns = ['City', 'Rooms','Bedrooms', 'Bathrooms', 'Price', 'Year'])
print(df)


df.to_csv("clean_summary_df.csv", encoding='utf-8')

with open("clean_summary.csv", "a", encoding='utf-8') as txt_file:
    for line in clean_list:
        txt_file.write(" ".join(line) + "\n")
