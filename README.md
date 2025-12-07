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

- Click the Code button in the upper right
- Select Download ZIP
- Extract the folder
- Note: this requires Python 3.8 or later
- Open the terminal and install the needed package (requests) by typing 'pip install requests' on Windows or on Mac 'pip3 install requests' and hitting enter
- In the terminal, check if python is installed by typing 'python3 -—version'. If you see a version like Python 3.x.x its installed, if not download Python from: https://www.python.org/downloads/
- In the terminal type 'cd' then drag the project folder that the file is in into the terminal window. It will auto-fill the correct path and hit enter 
- In the terminal type in a Pokemon to retreive its data using the format 'python main.py <pokemon-name>' or for Mac 'python3 main.py <pokemon-name>'. For example - 'python3 main.py pikachu'
- If the Pokemon does not exist or is spelt wrong it will give the error message 'Pokemon <pokemon-name> not found. Check spelling and try again.'
- To search another Pokemon retype 'python3 main.py <pokemon-name>' replacing the name with the new Pokemon
