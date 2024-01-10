# this is 5th project from this link https://medium.com/@luisprooc/30-data-engineering-project-ideas-9ecf0a70cbea
# in this project I created an ETL data pipeline for an autos data csv file
import pandas as pd
import sqlite3

# convert the csv file into  a dataframe  for more process
autos = pd.read_csv("autos.csv", encoding='Latin-1')

# get the columns names
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
# assign new columns names
autos.columns = custom_column_names

# remove columns that always have only one value
autos.drop(["seller", "offerType", "nrOfPictures"], axis=1, inplace=True)

# this is for finding some of the lowest prices
# print(autos.value_counts("price").sort_index(ascending=True).to_string())

# this is for finding some of the highest prices
# print(autos.value_counts("price").sort_index(ascending=False).to_string())

# remove cars with price lower than 200 dollars
autos = autos[(autos["price"] > 200)]
# next line is for checking that cars with price lower than 200 have been removed(uncomment to see)
# print(autos.value_counts("price").sort_index(ascending=True).head(1000).to_string())


# remove false dates to make the dataset better
# for example it has registration year 1000 (before even cars created) and 9999 (in far future)
for index in autos.index:
    if autos["registration_year"][index] < 1900 or autos["registration_year"][index] > 2024:
        autos.drop(index, inplace=True)

# print(autos["registration_year"].sort_values(ascending=False).head(100))

# create a local db and save the transformed data into it
connection = sqlite3.connect("final_data.db")
cursor = connection.cursor()
# db name , which database to connect , replace if the database was existed , use dataframe index
autos.to_sql("lighter_autos_data", connection, if_exists='replace', index=False)
