# importing pandas package 
import pandas as pd 
  
# making data frame from csv file  
data = pd.read_csv("College.csv") 
  
# replacing blank spaces with '_'  
data.columns =[column.replace(" ", "_") for column in data.columns] 
print(data.columns)
pd.options.display.max_colwidth = 200
# filtering with query method
stream = "science" 
percentage = 75.0
location = ["Mumbai",'Pune']
sakshi=data.query(f'Stream =="{stream.capitalize()}" and percentage >= {percentage} and Location == "{location[0]}" ') 

print (sakshi[0:1].college.values[0])
# display 
# for i in range(1,5):
#     print(sakshi[i].college)
print (sakshi.shape)