import pandas as pd

# Print all, assigns indexes
#df = pd.read_csv("orders.csv")
#print(df)




#Series: A 1D labeled array (like a column)
#DataFrame: A 2D labeled data structure (like a full spreadsheet or SQL table)

#data = {
#    'Name': ['Alice', 'Bob', 'Charlie'],
#    'Age': [25, 30, 35],
#    'Country': ['USA', 'Canada', 'UK']
#}
#
#df = pd.DataFrame(data)
#print(df)



#loading data frame
#df = pd.read_csv('data.csv')        # Load from CSV
#df = pd.read_excel('data.xlsx')     # Load from Excel
#df = pd.DataFrame(data_dict)        # Load from dictionary, DATA for example


#exploring a dataframe
#df.head()        # First 5 rows
#df.tail()        # Last 5 rows
#df.info()        # Column types and non-null values
#df.describe()    # Summary stats
#df.columns       # Column names
#df.index         # Row indices


#access
#df['Age']                  # Single column, set(df['Age']), len(..)
#df[['Name', 'Age']]        # Multiple columns
#df.iloc[0]                 # First row by position
#df.loc[0]                  # First row by label

#Conditional Filtering (Boolean masks)
#df[df['Age'] > 30]                          # Age over 30
#df[df['Country'] == 'USA']                 # Country match
#df[(df['Age'] > 25) & (df['Country'] == 'UK')]  # Multiple conditions

#Advanced filtering
#df[df['Name'].str.startswith('A')]         # Names starting with A
#df[df['Country'].isin(['USA', 'UK'])]      # Match multiple values
#df[~df['Country'].isin(['Canada'])]        # NOT condition




#CRUD Operations in Pandas
#create (insert rows)
#new_row = pd.DataFrame([{'Name': 'Diana', 'Age': 28, 'Country': 'Germany'}])
#df = pd.concat([df, new_row], ignore_index=True)

#read (access data)
#df.loc[df['Name'] == 'Alice']
#df.iloc[2]


#update modify values
#df.loc[df['Name'] == 'Bob', 'Age'] = 31             # Update Bob's age
#df['Country'] = df['Country'].str.upper()           # Convert all country names to uppercase


#delete (drop data)
#df = df.drop(2, axis=0)                             # Drop row with index 2
#df = df[df['Name'] != 'Alice']                      # Drop rows where name == Alice
#df = df.drop('Age', axis=1)                         # Drop 'Age' column

#cleaning data
#df.isnull().sum()                          # Count missing values
#df.dropna(inplace=True)                   # Drop rows with missing values
#df.fillna({'Age': 0}, inplace=True)       # Fill missing Age values with 0
#df.rename(columns={'Age': 'Years'}, inplace=True)   # Rename column
#df['Years'] = df['Years'].astype(float)   # Convert column to float

#analysing data
#df['Country'].value_counts()                       # Count occurrences
#df.groupby('Country')['Age'].mean()                # Average age per country
#df.sort_values(by='Age', ascending=False)          # Sort by Age descending

#saving data
#df.to_csv('cleaned_data.csv', index=False)
#df.to_excel('output.xlsx', index=False)
