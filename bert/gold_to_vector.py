from sentence_transformers import SentenceTransformer
import json


with open("gold_standard_phrases.json") as f:
    mapped_phrases = json.load(f)

phrases = list(mapped_phrases.values())

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(phrases)

list_to_json = []

for annotation, sentence, embedding in zip(list(mapped_phrases.keys()), phrases, embeddings):
    print("Discourse structure:", annotation)
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print("")
    list_to_json.append({"annotation": annotation, "sentence": sentence, "embedding": str(list(embedding))})

with open("gold_standard_embeddings.json", "w") as f2:
    json.dump(list_to_json, f2)
