# Algorithm Recipe: Music Recommendation Scoring

## Overview
This document describes the scoring logic used to recommend songs to users based on their taste profile. The algorithm uses a **point-based system** that weighs categorical matches (genre, mood) heavily while incorporating numerical feature similarity (energy, danceability, tempo, acousticness).

---

## User Taste Profile (Target User: Upbeat Pop Lover)

```python
user_profile = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.75,
    "target_danceability": 0.80,
    "target_valence": 0.80,
    "target_tempo_bpm": 120,
    "target_acousticness": 0.20,
    "likes_acoustic": False
}
```

---

## Scoring Algorithm

### Tier 1: Categorical Match (Foundation - 7 points max)

**Genre Match: +2.0 points**
- Exact match on `favorite_genre`: +2.0
- No match: +0.0
- Rationale: Genre is the strongest signal for taste. An upbeat pop lover should predominantly get pop recommendations.
- Why 2.0: Strong signal that determines baseline fit

**Mood Match: +1.0 point**
- Exact match on `favorite_mood`: +1.0
- No match: +0.0
- Rationale: Mood reinforces whether a song matches the user's emotional intent
- Why 1.0: Secondary categorical signal (weaker than genre but still critical)

**Categorical Subtotal: 0-3 points**

---

### Tier 2: Energy & Danceability (Sound Profile - 4 points max)

These features capture the "vibe" of a song within a matched genre.

**Energy Similarity: +0.0 to +1.5 points**
- Formula: `1.5 × (1 - |song_energy - target_energy|)`
- User target: 0.75
- Song with energy 0.75: +1.5 points (perfect)
- Song with energy 0.50: +1.5 × (1 - 0.25) = +1.125 points
- Song with energy 0.92: +1.5 × (1 - 0.17) = +1.245 points
- Rationale: Upbeat pop lovers want consistent energy levels; closeness matters more than absolute values
- Why 1.5: Substantial but less critical than genre/mood

**Danceability Similarity: +0.0 to +1.5 points**
- Formula: `1.5 × (1 - |song_danceability - target_danceability|)`
- User target: 0.80
- This user specifically values groove and rhythm
- Rationale: Danceability is core to pop enjoyment
- Why 1.5: Equally important as energy for this profile

**Sound Profile Subtotal: 0-3 points**

---

### Tier 3: Fine-Tuning (Tempo & Acousticness - 1 point max)

**Tempo (BPM) Similarity: +0.0 to +0.5 points**
- Formula: `0.5 × max(0, 1 - (|song_bpm - target_bpm| / 40))`
- User target: 120 BPM
- Song at 120 BPM: +0.5 points
- Song at 100 BPM: +0.5 × (1 - 20/40) = +0.25 points
- Song at 160 BPM: +0.5 × (1 - 40/40) = +0.0 points (outside tolerance)
- Rationale: Tempo tolerance is ±40 BPM for pop (80-160 BPM range)
- Why 0.5: Fine-tuning, not foundation

**Acousticness Preference: +0.0 to +0.5 points**
- User target: 0.20 (prefers electronic/produced, not acoustic)
- Formula: `0.5 × (1 - song_acousticness)` if acousticness <= 0.40
- Song with acousticness 0.05: +0.5 × (1 - 0.05) = +0.475 points (very synth-heavy, excellent)
- Song with acousticness 0.20: +0.5 × (1 - 0.20) = +0.40 points (good)
- Song with acousticness 0.80: +0.0 points (too acoustic, rejected)
- Rationale: Pop fans vary on acoustic preference; penalty for over-acoustic songs
- Why 0.5: Lowest priority, but still tuning

**Fine-Tuning Subtotal: 0-1 point**

---

## Total Score Formula

```
Total Score = Genre Match + Mood Match + Energy Similarity + Danceability Similarity + Tempo Similarity + Acousticness Preference

Score Range: 0.0 to 7.0 points
```

---

## Ranking Rules

### Rule 1: Minimum Threshold
- Only recommend songs scoring **≥ 2.0 points**
- Rationale: Genre match (2.0) is the minimum acceptable; mood can be forgiven, but wrong genre is disqualifying

### Rule 2: Sort by Score (Descending)
- Higher score = Better recommendation
- Ties broken by: Song ID (ascending)

### Rule 3: Return Top K
- Default: Return top 5 recommendations
- Configurable based on user request

---

## Example Calculations

### Example 1: Perfect Match
**Song**: Sunrise City (pop, happy, energy=0.82, danceability=0.79, tempo=118, acousticness=0.18)
- Genre match: +2.0 (pop == pop)
- Mood match: +1.0 (happy == happy)
- Energy: +1.5 × (1 - 0.07) = +1.395
- Danceability: +1.5 × (1 - 0.01) = +1.485
- Tempo: +0.5 × (1 - 2/40) = +0.475
- Acousticness: +0.5 × (1 - 0.18) = +0.41
- **Total: 7.155** ✅ Excellent recommendation

### Example 2: Right Genre, Wrong Mood
**Song**: Gym Hero (pop, intense, energy=0.93, danceability=0.88, tempo=132, acousticness=0.05)
- Genre match: +2.0 (pop == pop)
- Mood match: +0.0 (intense ≠ happy)
- Energy: +1.5 × (1 - 0.18) = +1.23
- Danceability: +1.5 × (1 - 0.08) = +1.38
- Tempo: +0.5 × (1 - 12/40) = +0.35
- Acousticness: +0.5 × (1 - 0.05) = +0.475
- **Total: 6.435** ⚠️ Still strong (genre + energy/danceability make up for mood)

### Example 3: Wrong Genre, Even With Good Audio
**Song**: Storm Runner (rock, intense, energy=0.91, danceability=0.66, tempo=152, acousticness=0.10)
- Genre match: +0.0 (rock ≠ pop)
- Mood match: +0.0 (intense ≠ happy)
- Energy: +1.5 × (1 - 0.16) = +1.26
- Danceability: +1.5 × (1 - 0.14) = +1.29
- Tempo: +0.5 × (1 - 32/40) = +0.1
- Acousticness: +0.5 × (1 - 0.10) = +0.45
- **Total: 3.39** ⚠️ Below strong threshold due to genre mismatch, but above minimum (2.0)

### Example 4: Wrong Everything
**Song**: Midnight Coding (lofi, chill, energy=0.42, danceability=0.62, tempo=78, acousticness=0.71)
- Genre match: +0.0 (lofi ≠ pop)
- Mood match: +0.0 (chill ≠ happy)
- Energy: +1.5 × (1 - 0.33) = +1.005
- Danceability: +1.5 × (1 - 0.18) = +1.23
- Tempo: +0.5 × max(0, 1 - 42/40) = +0.0 (outside tolerance)
- Acousticness: +0.0 (too acoustic, 0.71 > 0.40)
- **Total: 2.235** ⚠️ Barely above threshold; likely won't be in top 5

---

## Design Rationale

### Why This Weighting?

1. **Genre (2.0) > Mood (1.0)**: Users are more specific about genre preferences than mood. An upbeat pop lover might occasionally enjoy intense pop, but rarely wants rock.

2. **Energy & Danceability (1.5 each) > Tempo & Acousticness (0.5 each)**: The first two directly impact how a song *feels*, while the latter are fine-tuning details.

3. **Minimum threshold of 2.0**: Ensures the recommender respects genre preferences while allowing some flexibility within the genre.

4. **Point system over percentages**: Easier to reason about ("this is worth 2 points") and debug than normalized percentages.

---

## Testing Hypotheses

1. **Hypothesis 1**: This profile should strongly prefer pop songs with high danceability (Bass Drop Anthem, Electric Dreams, Gym Hero, Rooftop Lights) over chill lofi or rock.
   - **Test**: Run all 18 songs through the algorithm, verify top 5 are all pop or dance-adjacent.

2. **Hypothesis 2**: Songs with the right genre (pop) but different mood (Gym Hero: intense) should still rank high due to strong energy/danceability match.
   - **Test**: Verify Gym Hero scores above 6.0.

3. **Hypothesis 3**: Genre mismatches (rock, lofi, jazz) should rank below 3.0 even if energy/danceability are good.
   - **Test**: Verify Storm Runner, Midnight Coding score below 3.5.

---

## Future Refinements

- Add a "valence" component for emotional positivity matching
- Implement decay: lower scores for songs the user has already heard
- Add collaborative filtering signal: "other upbeat pop lovers also enjoyed..."
- Genre similarity (e.g., indie pop is closer to pop than rock is)