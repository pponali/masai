import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns


df = pd.read_csv("data/trends_analysis.csv")

os.makedirs("outputs", exist_ok=True)


assending_order = df['score'].sort_values(ascending=False)
top_10_stories = df.loc[assending_order.index].head(10)
top_10_stories['title'] = top_10_stories['title'].str.slice(0,50)

x = top_10_stories['title']
y = top_10_stories['score']

plt.barh(x,  y)
plt.xlabel("Score")
plt.xticks(rotation=90)
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.savefig('outputs/chart1_top_stories.png', bbox_inches='tight')
plt.show()

df['category'].value_counts()

x = df['category'].value_counts().index
y = df['category'].value_counts().values
color = ['lightblue', 'blue', 'purple', 'red', 'black']
plt.barh(x, y,  color=color)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Distribution of Stories by Category")
plt.savefig('outputs/chart2_categories.png', bbox_inches='tight')
plt.show()

yclea = df['score']
x = df['num_comments']

#Colour the dots differently for popular vs non-popular stories (use the is_popular column)
x = df['score']
y = df['num_comments']
colors = df['is_popular'].map({True: 'green', False: 'red'})

plt.scatter(x, y, c=colors, alpha=0.6)
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Number of Comments (Green: Popular, Red: Non Popular)")
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', label='Popular', markerfacecolor='green', markersize=10),
                    plt.Line2D([0], [0], marker='o', color='w', label='Non Popular', markerfacecolor='red', markersize=10)])
plt.savefig('outputs/chart3_scatter.png', bbox_inches='tight')
plt.show()

# Bonus: Dashboard - Combine all 3 charts into one figure
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
# Set a common title for the dashboard
fig.suptitle('TrendPulse Dashboard', fontsize=16, fontweight='bold')

# Chart 1: Top 10 Stories by Score
top_10_stories = df.nlargest(10, 'score').copy()
top_10_stories['title_short'] = top_10_stories['title'].str.slice(0, 50)
axes[0].barh(top_10_stories['title_short'], top_10_stories['score'])
axes[0].set_xlabel('Score')
axes[0].set_ylabel('Story Title')
axes[0].set_title('Top 10 Stories by Score')
axes[0].invert_yaxis()

# Chart 2: Stories per Category
category_counts = df['category'].value_counts()
colors_cat = ['lightblue', 'blue', 'purple', 'red', 'black']
axes[1].bar(category_counts.index, category_counts.values, color=colors_cat[:len(category_counts)])
axes[1].set_xlabel('Category')
axes[1].set_ylabel('Number of Stories')
axes[1].set_title('Distribution of Stories by Category')
axes[1].tick_params(axis='x', rotation=45)

# Chart 3: Score vs Comments
colors_scatter = df['is_popular'].map({True: 'green', False: 'red'})
axes[2].scatter(df['score'], df['num_comments'], c=colors_scatter, alpha=0.6)
axes[2].set_xlabel('Score')
axes[2].set_ylabel('Number of Comments')
axes[2].set_title('Score vs Comments')
axes[2].legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', label='Popular', markerfacecolor='green', markersize=8),
    plt.Line2D([0], [0], marker='o', color='w', label='Non Popular', markerfacecolor='red', markersize=8)
])

plt.tight_layout()
plt.savefig('outputs/dashboard.png', bbox_inches='tight', dpi=300)
plt.show()









