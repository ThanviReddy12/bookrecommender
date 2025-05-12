# Book Recommender System Using Machine Learning

This project aims to build a Book Recommender System using Machine Learning, specifically employing collaborative filtering techniques. The system suggests books based on user preferences, ratings, and interactions. The application is a Streamlit-based web app that allows users to get personalized book recommendations.

## Table of Contents
1.Introduction
2.Types of Recommendation Systems
3.Project Overview
4.Dataset
5.Concept Used
6.How to Run

## Introduction
Recommendation systems are becoming increasingly important in today’s fast-paced world. People often face information overload and are unable to make quick decisions about what to read, watch, or consume. A recommendation system helps alleviate this issue by providing suggestions tailored to a user’s preferences and behavior.
These systems use Artificial Intelligence (AI) algorithms to sift through large datasets and deliver personalized recommendations. They consider user profiles, browsing history, ratings, and even interactions with other users to suggest relevant content.

## Types of Recommendation Systems
1) Content-Based Filtering
Description: This system uses characteristics of items and user profiles. For example, based on the type of content you previously liked (like music or books), the system will recommend similar items.
Example: YouTube and Twitter use content-based systems.
Problem: May lead to overly narrow recommendations due to excessive specialization.

2) Collaborative Filtering
Description: Collaborative filtering is based on user-item interactions. It identifies patterns between users who share similar preferences. If a user likes a particular book, the system suggests books liked by other similar users.
Example: Book recommendation systems.
Problem: Computationally expensive, new items might not get recommended.

3) Hybrid Systems
Description: Hybrid systems combine both content-based and collaborative filtering methods to mitigate the limitations of each.
Example: Uses algorithms like Word2Vec and embedding for better recommendations.

## Project Overview
This is a Streamlit web application that recommends books based on user ratings and preferences. The system uses the Nearest Neighbors algorithm to identify books that are similar to the ones the user has liked. The web app allows users to input their interests and receive personalized book suggestions.


## Dataset
The dataset used in this project is sourced from Kaggle and includes three main CSV files:
BX-Books.csv: Contains information about books, including title, author, publisher, and URLs for book images.
BX-Users.csv: Contains user information such as user ID, location, and age.
BX-Book-Ratings.csv: Contains ratings given by users to books, with the user ID, ISBN of the book, and the rating provided.


## Concept Used: Nearest Neighbors Algorithm
The model utilizes the Nearest Neighbors algorithm from scikit-learn to calculate the similarity between books based on user ratings and other features.
Workflow:
Load the Dataset: Import the book ratings and features dataset for analysis.
Initialize the Value of k: Define the number of neighbors (k) to consider when making recommendations.
Calculate the Distance: Compute the Euclidean distance (or another suitable distance metric) between the test data point (the target book or user) and the training data points (other books or users).
Sort the Distances: Sort the distances in ascending order and select the top k nearest neighbors.
Return Book Recommendations: Based on the top k neighbors, recommend books that are most similar to the test data (target book/user).

## How to run 
