# INST490-Capstone-Project [![](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)


A program that will analyze a dataset from Spotify’s Billboard Hot 100.

Our project will be able to identify popular genres, artists, and audio metrics that makes a song reach The Hot 100. The project will be able to extract from the selected dataset and visualize it with graphs such as pie charts and bar graphs using spotipy and matplotlib modules in Python. Our project will not be creating our own plotting modules or analyzing songs outside The Hot 100.

![Total Energy Consumption Estimates](jkim1238/INST490-Capstone-Project/blob/main/Total%20Energy%20Consumption%20Estimates.png?raw=true)

## Summary

  - [Scope](#scope)
  - [Project Breakdown and Division of Labor](#project-breakdown-and-division-of-labor)
  - [Meetings and Communication](#meetings-and-communication)
  - [Schedule and Milestones](#schedule-and-milestones)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Running The Tests](#running-the-tests)
  - [Bibliography](#bibliography)
  - [Authors](#authors)

## Scope

Our project will be able to identify popular genres, artists, and audio metrics that makes a song reach The Hot 100. The project will be able to extract from the selected dataset and visualize it with graphs such as pie charts and bar graphs using spotipy and matplotlib modules in Python. Our project will not be creating our own plotting modules or analyzing songs outside The Hot 100.

## Project Breakdown and Division of Labor

The main software components will be scripts that will retrieve the data with spotipy and read data from the .csv file which will plot a graph based on a specific metric (ex. frequency of genre, frequency of artist, frequency of album).

The non-programming task is learning spotipy API and matplotlib modules which will be handled by the researcher.

## Meetings and Communication

Every Saturday evening on Discord or Zoom video call.

## Schedule and Milestones

  - Research spotipy API and matplotlib module
  - Retrieve dataset
  - Program a graph each week
  
## Installation

Besides needing the latest version of Python installed, you will also need to install the matplotlib, spotipy, and pandas Python library. This can be accomplished by running the following code in the terminal you are using:

```
pip install matplotlib
pip install spotipy
pip install pandas
```

## Usage

1. Edit spotify_analysis.py file and add API keys. 
2. Add client ID key as a string on line 30.
3. Add client secret key as a string on line 32.
4. Run program in 2 ways.
5. (1) Run program without arguments.
```
python spotify_analysis.py
```
6. (2) Run program with optional CSV file path argument. (past datasets can be found in /data/ folder)
```
python spotify_analysis.py [-p PATH]
```
7. Enter text menu options.

**Click image for Youtube Presentation/Usage**  
[![INST326 Final Project Presentation Spotify Analysis](readme-files/INST326_Final_Project_Presentation_Spotify_Analysis.gif)](https://www.youtube.com/watch?v=ZD7cg94gz2U)

## Running the Tests

1. Install pytest module:

```
pip install pytest
```

2. Ensure test_spotify_analysis.py, spotify_analysis.py, /data/test.csv is in the same directory.
3. Run pytest.

```
pytest test_spotify_analysis.py
```

<p align="center">
  <img src="https://imgur.com/kj46coA.png" />
</p>

## Bibliography

  - https://www.billboard.com/charts/hot-100
  - https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/

## Authors

  - **Jiin Kim** - *Researcher* -
    [jkim1238](https://github.com/jkim1238)
  - **Nour Fouladi** - *Analyst* -
    [TODO](https://github.com/jkim1238)