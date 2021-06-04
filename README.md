# Movie Recommendation System

### Author: [Wonuola Abimbola](https://github.com/Wonuabimbola)

## Overview

Build a movie recommendation system for a streaming service that offers a wide variety of award-winning movies on their platform. The data used in this project was obtained from the latest MovieLens Dataset.

This project incorporates both Content Based and Collaborative Filtering Methods

## Exploratory Data Analysis

### Looking at the frequency didtribution of the rating score below. The rating scale ranges from 0.5 to 5.0 with increments of 0.5. The most prevalent ratings given are 3.0, and 4.0 with 5.0 coming in third. We also see that people were less likely to give low ratings as evidenced by the low number of movies rated between 0.5 and 2.5.
![Rating Frequency Distribution](https://github.com/Wonuabimbola/Phase_4_project/blob/beta/images/FreqDistRating.png)

### Taking a look at the average rating per genre reveals that the genres with the highest average rating were Film-Noir, War and Documentary, although they all had average ratings above 3.0
![Average Rating per Genre](https://github.com/Wonuabimbola/Phase_4_project/blob/beta/images/AverageRatingPerGenre.png)

### Word cloud showing the most used words in movie titles
We can see that we have quite a few franchises in the dataset as evidenced by the bold lettering of 'II' and 'III'. We also have a lot of movies about 'love' apparently.
![Movie Title Word Cloud](https://github.com/Wonuabimbola/Phase_4_project/blob/beta/images/MovieTitleCloud.png)

### Word cloud showing the most frequent genres in the dataset
We can see that Drama, Comedy, Thriller, Action and Romance are the most frequently occuring genres in the dataset.
![Genre Word Cloud](https://github.com/Wonuabimbola/Phase_4_project/blob/beta/images/GenreCloud.png)

## Content Based Recommendation System

We merged the movies, ratings and tags dataset in order to use it here. After some light preprocessing, we feature engineered a column that took in all of the words mentioned in genres and tags per row (sort of a bag of words column) which we called combined_features

### Concise Steps:
* Count Vectorization of the newly created combined_features column into a matrix of token counts
* Calculation of the Cosine Similarity of the vectorized column 
* When a user enters a movie that they've liked, check for the movies that have the highest cosine similarity to the movie and recommend them to the user to watch

### An example is shown below:
The user entered in Hulk (2003) as a movie that they've seen and liked and our system recommended similar movies to them. The first movie in the list of recommendation is the movie itslef which makes sense it would be the most similar to itself.



