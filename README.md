# 5-financial-data

this is 5th project from this link: https://medium.com/@luisprooc/30-data-engineering-project-ideas-9ecf0a70cbea

I found the csv data file from this link: https://data.world/data-society/used-cars-data
its a dataset about used cars for sale.

In this ETL project: First i created a dataframe from the csv file , Second change some of the columns names to make it cleaner and mor meaningful , then i removed 3 columns because they always had one value (this help the dataset to become a little lighter) , then i wrote line 32 and 35 to find some of the highest and the lowest peices and removed cars that have price lower than 200 dollars(or euros).

At last for transform part I removed cars with registration year lower than 1900 (the year that cars created) and cars with registration year moer than 2024 (this year)(it makes the dataset lighter and cleaner)

then load it into a local database.

Extract = download and convert the csv file into a dataframe
Transform = change column names , remove redundant rows and columns
Load = load the data into a local datbase