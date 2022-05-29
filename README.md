# Book-recommendation-engine
This is my Microsoft Engage 2022 project on the problem statement of Algorithms for Recommendation Engine/system.

![Python](https://img.shields.io/badge/Python-3.9-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![Frontend](https://img.shields.io/badge/Frontend-HTML/Bootstrap-green)


## Overview

**BookShelf** is a multifunctionality web application which uses ***Popularity-based Recommendation*** to display Top 50 books by using *mean-threshold algorithm* in the `Top 50` section. This application also uses ***Item-item Collaborative filtering***  in the `What's next` section where the user can search a book he/she liked, and the application will recommend top four 'Books you should Read' next similar to the book searched by the user by calculating *similarity scores* with different books based on user ratings & user counts.
      For calculating the similarity scores I'm using `cosine similarity`, to learn more about it follow the Functionality Used section.
      
      
Check out the live demo: https://ac25-47-11-200-121.ngrok.io/
#### Heroku URL: https://book-recommending-app.herokuapp.com/

## How to run the project?

1. Clone or download this repository to your local machine.
2. Install all the libraries mentioned in the [requirements.txt] file with the command `pip install -r requirements.txt`.
3. Generate popular.pkl, books.pkl, similarity_score.pkl and final_rating_df.pkl file by running movie-recommender-engine.ipynb file in jupyter notebook from anaconda navigator and copy this file into the project directory. TO download anaconda follow https://www.anaconda.com/
4. Open your terminal/command prompt from your project directory and run the file `app.py` by executing the command `python app.py`.
5. Go to your browser and type `http://127.0.0.1:5000` in the address bar.
8. Hurray! That's it.


## Functionality Used:

### Mean-Threshold :

It is an algorithm to filter out item based on certain characteristics below a certain threshold and thereafter performing mean over the remaining dataset to get a realistic estimation of its popularity among the userbase. This alogrithm is implemented in the 'Top 50' section of the application to get the Top 50 movies present in the dataset.

### Similarity Score : 

How does it decide which item is most similar to the item user searches? Here come the similarity scores.
   
It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the users acount, ratings & reviews to both the items. So, similarity score is the measure of similarity users acount, ratings & reviews of two items. This can be done by cosine-similarity.
 
 
### How Cosine Similarity works?

Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
  
![image](https://user-images.githubusercontent.com/36665975/70401457-a7530680-1a55-11ea-9158-97d4e8515ca4.png)

  
More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)

### Sources of the datasets

The details of the books(title, author, isbn, genres, poster, user-ratings, user-count, etc) are taken from kaggle datasets, link of which are posted below:
      https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset
### Note: You need to have a kaggle account for accessing the dataset, else create one!
