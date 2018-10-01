import sys
import pandas as pd
import numpy as np
import random

from pprint import pprint

from sklearn.metrics.pairwise import pairwise_distances 



datasetF = "dataset.csv"


df = None
try:
	df = pd.read_csv(datasetF)
except FileNotFoundError as e:
	print("Tip: First run dataset.py to generate dataset, then rerun this program")
	sys.exit("Error: Required dataset not found... !!!")



n_users = df.user_id.unique().shape[0]
n_items = df.article_id.unique().shape[0]

# pprint(df)

data_matrix = np.zeros((n_users, n_items))

for line in df.itertuples():
	# print(data_matrix[line[2]-1, line[3]-1])
	data_matrix[line[1]-1, line[2]-1] = line[3]

	# print(data_matrix)

user_similarity = pairwise_distances(data_matrix, metric='cosine')
item_similarity = pairwise_distances(data_matrix.T, metric='cosine')

print(user_similarity)


def recommend(ratings_matrix, similarity, rtype='user'):
	pred = None
	if rtype == 'user':
		mean_user_rating = ratings_matrix.mean(axis=1)
		ratings_diff = (ratings_matrix - mean_user_rating[:, np.newaxis])
		
		pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff)/np.array([np.abs(similarity).sum(axis=1)]).T

	elif rtype == 'item':
		pred = ratings_matrix.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])

	return pred



user_based_recommendation = recommend(data_matrix, user_similarity, rtype='user')
article_based_recommendation = recommend(data_matrix, item_similarity, rtype='item')

# article_id =  input("Article ID")
# similar_articles = []
# if __name__ == '__main__':
	