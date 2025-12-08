1) Description

- This script acts as a Python command-line tool that pulls a specified Pokémons data (ID, name, height, weight) from the Pokémon API when a Pokemon is named in the terminal.
- To improve performance and reduce API calls, pulled results are stored in a local SQLite database.
- If the same Pokémon is queried more than once, the data is loaded instantly from the database instead of calling the API.
- Ensure the 'usage' steps are followed in section 3 in order to use properly.

2) Features

- Search any Pokémon by name from the terminal.
- Automatically saves responses into a local SQLite database.
- Shows whether the data came from the API or database.

3) Usage - How to run

- Navigate to the Oakland_Task repository page - (https://github.com/JWadeRT/Oakland_Task) and click the green 'Code' button in the upper right. On the drop down select 'Download Zip'.
- From your downloads folder unzip the file.
- Open your terminal and check if python is installed by typing 'python3 -—version' on Mac or 'python --version' on Windows. If you see a version like Python 3.x.x its installed, if not then download Python from: https://www.python.org/downloads/. Note: this requires Python 3.8 or later.
- In the terminal install the needed package 'requests' by typing 'pip install requests' on Windows or 'pip3 install requests' on Mac, and then hitting enter. If this step is missed it will return an error message.
- In the terminal type 'cd ' and then drag the unzipped 'Oakland_Task-master' file into the terminal window. It will auto-fill the correct file path after cd. Hit enter. 
- In the terminal type in a Pokemon to retreive its data using the format 'python main.py _pokemon-name_' on Windows or 'python3 main.py _pokemon-name_' on Mac. **For example - 'python3 main.py pikachu'**. If the wrong format is used this will give an error message. 
- If the Pokemon does not exist or is spelt wrong it will give the error message 'Pokemon <pokemon-name> not found. Check spelling and try again.'
- To search again simply retype 'python3 main.py _pokemon-name_' replacing the name with the Pokemon again as in the example.
