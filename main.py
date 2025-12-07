import requests
import json
import sys
import sqlite3

DB_NAME = "pokemon_cache.db"


def init_db():
    """Create database and table if not exists."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Store as REAL to allow decimal values
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            height REAL,
            weight REAL
        )
    """)

    conn.commit()
    conn.close()


def get_pokemon_from_db(name):
    """Try to get Pokemon from local database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemon WHERE name = ?", (name.lower(),))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "id": row[0],
            "name": row[1],
            "height": row[2],
            "weight": row[3],
        }
    return None


def save_pokemon_to_db(pokemon_data):
    """Save fetched Pokemon to local database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO pokemon (id, name, height, weight)
        VALUES (?, ?, ?, ?)
    """, (
        pokemon_data["id"],
        pokemon_data["name"].lower(),
        pokemon_data["height"],
        pokemon_data["weight"]
    ))
    conn.commit()
    conn.close()


def get_pokemon_info(name):
    """Fetch Pokemon either from DB or API."""
    cached = get_pokemon_from_db(name)
    if cached:
        print("[CACHE HIT] Returning saved data from database.")
        return cached

    # Fetch from API
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Pokemon '{name}' not found. Check spelling and try again.")
        return None

    data = response.json()

    # Convert height to m & weight to kg
    height_m = data["height"] / 10
    weight_kg = data["weight"] / 10

    result = {
        "id": data["id"],
        "name": data["name"],
        "height": height_m,
        "weight": weight_kg,

    }

    save_pokemon_to_db(result)
    print("[API CALL] Saved new data to database.")
    return result


if __name__ == "__main__":
    init_db()

    if len(sys.argv) < 2:
        print("Usage: Use the following format in the terminal to pull pokemon data - python main.py <pokemon-name>")
        sys.exit(1)

    pokemon_name = sys.argv[1]
    result = get_pokemon_info(pokemon_name)

    if result:
        # Add units for display only
        result_display = result.copy()
        result_display["height"] = f"{result['height']:.1f} m"
        result_display["weight"] = f"{result['weight']:.1f} kg"
        print(json.dumps(result_display, indent=4))
