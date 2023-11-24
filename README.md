# Watch-Next

## Description

This Python script serves as a simple movie recommender system based on natural language processing using the spaCy library.
The script takes a movie description as input and compares it with a list of movies stored in a file (movies.txt). 
It then calculates the similarity between the input description and each movie in the file, ultimately recommending the movie with the highest similarity score.

## Table of Contents
- [Usage](#usage)
- [Credits](#credits)
- [Contact](#contact)
- [License](#license)



# How to Use
Install spaCy:
Make sure you have spaCy installed. If not, you can install it using:

## bash
pip install spacy
Download spaCy Model:
Download a spaCy English model. For example:

## bash
python -m spacy download en_core_web_sm

# Prepare Movie Descriptions:
Edit the movies.txt file with a list of movie descriptions, each on a new line.

# Run the Script:
Execute the script, providing a movie description as an example. The script will output the title of the most similar movie from the provided list.
python watch-next.py

# Example usage
planet_hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

recommended_movie = get_watch_next(planet_hulk_description)

if recommended_movie:
    print("Recommended Movie:", recommended_movie)
else:
    print("No matching movies found.")

# Note
Ensure the movies.txt file contains a variety of movie descriptions for better recommendations.
Adjust the script and spaCy model according to your specific use case or expand its functionalities as needed.

## Credits
This project was created by:

Adriano Mama
GitHub: AdrianoMama
Contact
If you have any questions or feedback regarding this project, feel free to contact the author:

Name: Adriano Mama
Email: adrianoblase99@gmail.com
License
© 2023 Adriano Mama. All rights reserved.
