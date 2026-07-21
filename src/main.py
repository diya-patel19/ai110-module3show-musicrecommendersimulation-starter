"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Define multiple user profiles - uncomment the one you want to test
    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "target_energy": 0.85,
            "target_danceability": 0.85,
            "target_tempo_bpm": 130,
        },
        "Chill Lofi": {
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
    }

    # Select profile to test (change this to test different profiles)
    user_prefs = profiles["Deep Intense Rock"]

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 80)
    print("🎵 MUSIC RECOMMENDATIONS FOR YOU")
    print("=" * 80)
    print(f"Profile: {user_prefs['genre'].title()} • {user_prefs['mood'].title()} • Energy: {user_prefs['target_energy']}")
    print("=" * 80 + "\n")

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


if __name__ == "__main__":
    main()
