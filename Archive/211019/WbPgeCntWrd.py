from Archive import funcTxtAnlytcs as ff
import urllib.request, urllib.parse

wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()

wordfreq = []
# for w in wordlist:
#     wordfreq.append(wordlist.count(w))

# wordfreq = [wordlist.count(w) for w in wordlist]  # a list comprehension
# print("Pairs\n" + str(list(zip(wordlist, wordfreq))))


# html-to-freq.py

url = 'https://www.lens.org/lens/patent/119-821-849-121-092/fulltext'
# url = 'https://www.lens.org/images/patent/US/20190360639/A1/US_2019_0360639_A1.pdf'
# url = 'https://ph.parker.com/dk/da/safety-exhaust-valve-p33-series-pneumatic-division-europe'
print(url)
response = urllib.request.urlopen(url)
# print(ff.printtext(response))
html = response.read()
text = ff.stripTags(html).lower()
print(text)
wordlist = ff.stripNonAlphaNum(text)
fullwordlist = ff.stripNonAlphaNum(text)
wordlist = ff.removeStopwords(fullwordlist, ff.stopwords)
dictionary = ff.wordListToFreqDict(wordlist)
sorteddict = ff.sortFreqDict(dictionary)

# for s in sorteddict: print(str(s))
for s in sorteddict:
    if s[0] >= 3:
        print(str(s))
