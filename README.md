# twitter-relevance-with-pyterrier
This repository contains work for using PyTerrier to index twitter users and find the most relevant users for a given query. All the code from data collection to experimentation is included.

# Requirements
To run the app.py file, PyTerrier is required in addition to the files in the repository

# Trying the Models
1. To run a model we packaged in the ```app.py``` file, navigate to the directory and run the file with ```python app.py```
2. To run the LTR models, run the notebook ```04_Experiments_andLTR``` and run the whole notebook. The last cell has a way for users to test out the models with the data we've collected.

# Running Data Collection
Data collection will require you to have a bearer token to use with Twitter's api. You can enter this in the first cell by setting the variable ```BEARER_TOKEN```
