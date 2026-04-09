import pandas as pd
import json

df = None

with open("data/trends_20240115.json","r") as f: 
    data = json.load(f)
    #print(data["all_stories"])
    df = pd.DataFrame(data["all_stories"])

print(f"Loaded {df.shape[0]} stories from data/trends_20240115.json")

#removing the duplicate stories from the dataframe.
df.drop_duplicates(inplace=True)
print(f"After removing duplicates: {df.shape[0]}")


#removing the rows where the title or score or post_id is missing as there are important data points.
df.dropna(subset=["title","post_id","score"], inplace=True)
print(f"After removing nulls: {df.shape[0]}")


#removing the rows whose score is less than 5.
df = df[df['score'] >= 5]
print(f"After removing low scores: {df.shape[0]}")

#removing the trailing and leading spaces from the title of each story.
df['title'] = df['title'].str.strip()

print(f"Saved  {df.shape[0]} rows to data/trends_clean.csv")
print("Stories per category:")
for category in df['category'].unique():
    print(f"{category} {df[df['category'] == category].shape[0]}")


#saving the cleaned dataframe to csv file by excluding the index column from the dataframe.
df.to_csv("data/trends_clean.csv" , index=False)
