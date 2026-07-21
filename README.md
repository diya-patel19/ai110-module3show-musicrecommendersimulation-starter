# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Real-life recommendations work by combining collabroative filtering and content based filtering. This way, users are able to get reccomendations through both what they specifically like and also what similar users have also liked. In my simulation, year 'Song' will have features such as genre, moood, tempo, and danceability. 'UserProfile' will store information such as most played genres and moods of the user, as well as what songs are most repeated the played so the reccomendations of the simulation can give similar songs that the user might like. 

My recommender will compute a score by first splitting the score into 3 categories, each with different weights. The first category, which has a maximum of 3 points, will determine if the genre (2 points) and the mood (1 point) will match the user's preferences. The second category, which has a maximum of 3 points, will determine if the songs energy and danceability (each 1.5 points) match the users preferences. And the last category, which has a maximum of 1 point, will determine if the tempo and acousticness match as well. A bias that may occur is a lack of genre diversity, only giving the user songs from the few genres that they like. Anothe bais that may occur is that the scoring is very binary, either it matches or it does'nt, so song in the in-between may not be recommended at all.  

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

```
Loading songs from data/songs.csv...

================================================================================
🎵 MUSIC RECOMMENDATIONS FOR YOU
================================================================================
Profile: Pop • Happy • Energy: 0.75
================================================================================

1. SUNRISE CITY
   Artist: Neon Echo • Genre: Pop
   Score: 6.76/7.0
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+1.40), danceability similarity (+1.48), tempo similarity (+0.47), acousticness match (+0.41)

2. GYM HERO
   Artist: Max Pulse • Genre: Pop
   Score: 5.43/7.0
   Why: genre match (+2.0), energy similarity (+1.23), danceability similarity (+1.38), tempo similarity (+0.35), acousticness match (+0.47)

3. ROOFTOP LIGHTS
   Artist: Indigo Parade • Genre: Indie Pop
   Score: 4.73/7.0
   Why: mood match (+1.0), energy similarity (+1.48), danceability similarity (+1.47), tempo similarity (+0.45), acousticness match (+0.33)

4. NIGHT DRIVE LOOP
   Artist: Neon Echo • Genre: Synthwave
   Score: 3.66/7.0
   Why: energy similarity (+1.50), danceability similarity (+1.40), tempo similarity (+0.38), acousticness match (+0.39)

5. HIP HOP FLOW
   Artist: Urban Beats • Genre: Hip Hop
   Score: 3.46/7.0
   Why: energy similarity (+1.46), danceability similarity (+1.48), tempo similarity (+0.15), acousticness match (+0.38)
```

```
# USER 1: High-Energy Pop

================================================================================
🎵 MUSIC RECOMMENDATIONS FOR YOU
================================================================================
Profile: Pop • Happy • Energy: 0.85
================================================================================

1. SUNRISE CITY
   Artist: Neon Echo • Genre: Pop
   Score: 6.62/7.0
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+1.46), danceability similarity (+1.41), tempo similarity (+0.35), acousticness match (+0.41)

2. GYM HERO
   Artist: Max Pulse • Genre: Pop
   Score: 5.78/7.0
   Why: genre match (+2.0), energy similarity (+1.38), danceability similarity (+1.46), tempo similarity (+0.47), acousticness match (+0.47)

3. ROOFTOP LIGHTS
   Artist: Indigo Parade • Genre: Indie Pop
   Score: 4.57/7.0
   Why: mood match (+1.0), energy similarity (+1.36), danceability similarity (+1.46), tempo similarity (+0.42), acousticness match (+0.33)

4. ELECTRIC DREAMS
   Artist: Synthwave Collective • Genre: Electronic
   Score: 3.77/7.0
   Why: energy similarity (+1.46), danceability similarity (+1.50), tempo similarity (+0.38), acousticness match (+0.44)

5. BASS DROP ANTHEM
   Artist: DJ Sonic • Genre: Dance
   Score: 3.71/7.0
   Why: energy similarity (+1.35), danceability similarity (+1.40), tempo similarity (+0.47), acousticness match (+0.49)
```

```
# USER 2: Chill Lofi

================================================================================
🎵 MUSIC RECOMMENDATIONS FOR YOU
================================================================================
Profile: Lofi • Chill • Energy: 0.35
================================================================================

1. LIBRARY RAIN
   Artist: Paper Lanterns • Genre: Lofi
   Score: 6.42/7.0
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+1.50), danceability similarity (+1.46), tempo similarity (+0.46), acousticness match (+0.00)

2. MIDNIGHT CODING
   Artist: LoRoom • Genre: Lofi
   Score: 6.25/7.0
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+1.40), danceability similarity (+1.40), tempo similarity (+0.46), acousticness match (+0.00)

3. FOCUS FLOW
   Artist: LoRoom • Genre: Lofi
   Score: 5.29/7.0
   Why: genre match (+2.0), energy similarity (+1.42), danceability similarity (+1.43), tempo similarity (+0.44), acousticness match (+0.00)

4. SPACEWALK THOUGHTS
   Artist: Orbit Bloom • Genre: Ambient
   Score: 4.00/7.0
   Why: mood match (+1.0), energy similarity (+1.40), danceability similarity (+1.29), tempo similarity (+0.31), acousticness match (+0.00)

5. COFFEE SHOP STORIES
   Artist: Slow Stereo • Genre: Jazz
   Score: 3.27/7.0
   Why: energy similarity (+1.47), danceability similarity (+1.48), tempo similarity (+0.31), acousticness match (+0.00)
```

```
# USER 3: Deep Intense Rock

================================================================================
🎵 MUSIC RECOMMENDATIONS FOR YOU
================================================================================
Profile: Rock • Intense • Energy: 0.9
================================================================================

1. STORM RUNNER
   Artist: Voltline • Genre: Rock
   Score: 6.89/7.0
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+1.48), danceability similarity (+1.48), tempo similarity (+0.47), acousticness match (+0.45)

2. GYM HERO
   Artist: Max Pulse • Genre: Pop
   Score: 4.36/7.0
   Why: mood match (+1.0), energy similarity (+1.46), danceability similarity (+1.16), tempo similarity (+0.28), acousticness match (+0.47)

3. HEAVY METAL THUNDER
   Artist: Iron Fists • Genre: Metal
   Score: 3.58/7.0
   Why: energy similarity (+1.41), danceability similarity (+1.46), tempo similarity (+0.25), acousticness match (+0.46)

4. ELECTRIC DREAMS
   Artist: Synthwave Collective • Genre: Electronic
   Score: 3.48/7.0
   Why: energy similarity (+1.47), danceability similarity (+1.20), tempo similarity (+0.38), acousticness match (+0.44)

5. BASS DROP ANTHEM
   Artist: DJ Sonic • Genre: Dance
   Score: 3.24/7.0
   Why: energy similarity (+1.43), danceability similarity (+1.09), tempo similarity (+0.22), acousticness match (+0.49)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



