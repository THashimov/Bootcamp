import spacy

nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("mouse")


print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word1.similarity(word4))

# Spacy can pick out when a word might relate to another word even if they are not the same.
# Cat and mouse have a higher similarity than cat and apple because they are both animals
# Interestingly, cat and mouse are less similar than cat and monkey  
# The words are more similar when using the sm package, however, spacy doesn't like that we aren't using a vector

print("\n\n")

tokens = nlp("cat apple monkey banana")

for token1 in tokens :
    for token2 in tokens :
        print(token1.text, token2.text, token1.similarity(token2))


print("\n\n")


sent_to_comp = "Why is my cat on my car"

sentences = [
                "where did my dog go", 
                "Hello, there is my car",
                "I\'ve lost my car in my car",
                "I\'d like my boat back",
                "I will name my dog Diana"
            ]

sent_to_comp = nlp(sent_to_comp)

for sentence in sentences :
    similarity = nlp(sentence).similarity(sent_to_comp)
    print(f"{sentence} - {similarity}")