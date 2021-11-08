import nltk
from nltk.book import*
from nltk.corpus import*
emma = nltk.corpus.gutenberg.words('austen-emma.txt')

#Exercise 18

def word_only_bigrams(text, language, number):
    all_bigrams = nltk.bigrams([w.lower() for w in text if w.isalpha()])
    fdist = list(nltk.FreqDist(all_bigrams))
    stopwords = nltk.corpus.stopwords.words(language)
    final_list = []
    for bigram in fdist:
        if bigram[0] not in stopwords:
            if bigram[1] not in stopwords:
                final_list.append(bigram)
    return final_list[:number]

print(word_only_bigrams(emma, "english", 49))

#Exercise 19

cfd = nltk.ConditionalFreqDist(
         (genre, word)
          for genre in brown.categories()
           for word in brown.words(categories=genre))
genres = ["news", "religion", "hobbies", "science_fiction", "romance", "humor"]
ly_conj_adverbs = ["accordingly", "additionally", "certainly", "consequently", "conversely", "definitely", "namely", "naturally", "notably", "similarly"]
cfd.tabulate(conditions=genres, samples=ly_conj_adverbs)