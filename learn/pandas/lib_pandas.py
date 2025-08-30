import pandas as pd
import sqlite3


column = ["Maddy", "Batman", "Sponge"]
titled_column = {"name": column, "height": [1.54, 1.9, 0.25], "weight": [50, 100, 1.3]}

data = pd.DataFrame(titled_column)
#print(data)

selected_data = data["weight"][1]
#print(f"Selected data: \n{selected_data}")

selected_column = data["weight"]
#print(f"Selected columns: \n{selected_column}")

selected_row = data.iloc[1]
#print(f"Selected rows: \n{selected_row}")


#create a new column
bmi = []
for i in range(len(data)):
    bmi_score = data["weight"][i]/(data["height"][i]**2)
    bmi.append(bmi_score)

data["bmi"] = bmi

#print(data)

#data.to_csv("bmi.csv")
#data.to_csv("bmi.csv", index= False, sep="\t")#separated with tab
#data.to_csv("bmi.txt")

data2 = pd.read_csv("bmi.csv", sep="\t")
connection = sqlite3.connect("gta.db")

data_sql = pd.read_sql("select * from gta", connection)
#print(data_sql.head())#only first 5 rows
#print(data_sql.head(2))#only first 2 rows
#print(data_sql.tail(2))#only last 2 rows


filtered_row = data_sql[ data_sql["city"] == "Liberty City" ] #for column city to match CITY and output entire row.

replaced_city = data_sql.replace("Liberty City", "New York")

remove_column = data_sql.drop(["city", "release_year"], axis=1) #axis 1 is column, axis 0 is row , removes multiple columns

remove_row = data_sql.iloc[1:4] #selects only 1,2,3 row




#add new row
row = {"release_year":2021, "release_name": "Natural Vision Evolved", "city": "Los Angels"}

new_row_data = data_sql.append(row, ignore_index=True)



#drop duplicates
jam_data = pd.read.csv("jamData.csv")
jam_data = jam_data.drop_duplicates( subset=["name / nickname (optional)"])


