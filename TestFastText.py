from gensim.models import FastText

# Sample training corpus (tiny for demo)
sentences = [
    ["i", "am", "playing", "football"],
    ["she", "plays", "football"],
    ["he", "played", "basketball"],
    ["they", "are", "playing", "tennis"]
]

# Train FastText model (using subword information)
model = FastText(sentences, vector_size=50, window=3, min_count=1, sg=1)  # sg=1 → skip-gram

# Get embedding for a known word
print("Vector for 'playing':")
print(model.wv["playing"])

# Get embedding for an OOV word — still works due to subwords!
print("\nVector for unseen word 'playingly':")
print(model.wv["playingly"])


import fasttext
model = fasttext.load_model('cc.en.300.bin')