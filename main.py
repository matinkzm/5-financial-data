import pandas as pd
import numpy as np

autos = pd.read_csv("autos.csv", encoding='Latin-1')

custom_column_names = autos.columns
custom_column_names = custom_column_names.tolist()

# change some columns names
for i in range(0, len(custom_column_names)):
    if custom_column_names[i] == "yearOfRegistration":
        custom_column_names[i] = "registration_year"
    elif custom_column_names[i] == "monthOfRegistration":
        custom_column_names[i] = "registration_month"
    elif custom_column_names[i] == "notRepairedDamage":
        custom_column_names[i] = "unrepaired_damage"
    elif custom_column_names[i] == "dateCreated":
        custom_column_names[i] = "ad_created"
    else:
        continue

autos.columns = custom_column_names

# remove columns thar always have only one value
autos.drop(["seller", "offerType", "nrOfPictures"], axis=1, inplace=True)

# this is for finding some of the lowest prices
# print(autos.value_counts("price").sort_index(ascending=True).to_string())

# this is for finding some of the highest prices
# print(autos.value_counts("price").sort_index(ascending=False).to_string())

# remove cars with price lower than 200 dollars
autos = autos[(autos["price"] > 200)]
# print(autos.value_counts("price").sort_index(ascending=True).to_string())


# remove false data to make the set better
for index in autos.index:
    if autos["registration_year"][index] < 1900 or autos["registration_year"][index] > 2024:
        autos.drop(index, inplace=True)

# print(autos["registration_year"].sort_values(ascending=False).head(100))
