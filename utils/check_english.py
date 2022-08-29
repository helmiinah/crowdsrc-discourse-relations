import enchant
import pandas as pd
import string
import spacy


d = enchant.Dict("en_US")
model = spacy.load('en_core_web_sm')

def parse(result):
    result = result.lower()
    phrase = "John " + result + " John"
    
    parsed = model(phrase)
    if set([d.check(w) for w in result.split()]) == {True} and len(str(result)) > 1 and set(list(result)) != {"a", "b"}:
        if [t.pos_ for t in parsed if t.pos_ in ['AUX', 'VERB']]:
            return True
        else:
            return False
    else:
        return False


def check_english(result):
    result = result.translate(str.maketrans("", "", string.punctuation))
    if set([d.check(w) for w in result.split()]) == {True} and len(str(result)) > 1 and set(list(result.lower())) != {"a", "b"}:
        return True
    else:
        return False


df = pd.read_csv("description_assignments_08-08-2022.tsv", sep="\t")


df['is_english'] = df.apply(lambda x: parse(x["OUTPUT:result"]), axis=1)

reject = df[df["is_english"] == False]['OUTPUT:result']
accept = df[df["is_english"] == True]['OUTPUT:result']

print(reject)
print(accept)

accept.to_csv("accept_spacy.csv")
reject.to_csv("reject_spacy.csv")