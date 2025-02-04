import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


df = pd.read_csv('wine.csv')


print(df.isnull().sum()/df.shape[0]*100)
print(df.nunique())

print(df.duplicated().sum())

for i in df.select_dtypes(include="object").columns:
    print(df[i].value_counts())
    print("***"*10)

print(df.describe(include="object").T)

for i in df.select_dtypes(include="number").columns:
    sns.boxplot(data=df , x=i)
    plt.show()

for i in ['country', 'description', 'designation', 'province', 'region_1',      
       'region_2', 'taster_name', 'taster_twitter_handle', 'title', 'variety',
       'winery']:
    sns.scatterplot(data=df, x=i, y='price')
    plt.show()

print(df.select_dtypes(include= "object").columns)
s = df.select_dtypes(include="number").corr()
print(s)
plt.figure(figsize=(15,15))
sns.heatmap(s, annot=True)

for i in ["designation","region_1","region_2","taster_name","taster_twitter_handle","country"]:
    df[i].fillna(df[i].mode()[0], inplace=True)



def handle_rare_categories(df, column, threshold=0.01):
    freq = df[column].value_counts(normalize=True)
    rare_categories = freq[freq < threshold].index
    df[column] = df[column].apply(lambda x: 'Other' if x in rare_categories else x)
    return df

df = handle_rare_categories(df , 'designation', threshold=0.1)

label_encoder = LabelEncoder()
df['designation_encoded'] = label_encoder.fit_transform(df['designation'])


df['region1_encoded'] = label_encoder.fit_transform(df['region_1'])
df['region2_encoded'] = label_encoder.fit_transform(df['region_2'])
df['country_encoded'] = label_encoder.fit_transform(df['country'])
df['taster_name_encoded'] = label_encoder.fit_transform(df['taster_name'])
df['taster_twitter_handle_encoded'] = label_encoder.fit_transform(df['taster_twitter_handle'])

print(df.head())
print(df['country_encoded'])
print(df.info())

print(df.isnull().sum())
print(df.head())

df1 = df.dropna() 


df.drop(["title","description" ,"designation"], axis=1, inplace=True)


print(df.info())
print(df.isnull().sum())
print(df.nunique())
print(df1.info())
df1.reset_index(drop=True)

print(df)

for i in df.columns:
    if df[i].dtypes!= "object":
        df[i].fillna(df[i].median(),inplace=True)
    elif df[i].dtypes == "object":
        df[i].fillna(df[i].mode()[0],inplace=True)
print(df.isnull().sum())
summary = df.describe().T.reset_index()
print(summary)

summary['IQR'] = summary['75%'] - summary['25%']

print(summary['IQR'])

summary['lw'] = summary['25%'] -1.5*summary['IQR']
summary['uw'] = summary['25%'] +1.5*summary['IQR']
summary['skew'] = df.select_dtypes(include='number').T.skew()
summary['kurtosis'] = df.select_dtypes(include='number').T.kurt()
summary['variance'] = summary['std']**2
summary['Range'] = summary['max'] - summary['min']
summary['cv'] = summary['std']/summary['mean']
print(summary)


nul = pd.Series(df.select_dtypes(include='number').isnull().sum(),name="null_values")

print(nul)
  
pd.merge(summary,nul,left_index=True,right_index=True)

pd.set_option("display.max_row", None)

print(df)
