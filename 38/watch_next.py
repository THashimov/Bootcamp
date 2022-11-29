import spacy 

nlp = spacy.load('en_core_web_md')

# Open the file and read each line, 
# Compare each line with the description in the argument
# Save the comparison value in a variable along with the movie title
# If the next line has a higher value, overwrite the values
# Once complete, return the movie title
def watch_next(desc) :
    desc = nlp(desc)
    similarity_val = 0
    title = ""

    with open("38/movies.txt", "r", encoding="UTF-8") as file :
        for line in file :
            line = line.split(":")
            movie_desc = nlp(line[1])
            similarity = desc.similarity(movie_desc)
            if similarity > similarity_val :
                similarity_val = similarity
                title = line[0]
        return (title)

desc = "Will he save their world or destroy it? When the hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space where the Hulk can live in peace. Unfortunately, the Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator"

print(watch_next(desc))