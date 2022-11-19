import spacy

nlp = spacy.load("en_core_web_sm")

sentences = [u"The old man the boat", u"The horse raced past the barn fell", u"The prime number few", u"Fat people eat accumulates", u"The man who hunts ducks out on weekends"]

garden_path_sentences = []

for sentence in sentences :
    doc = nlp(sentence)
    garden_path_sentences.append([(ent.text, ent.label_) for ent in doc.ents])

print(garden_path_sentences)

# Spacy only found one entity which was weekends, as DATE
# There isn't anything unusual here