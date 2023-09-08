# Kimbot

A Seattle Department of Transportation (DOT) Twitter chatbot project that makes traffic tweets fun.

The Let’s Make (Twitter) Friends in Seattlehackathon was hosted by a Institute for Systems Biology.

Most if not all DOT traffic updates are boring and frequently a one-way communication so lacking any user engagement 
long term utilization is low. _demo is deprecated_ [API shutdown](https://sea.mashable.com/tech/24506/twitter-api-changes-crush-possumeveryhour-and-other-good-bots#:~:text=Twitter%27s%20API%20used%20to%20be,switching%20to%20a%20paid%20one.).


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
- The hackathon started on Saturday morning but to me early is ontime, ontime is late and late is unacceptable. As 
  it turns out a dozen other people were asking similar questions and we met up to review the rules and make 
  informal team design choices the day before.
- The problem we wanted to address was how can we increase social media engagement but not be yet another 
  trolling or toxic bot on twitter.
- Our purpose was to find a way to customize boring DOT posts in context of each user preference
- We wanted to show you don't need millions of dollars and dozens of people to rebuild a tool or customize social 
  media experiences.


## Technologies Used
- Twitter API - 2016 version
- AWS EC2 instance
- [tweepy](https://github.com/tweepy/tweepy.github.com) - A python package to scan, sort or ingest tweets.
[![PyPI Version](https://img.shields.io/pypi/v/tweepy?label=PyPI)](https://pypi.org/project/tweepy/)
[![Python Versions](https://img.shields.io/pypi/pyversions/tweepy?label=Python)](https://pypi.org/project/tweepy/)
[![DOI](https://zenodo.org/badge/244025.svg)](https://zenodo.org/badge/latestdoi/244025)

  [![Documentation Status](https://readthedocs.org/projects/tweepy/badge/?version=latest)](https://tweepy.readthedocs.io/en/latest/)
  [![Test Status](https://github.com/tweepy/tweepy/workflows/Test/badge.svg)](https://github.com/tweepy/tweepy/actions?query=workflow%3ATest)
  [![Coverage Status](https://img.shields.io/coveralls/tweepy/tweepy/master.svg?style=flat)](https://coveralls.io/github/tweepy/tweepy?branch=master)
  

- [tweepy](https://github.com/tweepy/tweepy.github.com) - A python package to scan, sort or ingest tweets with 
  ratelimits.
- Python 2.7
- Pycharm
- 2013 MacBookPro 16 MB of ram, 1TB HDD
- Three days of coding


## Features
List the ready features here:
- 13 different replacement tuples
- 13 different replacement options
- Seattle Zip code as standard DOT tweets
- Option for frequency of tweet - in process


## Screenshots
![Example screenshot](/images/Screen Shot 2023-09-07 at 4.39.21 PM.png)


## Setup
1. From your terminal run `pip install -r requirements.txt`
2. Once installed find any other environment variables and load those
3. I use anaconda for all my Python package handling.


## Usage
1. I run this from a terminal inside my Pycharm instance with virtual environment.
2. You will need to enter your Twitter API key in your own .env file at root
3. Setup your own AWS instance and enable access from your IP address
4. This codebase was designed for MacOS and Linux

What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.


## Usage
1. You will need to enter your Twitter API key in your own .env file at root
2. Setup your own AWS instance and enable access from your IP


## Project Status
Project is: _no longer being worked on_. We completed the last work several years ago and since June 2023 Twitter 
has deprecated use of their free API.

Our shared idea was expanded upon in a [2018 Paper](https://www.researchgatenet/publication/317977462_Predicting_TV_programme_audience_by_using_twitter_based_metrics) that was trained 
using crawled data 
from television programs
[<img src="images/v2/Twitter_Kimbot/Twitter-Vigilance-Architecture.png"/>]()

[<img src="images/v2/Twitter_Kimbot/Twitter-Vigilance-Architecture.png" width="250"/>](Twitter-Vigilance-Architecture.png)

What started as an chatbot that would imitate Kim Kardashian stalled out as 82% of her conversation were hair, 
clothes and her butt which were not interesting. 

<img src="images/Screen Shot 2023-09-07 at 4.39.01 PM.png"/>

Since my goal was to both challenge my coding skills with a cool 
concept and to win the Hackathon I had to ask the organizers for advice and collaborate with my team. So over the 
weekend we evolved this 
into a 
hackathon winning 
Markov 
inspired chatbot
trained and hosted on AWS EC2 micro 
instance using publicly available Twitter training data from Silicon Valley and Tweets from Startups and 
@marvelavengers accounts to make traffic alerts more fun.
<img src="images/Screen Shot 2023-09-07 at 4.39.21 PM.png"/>


## Room for Improvement
1. Adding multiple city/state municipalities DOT listings.
2. Enable user option to change from Marvel, Starwars, Startrek, Harry Potter or others.
3. User selectable DOT service in 31 states.
4. User selectable time of day for update.
5. User selectable road choices.
6. Migrate code from 2.7 to 3.x.
7. Rename to DopeyWins.
8. Migrate KimK mentions to prior versioning.
9. Create and integrate a SQL database.
10. Clean up code for multi-environment access.
11. Upgrade code for cloud deployment.
12. Upgrade code for Black[d] linting.
13. Upgrade codebase for user selectable state and DOT districts.


## Acknowledgements
Give credit here.
- Our code was improved by Elizabeth Sutton and @Justin_Devs
- This project was based on [this tutorial](https://www.example.com).
- Many thanks to...


## Contact
Created by [@datatalking](datatalking.github.io) - feel free to contact me!
