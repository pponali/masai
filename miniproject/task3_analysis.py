import pandas as pd
import numpy as np

df = pd.read_csv("data/trends_clean.csv")
print(f"Loaded data:  {df.shape}")
print("First 5 rows:")
print(df.head(5))


print(f"Average score: {df['score'].mean():.2f}")
print(f"Average comments: {df['num_comments'].mean():.2f}")
print("--- NumPy Stats ---")
score_array =np.array(df['score'])
print(f"Mean score: {np.mean(score_array):.2f}")
print(f"Median score: {np.median(score_array)}")
print(f"Std deviation: {np.std(score_array):.2f}")
print(f"Max score: {np.max(score_array)}")
print(f"Min score: {np.min(score_array)}")


#Category distribution on the stories. values counts will give the number of stories for each category.
#from the value counts get the max index for the category name.
#from the value counts get the max value for the category count.


category_counts = df['category'].value_counts()
most_common_category = category_counts.idxmax()
most_common_category_count = category_counts.max()
print(f"Most stories in: {most_common_category} ({most_common_category_count} stories)")    


most_commented_story = df.loc[df['num_comments'].idxmax()]
#print(df.loc[9])
print(f'''Most commented story: "{most_commented_story['title']}"   —  {most_commented_story['num_comments']} comments''')

engagement = np.array(df['num_comments']) / (np.array(df['score']) + 1)

print(engagement)

df['engagement'] = engagement

is_popular = df['score'] > df['score'].mean()
print(is_popular)

df['is_popular'] = is_popular

print(df)

df.to_csv("data/trends_analysis.csv", index = False)