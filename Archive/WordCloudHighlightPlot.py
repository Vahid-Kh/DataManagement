# Python program to generate WordCloud

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import funcFrqStpWrd as ff

comment_words = ''
stopwords = set(STOPWORDS)

# iterate through the csv file
lt = []

df = pd.read_csv(r"Data/MoistureAcidDirtPurgerRetention.csv", encoding="latin-1")
for val in df.Keywords:

    # typecaste each val to string
    val = str(val)

    # split the value
    tokens = val.split(";")

    # print(tokens)
    #   ###    Converts each token into lowercase
    for i in range(len(tokens)):
        # tokens[i] = tokens[i].lower()
        lt.append(tokens[i])
    comment_words += " ".join(tokens) + " "

wordcloud = WordCloud(width=2500, height=1500, background_color='white', stopwords=ff.stopwords,
                      prefer_horizontal=1, min_font_size=10).generate(comment_words)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)


#We'll create a new list that contains punctuation we wish to clean.
punctuations = ['(',')',';',':','[',']',',','™','/','.']
#We initialize the stopwords variable, which is a list of words like "The," "I," "and," etc. that don't hold much value as keywords.

#We create a list comprehension that only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
wanted =['cascade', 'ammonia', 'CO', 'learning']
keywords = [word for word in lt if not word in ff.stopwords and not word in punctuations]
# print(keywords)
match = [word for word in lt if word in wanted]
# print(match)
dictionary = ff.wordListToFreqDict(keywords)
sorteddict = ff.sortFreqDict(dictionary)

# for s in sorteddict:
#     # if s[0] >= 3:
#         print(str(s))
dictionary = ff.wordListToFreqDict(match)
sorteddict = ff.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))
plt.show()