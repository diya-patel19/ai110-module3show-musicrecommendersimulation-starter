from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read CSV file and return list of song dictionaries with numeric fields converted."""
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    
    songs = []
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate song score (0-7 points) and return reasons for the score."""
    score = 0.0
    reasons = []

    # Tier 1: Categorical Match (0-3 points)
    # Genre match: +2.0
    if song['genre'].lower() == user_prefs.get('genre', '').lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match: +1.0
    if song['mood'].lower() == user_prefs.get('mood', '').lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Tier 2: Sound Profile (0-3 points)
    # Energy similarity: +0.0 to +1.5
    target_energy = user_prefs.get('target_energy', 0.5)
    energy_sim = 1.5 * (1 - abs(song['energy'] - target_energy))
    energy_sim = max(0, energy_sim)
    score += energy_sim
    reasons.append(f"energy similarity (+{energy_sim:.2f})")

    # Danceability similarity: +0.0 to +1.5
    target_danceability = user_prefs.get('target_danceability', 0.5)
    danceability_sim = 1.5 * (1 - abs(song['danceability'] - target_danceability))
    danceability_sim = max(0, danceability_sim)
    score += danceability_sim
    reasons.append(f"danceability similarity (+{danceability_sim:.2f})")

    # Tier 3: Fine-Tuning (0-1 point)
    # Tempo similarity: +0.0 to +0.5 (±40 BPM tolerance)
    target_tempo = user_prefs.get('target_tempo_bpm', 120)
    tempo_sim = 0.5 * max(0, 1 - (abs(song['tempo_bpm'] - target_tempo) / 40))
    score += tempo_sim
    reasons.append(f"tempo similarity (+{tempo_sim:.2f})")

    # Acousticness preference: +0.0 to +0.5
    # Penalizes acoustic songs if user prefers synth (acousticness > 0.40)
    if song['acousticness'] <= 0.40:
        acousticness_sim = 0.5 * (1 - song['acousticness'])
    else:
        acousticness_sim = 0.0
    score += acousticness_sim
    reasons.append(f"acousticness match (+{acousticness_sim:.2f})")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs, filter by threshold (2.0), and return top k sorted by score."""
    recommendations = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
        if score >= 2.0
    ]
    return sorted(recommendations, key=lambda x: (-x[1], x[0]['id']))[:k]
