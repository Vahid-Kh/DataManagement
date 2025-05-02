import matplotlib.pyplot as plt
import pandas as pd

# Example data (replace this with your actual data)
data = {
    'word': ['artificial', 'intelligence', 'diabetes', 'type', 'learning', '1'] * 9,  # Example of 54 words
    'count': [20, 16, 14, 9, 8, 8] * 9  # Repeated counts
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Sort data by count in descending order
df = df.sort_values(by='count', ascending=False)

# Select the top 50 words
df_top50 = df.head(50)

# Plot the horizontal bar chart
plt.figure(figsize=(10, 8))
plt.barh(df_top50['word'], df_top50['count'], color='lightcoral')
plt.xlabel('Count')
plt.ylabel('Words')
plt.title('Top 50 Word Count Visualization')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest count at the top
plt.tight_layout()  # Adjust layout
plt.show()
