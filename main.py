import pandas as pd

p=pd.read_csv("C:\\Users\\IT\\Downloads\\archive (1)\\result.csv") #load the dataset
print(p.head())

# Handling missing values
p.dropna(inplace=True)

# Dealing with duplicates
p.drop_duplicates(inplace=True)

# Data transformation


p['UnEmployeeRate'] = pd.to_numeric(p['UnEmployeeRate'])
p['movieScore'] = pd.to_numeric(p['movieScore'])



# Data filtering (if needed)
p= p[['year','UnEmployeeRate','movieScore']]

print(p)
