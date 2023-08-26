from setuptools import setup, find_packages

setup(
    name="golf_tournament_scraper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        "requests",
        "openai",
        "tenacity",
        "serpapi"
    ],
    entry_points={
        'console_scripts': [
            'golf_tournament_scraper=main:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python project to scrape golf tournament results and use OpenAI to extract information.",
    keywords="openai beautifulsoup scraper golf",
    url="http://github.com/yourusername/golf_tournament_scraper",   # project home page, if any
)