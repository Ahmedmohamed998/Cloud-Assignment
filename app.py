import os
from collections import Counter
import nltk
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "paragraphs.txt")
stop_words = set(nltk.corpus.stopwords.words('english'))
with open(file_path, 'r') as file:
    text = file.read()
words = nltk.word_tokenize(text)
filtered_words = [word for word in words if word.lower() not in stop_words]
filtered_text = ' '.join(filtered_words)
word_counts = Counter(filtered_words)
for word, count in word_counts.items():
    print(f"{word}: {count}")
