import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = pd.read_csv('data.csv')
#print(data['Smoking'].dtype)

# Find null data
null_data = data.isnull().sum()
#print(null_data)

# Find duplicate rows
duplicate_rows = data.duplicated()
#print(duplicate_rows)
print(data['HeartDisease'])
data['BMI'] = data['BMI'].astype(int)
data.drop('AgeCategory', axis=1, inplace=True)
replacements = {
    'HeartDisease': {'No': 0, 'Yes': 1},
    'Smoking': {'No': 0, 'Yes': 1},
    'AlcoholDrinking': {'No': 0, 'Yes': 1},
    'Stroke':{'No': 0, 'Yes': 1},
    'DiffWalking':{'No': 0, 'Yes': 1},
    'Sex':{'Female': 0, 'Male': 1},
    'Race':{'White':0, 'Black':1,'or':2,'Asian':3,'Other':4,'Hispanic':5,'American':6,'Yes':7}
}
data.replace(replacements, inplace=True)
data.to_csv('new_data.csv', index=False)








# create a MinMaxScaler object
scaler = MinMaxScaler()

# fit and transform the data
normalized_data = scaler.fit_transform(data)
print("\nNormalized Data")
print(normalized_data)
data.to_csv('preprocessed_data.csv', index=False)

