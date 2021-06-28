# Movie Recommendation System

### Author: [Wonuola Abimbola](https://github.com/Wonuabimbola)

## Project Goal

This project aims to build a movie recommendation system for a streaming service that offers a wide variety of movies on their platform. They would like to be able to introduce existing users to new movies that they may not have seen before in order to generate more exposure to less popular movies and also recommend movies to new users on the platform using information about the previous movies they've enjoyed and predicting movies similar to them. This project incorporates both Content Based and Collaborative Filtering Methods.  

## Data Understanding

The dataset used in this project was obtained from the latest [MovieLens Dataset.](https://grouplens.org/datasets/movielens/latest/) It contains about 100k user ratings, 9.7k movie and 3.6k movie tags.

## Exploratory Data Analysis

Looking at the frequency distribution of the rating score below. The rating scale ranges from 0.5 to 5.0 with increments of 0.5. The most prevalent ratings given are 3.0, and 4.0 with 5.0 coming in third. We also see that people were less likely to give low ratings as evidenced by the low number of movies rated between 0.5 and 2.5.
![Rating Frequency Distribution](https://github.com/Wonuabimbola/Phase_4_project/blob/master/images/FreqDistRating.png)

Taking a look at the average rating per genre reveals that the genres with the highest average rating were Film-Noir, War and Documentary, although they all had average ratings above 3.0
![Average Rating per Genre](https://github.com/Wonuabimbola/Phase_4_project/blob/master/images/AverageRatingPerGenre.png)

Word cloud showing the most used words in movie titles
We can see that we have quite a few franchises in the dataset as evidenced by the bold lettering of 'II' and 'III'. We also have a lot of movies about 'love' apparently.
![Movie Title Word Cloud](https://github.com/Wonuabimbola/Phase_4_project/blob/master/images/MovieTitleCloud.png)

Word cloud showing the most frequent genres in the dataset
We can see that Drama, Comedy, Thriller, Action and Romance are the most frequently occuring genres in the dataset.
![Genre Word Cloud](https://github.com/Wonuabimbola/Phase_4_project/blob/master/images/GenreCloud.png)

## Content Based Recommendation System

We merged the movies, ratings and tags dataset in order to use it here. After some light preprocessing, we feature engineered a column that took in all of the words mentioned in genres and tags per row (sort of a bag of words column) which we called combined_features

### Concise Steps:
* Count Vectorization of the newly created combined_features column into a matrix of token counts
* Calculation of the Cosine Similarity of the vectorized column 
* When a user enters a movie that they've liked, check for the movies that have the highest cosine similarity to the movie and recommend them to the user to watch

### An example is shown below:
The user entered in Hulk (2003) as a movie that they've seen and liked and our system recommended similar movies to them. The first movie in the list of recommendation is the movie itself which makes sense it would be the most similar to itself.
![Content Based Example](https://github.com/Wonuabimbola/Phase_4_project/blob/master/images/examplecontentbased.png)

## Collaborative Filtering Recommendation System Using 'Surprise' package

After running the following models:
* KNNBasic
* KNNWithMeans
* KNNBaseline
* SVD

The model that resulted in the lowest rmse score was the SVD model. After tuning the hyperparameter values iteratively, the lowest rmse score achieved was ~0.848. The lineplot shows the 'rmse' scores of all the models mentioned above.
![Models VS RMSE Score](https://github.com/Wonuabimbola/Phase_4_project/blob/master/images/modelvsrmse.png)

## Conclusion

* Both models are useful and work hand-in-hand.
* Content based recommendations are straightforward and help with the 'cold start' problem but do not expose the user to new/different type of content.
* Collaborative Filtering helps to expose the user to content they may not have seen before based on users that share similar tastes.
* Recommendation systems get better when it has more information so more data would definitely in the accuracy of the recommendation made. 

# Navigation


```
├── data                                   <- obtained from grouplens.org
│   ├── links.csv                          <- contains identifiers that can be used to link to other sources of movie data
│   ├── movies.md                          <- movie information
|   ├── ratings.csv                        <- movie ratings
│   ├── tags.csv                           <- user-generated metadata about movies
├── images                                 <- Visualizations used in README and pdf file
├── gitignore                              <- files to ignore
├── README.md                              <- This README file
├── contentbasedrec.py                     <- file storing the class used for content based rec
├── movie_lens_rec.ipynb                   <- final notebook
└── movie_rec_system.pdf                   <- final presentation
```

## Contact Information

With questions or feedback on this repository, please reach out via:
- [GitHub](https://github.com/Wonuabimbola)
- [LinkedIn](https://www.linkedin.com/in/wonuola-abimbola)



