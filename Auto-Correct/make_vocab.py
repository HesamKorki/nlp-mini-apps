# %% Libraries
import re
import matplotlib.pyplot as plt

# %% Preprocessing
text = "red pink pink blue blue yellow ORANGE BLUE BLUE PINK"
text = text.lower()
words = re.findall(r'\w+',text)
print(words)
print('count: ', len(words))
# %% Create the Vocabulary
vocab = set(words)
print(vocab)
print('count: ', len(vocab))

word_counts = dict()
for w in words:
    word_counts[w] = word_counts.get(w,0) + 1
print('word_counts: ', word_counts)
# %% Visualize the vocabulary and word frequencies
plt.bar(range(len(word_counts)), list(word_counts.values()), align='center', color=word_counts.keys())
_ = plt.xticks(range(len(word_counts)), list(word_counts.keys()))
# %%
