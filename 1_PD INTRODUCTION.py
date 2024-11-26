# # # What is Pandas?
# Ans: Pandas is a Python library used to working with data sets.It has function for analyzing, clean, exploring and manipulation of data. The name "Pandas" has reference to both "Panel Data" and "Python Data Analysis"

# # # Why use Pandas ?
# Ans : Pandas allow to analize Big data and make conclussion based on statical theories.Pandas can clean messy datasets and make them readable and relevant. Relevant  datasets is verry important in Data Science

# # # What can pandas do ?
# Ans: Pandas gives answers about the data like? 1.Is there a correlation between two or more colums  2.What is average value? 3.Max value? 4. Minumum value

# Pandas are also able to delet row that are not relevant or contains wrong values like empty or Null values.This is called cleaning the data




import pandas as pd
print(pd.__version__)



##############################################################################

# read csv files: (comma seperated file) it is a simple way to store the big and bigest data sets. csv files contains plain text. 
# loading the csv into a dataframe with to_string
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())

# loading the csv into a dataframe without to_string
import pandas as pd
df = pd.read_csv('data.csv')
print(df)

# max_rows : you can check your system's maximum rows with:
import pandas as pd
print(pd.options.display.max_rows)

# yes, we can increase the maximum number of rows to display the entire dataframe.
import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)



###########################################################################################
# JSON: Big data sets are normally stored and extracted as JSON. JSON is a plain text, but it has a format of an object.
# Loading the JSON into a dataframe:
import pandas as pd
sourov = pd.read_json('data.js')
print(sourov.to_string())

# Dictionary as a JSON: if your JSON code is not in a file, but in a python dictionary, then you can do all below:
import pandas as pd
data = {
    "Duration":{
        "0":60,
        "1":60,
        "2":60,
        "3":45,
        "4":45,
        "5":60
        },
    "Pulse":{
        "0":110,
        "1":117,
        "2":103,
        "3":109,
        "4":117,
        "5":102
        },
    "Maxpulse":{
        "0":130,
        "1":145,
        "2":135,
        "3":175,
        "4":148,
        "5":127
        },
    "Calories":{
        "0":409.1,
        "1":479.0,
        "2":340.0,
        "3":282.4,
        "4":406.0,
        "5":300.5
        }        
        }
xnew = pd.DataFrame(data)
print(xnew)


#############################################################################
# cleaning data : it means fixing the bad data in your data set. bad data could be: empty cell, data in a wrong format, duplicate data and wrong data.
# emplty cell: it will give you wrong result always, we will have to remove the rows always that contain the bad data.
# loading and reading the original dataframe
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
print(sourov.to_string())

# here we will return a new data frame with no empty cell.

import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
sourovnew = sourov.dropna()
print(sourovnew.to_string())

# if at any case you want to change the original dataframe, than use the inplace=True argument. it will remove the rows containing the NULL(NaN) values.
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
sourov.dropna(inplace=True)
print(sourov.to_string())

# replacing the empty value: we will use the fillna() method which will allow us to replace the empty cell with a value.
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
sourov.fillna(130, inplace=True)
print(sourov.to_string())

# to replace only the empty value for one column , you need to specify the column name.
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
sourov["Calories"].fillna(130, inplace=True)
print(sourov.to_string())

# here we can also replace the empty cell using mean(), median() or mode().
#calculate the MEAN and replace the empty values with it.
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
x = sourov["Calories"].mean()
sourov["Calories"].fillna(x, inplace=True)
print(sourov.to_string())

# calculate the MEDIAN and replace any empty values in it.:
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
x = sourov["Calories"].median()
sourov["Calories"].fillna(x, inplace=True)
print(sourov.to_string())

# calculate the MODE and replace the empty cell with it.
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
x = sourov["Calories"].mode()[0]
sourov["Calories"].fillna(x, inplace=True)
print(sourov.to_string())

##############################################################################
# Data in a wrong format: to fix this problem, there are 2 ways: removing the rows or convert all the cells in the same format.
# loading and reading the original dataframe
import pandas as pd
x = pd.read_csv('dirtydata.csv')
print(x.to_string())

# now let's try to convert all the cells in the date column into dates.via to_datetime()
import pandas as pd
x = pd.read_csv('dirtydata.csv')
x["Date"] = pd.to_datetime(x['Date'])
print(x.to_string())

# here now we will remove the rows with a NULL value in the 'Date' column.
import pandas as pd
x = pd.read_csv('dirtydata.csv')
x['Date'] = pd.to_datetime(x['Date'])
x.dropna(subset=['Date'], inplace=True)
print(x.to_string())

######################################################################
# removing the duplicate values: 1st you need to discover the duplicate values via duplicated() method.

# loading and reading the original dataframe
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
print(sourov.to_string())

# returns True for every row that is duplicate otherwise return false:
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
print(sourov.duplicated())

# removing the duplicate from the data set. via drop_duplicates()
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
sourov.drop_duplicates(inplace=True)
print(sourov.to_string())
#############################################################
# wrong Data: its only a wrong data

# loading and reading the original dataframe
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
print(sourov.to_string())

# here we will set "Duration" = 45 in row 7:
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
sourov.loc[7,'Duration'] = 45
print(sourov.to_string())

# for larger data set: now here we will loop through all the values in "Duration" column, if the value is higher than 120 than set it to 120.
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
for i in sourov.index:
    if sourov.loc[i, "Duration"] > 120:
        sourov.loc[i, "Duration"] = 120
print(sourov.to_string())

# you can also remove the rows for wrong data in larger dataset.
import pandas as pd
sourov = pd.read_csv('dirtydata.csv')
for i in sourov.index:
    if sourov.loc[i, "Duration"] > 120:
        sourov.drop(i, inplace=True)
print(sourov.to_string())