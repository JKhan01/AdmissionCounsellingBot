# importing pandas package 
import pandas as pd 
  
# making data frame from csv file  
data = pd.read_csv("College.csv") 
  
# replacing blank spaces with '_'  
data.columns =[column.replace(" ", "_") for column in data.columns] 
print(data.columns)

# filtering with query method 
sakshi=data.query('Stream =="Arts"') 
  
# display 
print(sakshi)