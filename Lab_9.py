# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:48:03 2024

@author: oamin
"""

import pandas as pd
import matplotlib.pyplot as plt


# 1. Sales by Region

df = pd.read_csv("Superstore.csv")

region_sales = df.groupby('Region')["Sales"].sum()
print(region_sales)

plt.figure(figsize=(8,8))
plt.pie(region_sales, labels = region_sales.index, autopct = "%1.1f%%",
        startangle = 120, explode = [1,0,1,0])
plt.title("Sales by Region")
plt.show()

# 2. Sales by Category

category_sales = df.groupby('Category')["Sales"].sum()
print(category_sales)

plt.figure(figsize=(10,6))
plt.bar(category_sales.index, category_sales.values, color = "red")
plt.title("Sales by category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()



# 3. Sales over time

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = df.resample("M", on = "Order Date")["Sales"].sum()

plt.figure(figsize = (10,6))
plt.plot(monthly_sales.index, monthly_sales.values)
plt.title("Sales by month")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()


# 3b. Highlight promotion period

promotion_start = '2015-06-01'
promotion_end = '2016-06-01'

plt.figure(figsize = (10,6))
plt.plot(monthly_sales.index, monthly_sales.values)
plt.axvspan(promotion_start, promotion_end, color = "Yellow", alpha = 0.3)
plt.title("Sales by month")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()



# 4. Stacked bar chart based on region

# Filter for selected regions
selected_regions = ['West', 'East']



# 5. Plotting a map using scatterplot

df = pd.read_csv("worldcities.csv")
plt.figure(figsize = (10,6))
plt.scatter(df["lng"], df["lat"], color = "blue", s = 20)
plt.title("City Locatoins")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()




# 6. Plotting map but specifying color for geographic location

colors = ["Blue"] * df.shape[0]

for i in range(df.shape[0]):
    if df["country"][i] == "Canada":
        colors[i] = "Red"
        
plt.figure(figsize = (10,6))
plt.scatter(df["lng"], df["lat"], c = colors, s = 20)
plt.title("City Locatoins")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()





# "Plot the cities on a map, but use different colors for cities in the Northern and Southern Hemispheres. 
# Make cities in the Northern Hemisphere blue and cities in the Southern Hemisphere green."

colors = ["Blue"] * df.shape[0]

for i in range (df.shape[0]):
    if df["lat"][i] > 0:
        colors[i] = "Blue"
    else:
        colors[i] = "Red"
        
plt.figure(figsize = (10,6))
plt.scatter(df["lng"], df["lat"], c = colors, s = 20)
plt.title("City Locatoins")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# Initialize a list to store colors

# Loop through each row to assign color based on hemisphere
  

# Plotting the cities with different colors based on hemisphere

