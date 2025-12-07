1) Description

- This script acts as a Python command-line tool that pulls Pokémon data (ID, name, height, weight) using the Pokémon API, when a pokemon is named in the terminal  
- To improve performance and reduce API calls, pulled results are stored in a local SQLite database
- If the same Pokémon is queried again, the data is loaded instantly from the cache instead of calling the API

2) Features

- Search any Pokémon by name from the terminal
- Automatically saves responses into a local SQLite database
- Height is shown in meters
- Weight is shown in kilograms
- Shows whether the data came from the API or database

3) Usage - How to run

- Click the Code button in GitHub
- Select Download ZIP
- Extract the folder and open it in your editor
- Note: this requires Python 3.8 or later
- In the terminal install the needed package (requests) by using - 'pip install requests' and hitting enter
- In the terminal type in a Pokemon to retreive its data using the format 'python main.py <pokemon-name>'. For example - 'python main.py pikachu'
