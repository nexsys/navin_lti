import sys

import pandas as pd
import numpy as np
import random

from pprint import pprint

dataset_kraggle = "titles.csv"
datafile_articles = "sample_titles.csv"
datasetF = "dataset.csv"



try:
	df = pd.read_csv(datafile_articles)
except FileNotFoundError as e:
	try:
		df = pd.read_csv(dataset_kraggle, sep="\n") #original dataset 
	except FileNotFoundError as e:
		print("Tip: Plz download dataset from 'https://www.kaggle.com/obismey/wikidata' then rerun this program")
		sys.exit("Error: Required dataset not found... !!!")


	# initial dataset is way to large(>76mb), so taking sample (randomly selecting 1000 articles)
	sdf = df.sample(1000)
	sdf.to_csv("sample_titles.csv", index=False)



# Could not find relevant dataset of users, so generating dummy users and ratings dataset
try:
	usersdf = pd.read_csv(datasetF)
	print("dataset is ready")
	pprint(usersdf.head(10))
except FileNotFoundError as e:
	ratings = random.sample(range(10), 10) # upto 10 rating
	art_df = pd.read_csv(datafile_articles)
	art_id = art_df.index.tolist()
	u = random.sample(range(100), 100) # up to 100 users
	users = [("Navin.lti"+str(item)) for item in u]

	userdf = pd.DataFrame(users, columns=["users"])
	userdf.to_csv("users", index=False)

	# random.choice(ratings), random.choice(art_id)
	dataset = [(users.index(random.choice(users)) , random.choice(ratings), item) for item in art_id]
	df = pd.DataFrame(dataset, columns=["user_id", "article_id", "rating"])
	df.to_csv(datasetF, index=False)

	print(df.head(10))
