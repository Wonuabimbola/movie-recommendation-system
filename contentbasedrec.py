class ContentBasedRec:

    #     initialize the class object variables
    def __init__(self,name,df):
        self.name = name
        self.df = df
        self.title = df['title']
        self.index = df['index']
        self.combined_features = df['combined_features']
        
        
    def cosine_sim(self):
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        import pandas as pd
        count_vec = CountVectorizer()
      # convert the contents of the combined features into a matrix of token counts
        count_matrix = count_vec.fit_transform(self.combined_features)
        cosine_sim = pd.DataFrame(cosine_similarity(count_matrix))
        return cosine_sim

        # getting the index of the movie in question
    def title_index(self):
        return self.df[self.title == self.name]["index"].values[0]

    #     getting the index of the movies most similar to the movie selected
    def similar_movies(self):
#         self.cosine_idxcol = self.cosine_sim['index']
        self.title_index()
        similar_movies = list(enumerate(self.cosine_sim()[self.title_index()]))
        return sorted(similar_movies, key=lambda x:x[1], reverse=True)

    #     using the index of the movies to get the movie titles and recommending the first 15 most similar movies
    def movie_list(self):
        movie_list = []
        for movie in self.similar_movies():
            movie_index = movie[0]
            movie_title = self.df[self.index == movie_index]["title"].values[0]
            if movie_title not in movie_list:
                movie_list.append(movie_title)
            else:
                 pass
            if len(movie_list)==15:
                print('Here are a few recommendations for you')
                return movie_list