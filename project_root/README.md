# Golf Tournament Scraper

This Python project uses BeautifulSoup and OpenAI to scrape golf tournament results from the provided URL. The script identifies each player and their associated team (college) from the golfstat tournament page, finds the golf course, city, state for the tournament, and uses this information to find the Course Profile on BlueGolf.com using SerpApi. It then extracts the course rating from the BG page and checks if the player has two 18-hole scores from the tournament that add up to (the course rating * 2) + 15 or less. If so, they pass the PAT. The script also uses SerpApi to find the player's Instagram and/or Twitter and/or LinkedIn accounts by searching their name, team/school, and the term "golf". The results are then compiled and printed out as the script runs.

## Installation

1. Clone the repository
2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

Run the main script from the project root:

```bash
python main.py
```

## Files

- `main.py`: The main script that runs the program.
- `requirements.txt`: Contains the required Python packages.
- `setup.py`: The setup script for the project.
- `.gitignore`: Specifies files to be ignored by Git.
- `.vscode/launch.json`: Contains configuration for launching the program in VS Code.
- `src/openai_wrapper.py`: Contains the OpenAIQueryHandler class for interacting with OpenAI.
- `src/extractor.py`: Contains the Extractor class for extracting data from web pages.
- `src/page_scraper.py`: Contains the PageScraper class for scraping web pages.
- `src/serpapi_wrapper.py`: Contains the SerpApiWrapper class for interacting with SerpApi.
- `src/player.py`: Contains the Player class for storing player data.
- `src/course.py`: Contains the Course class for storing course data.
- `src/tournament.py`: Contains the Tournament class for storing tournament data.
- `src/results_compiler.py`: Contains the ResultsCompiler class for compiling the results.
- `src/progress_printer.py`: Contains the ProgressPrinter class for printing progress updates.

## Note

The OpenAI API key is read from environment variables set in the shell. Do not create a `.env` file.