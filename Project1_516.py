import nltk
from nltk.book import*

#Exercise 24
list = []
for word in text6:
    if word.endswith("ise") or "z" in word or "pt" in word and word.islower() and word.istitle and word.isalpha():
        list.append(word)

print(list)

#Exercise 25
my_sent = ["she", "sells", "sea", "shells", "by", "the", "sea", "shore"]
for word in my_sent:
    if word.endswith("sh"):
         print(word)

for word in my_sent:
    if word len(word) >= 4:
        print(word)
