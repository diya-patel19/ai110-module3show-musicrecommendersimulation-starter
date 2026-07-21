"""
Test script to run the recommender with multiple user profiles.
Includes normal and adversarial/edge-case profiles.
"""

from src.recommender import load_songs, recommend_songs

# Load songs once
songs = load_songs("data/songs.csv")

# Define test profiles
profiles = {
    "High-Energy Pop Lover": {
        "genre": "pop",
        "mood": "happy",
        "target_energy": 0.85,
        "target_danceability": 0.85,
        "target_tempo_bpm": 130,
    },
    "Chill Lofi Vibes": {
        "genre": "lofi",
        "mood": "chill",
        "target_energy": 0.35,
        "target_danceability": 0.55,
        "target_tempo_bpm": 75,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "target_energy": 0.90,
        "target_danceability": 0.65,
        "target_tempo_bpm": 150,
    },
    "Conflicting Preferences (Energetic + Sad)": {
        "genre": "indie rock",
        "mood": "sad",
        "target_energy": 0.90,
        "target_danceability": 0.75,
        "target_tempo_bpm": 120,
    },
    "Acoustic Synth Contradiction": {
        "genre": "folk",
        "mood": "peaceful",
        "target_energy": 0.30,
        "target_danceability": 0.90,
        "target_tempo_bpm": 100,
    },
    "Rare Genre Enthusiast": {
        "genre": "reggae",
        "mood": "relaxed",
        "target_energy": 0.65,
        "target_danceability": 0.70,
        "target_tempo_bpm": 100,
    },
}

def print_profile_results(profile_name, user_prefs):
    """Run recommender for a profile and print results."""
    print("\n" + "=" * 80)
    print(f"🎵 {profile_name.upper()}")
    print("=" * 80)
    print(f"Profile: {user_prefs['genre'].title()} • {user_prefs['mood'].title()} • "
          f"Energy: {user_prefs['target_energy']} • "
          f"Danceability: {user_prefs['target_danceability']} • "
          f"Tempo: {user_prefs['target_tempo_bpm']} BPM")
    print("=" * 80 + "\n")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    if not recommendations:
        print("No recommendations found matching your preferences.\n")
        return

    for rank, (song, score, explanation) in enumerate(recommendations, 1):
        reasons = explanation.split("; ")
        print(f"{rank}. {song['title'].upper()}")
        print(f"   Artist: {song['artist']} • Genre: {song['genre'].title()}")
        print(f"   Score: {score:.2f}/7.0")
        print(f"   Why: {', '.join(reasons)}")
        print()

# Run all profiles
if __name__ == "__main__":
    for profile_name, user_prefs in profiles.items():
        print_profile_results(profile_name, user_prefs)