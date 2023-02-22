import spacy
nlp = spacy.load('en_core_web_md')


# Function to return a movie for the user to watch if they have just watched Planet Hulk
# Based on the similarity between the description of Planet Hulk and the list of movies.
def what_should_I_watch(sample, movie_dict):

    max_sim = 0
    watch_me = ""

    # Iterate over movies in the movie dictionary, comparing the simlarity of the sample description to the
    # description of each movie. 
    # Update the variables for hightest similarity and the corresponding title each time the next movie
    # gets a higher score. 
    for title, descr in movie_dict.items():
        sim = nlp(sample).similarity(nlp(descr))

        if sim > max_sim:
            max_sim = sim
            watch_me = title
    
    return watch_me


# MAIN CODE -----------------------------------------------------------------------------------------

# Open movie text file and store each line in a list.
movies = open("movies.txt", "r")
movie_list = movies.readlines()

# Iterate over movie list and store each title and description in new movie dictionary. 
movie_dict = {}

for movie in movie_list:
    title = movie[0:8]
    descr = movie[9:]
    movie_dict[title] = descr

# Planet Hulk sample description.
sample  = ("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati"
" trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land"
" on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

# Prints out wha movie you should watch based on having watched Planet Hulk. 
print(f"🎥 Based on the movie you just watched, you should now watch: {what_should_I_watch(sample, movie_dict)}! Enjoy!")

    



