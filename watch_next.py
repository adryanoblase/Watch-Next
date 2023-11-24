import spacy

# Define a function to recommend movies based on the input description
def get_watch_next(description):
    # Read the movies.txt file
    with open('movies.txt', 'r') as file:
        movies = file.readlines()

    # Process the input description
    input_doc = nlp(description)

    # Initialize variables to store the most similar movie title and its similarity score
    most_similar_movie = None
    max_similarity_score = 0.0

    # Iterate through each movie description and find the most similar one
    for movie in movies:
        movie_doc = nlp(movie.strip())
        similarity_score = input_doc.similarity(movie_doc)

        # Update if the current movie is more similar
        if similarity_score > max_similarity_score:
            max_similarity_score = similarity_score
            most_similar_movie = movie.strip()

    return most_similar_movie

if __name__ == "__main__":
    # Example usage
    planet_hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

    recommended_movie = get_watch_next(planet_hulk_description)

    if recommended_movie:
        print("Recommended Movie:", recommended_movie)
    else:
        print("No matching movies found.")
