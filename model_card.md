# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

SongFinder

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This is a classroom project that will recommend the user songs based on their own preferences. Using the songs in its database, it will use your preferences on categories such as genre, danceability, bpm, vibe, and more and suggest you similar songs that you may enjoy listening to. 

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The model uses a 7-point scoring system with three categoeis. The first categorie includes genre match, worth 2 points, and mood match, worth 1 point. If a song doesn't match your genre, it starts at a disadvantage. The second categorey includes energy and danceability, each worth up to 1.5 points. In this category, the system rewards songs that are close to your preference. If you like medium energy (0.75), a song with energy 0.76 gets nearly full points, while a song with energy 0.92 gets fewer points because it's farther from your target. This prevents the system from just recommending the highest-energy songs. The last category includes tempo and acousticness, and they add up to 1 point total. Only songs scoring 2.0 or higher are recommended. 

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog contains 18 songs across 10 genres. Each song has 10 attributes: title, artist, genre, mood, energy, tempo (BPM), valence, danceability, and acousticness. Unfortunately, the dataset is tiny compared to real platforms with overrepresented genres, such bas pop and electronic music. The dataset also ignores artist popularity, release date, lyrics, cultural context, and user listening history, which are all crucial for real recommendations. Underrepresented moods like "melancholic" and "aggressive" appear in only 1-2 songs, meaning users seeking those moods get poor recommendations.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works very well for users with clear, popular genre preferences. When I tested the High-Energy Pop lover, "Sunrise City" ranked #1 with a score of 6.62/7.0 because it perfectly matched genre, mood, energy, and danceability—exactly what my intuition predicted. The energy/danceability matching, which rewards closeness rather than extremes, correctly prevents the system from recommending only the highest-energy songs.The system also does good at explaning each reccomendation, whcih includes a breakdown of scoring, helping users understand why a song was suggested.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One bias and limitation the recommender shows is inability to recommend songs accross multiple genres. Because genre matching is very highly weighted, 2 points, users interested in rock music will rarely see other genres of music, such as pop or electronic, even if other factors of the song match their preferences. The system also ignores other features, such as artist poularity, lyrics, cultural context, and listening history. All this combined means that the users are trapped in their preferred genre, missing discoveries in other genres that real platforms actively try to encourage. 

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested the 3 main user profiles, High Energy Pop, Chill Lof, and Deep Intesne Rock. For each prifle, I looked for whether the top recommendations matched the genre and mood. I also looked for cross genre reccomendations, and discovered that high energy lovers tend to see more genre variety compared to low energy lovers. This means that the reccomender favors users with extreme preferences, either very high or very low energy, while middle ground listeners miss discoveries. I ran the disabling mood matching tests, and found that cross genre recommendatiosn dropped to almost nothing. 

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

An additional feature I would like to add is making the points for genre matching less binary, which allows for slightly similar but not the same genre to get a score higher than a flat 0. I would also like to be able to adjust wieghts based on user behavior. If a user keeps skipping songs with high danceability despite having high danceability preference, lower that feature's importance in future recommendations. If they always finish low-energy songs, boost that feature. Let the system learn from what users actually do, not just their stated preferences. Additionally, expanding the song database and including infomration such as artist popularity and country/language, allowing recommendations to be more personalized for the user and their preferences.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this recommender taught me that the most important decision is what to weigh heavily. I chose to weigh genre the heaviest, but this means that this cateogries dominates the system. Using AI tools helped me greatly, but I still had to check them from time to time. Even though the AI could tell me that the test ran perfectly, I still had to go back and check myself because sometimes there would be an error on my end that the AI did not catch. When it was writing code, I still tried my best to understand why and how it was writing it, so I could proofread what I understood. It suprised me that simple algorithm can still "feel" like recommendatison. Even though no personal infomraiton about the user was shared, all the recommendations were still personalized to fit each user. It all seemed very complicated, like recommendations a friend might give you, but it's just an algorithm working in the background. If I had estended this project, I would have tried to connect the project to a larger database to be able to give actual recommendations, and also try to get the algorithm to take in more features of each song into account before giving recommendations. 