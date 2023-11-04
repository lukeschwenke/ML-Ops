import neptune
import lakefs_client
from lakefs_client import models
from lakefs_client.client import LakeFSClient
import sklearn
from sklearn.model_selection import train_test_split
import pandas as pd

# Initialize Neptune
run = neptune.init_run(
    project="mlops-uchicago/mlops-hw2"
) 

from neptune.integrations.xgboost import NeptuneCallback
neptune_callback = NeptuneCallback(run=run, log_tree=[0, 1, 2, 3])


######################################## lakeFS Data Versioning
# lakeFS credentials and endpoint
configuration = lakefs_client.Configuration()
configuration.username = 'AKIAJ7N3Q7CLFRFGLJ3Q'
configuration.password = '4Qz2msNzhGUwvPUhpcRZQz/vF9hUpEXs5iguekBm'
configuration.host = 'https://cute-cat-6fs7iz.us-east-1.lakefscloud.io'#/repositories/sample-repo/'

# Variables from lakeFS
repo = 'sample-repo'
lake_branch = 'tracking'
commit_ids = ['336e684405152053bb607a31c4240a2490747fee60620e745f76cb6c74523cb7', # UNCLEANED (v1)
              '7edf3e4296bf352581032b687ec1ff4a892a8d056936c83e16f537744b188f55'] # CLEANED (V2)

client = LakeFSClient(configuration)

lakefs_data = client.objects.get_object(
    repository=repo,
    ref=commit_ids[1], # Notes: 0 - UNCLEANED (V1), 1 - CLEANED (V2)
    path='data/athletes.csv')

df = pd.read_csv(lakefs_data)

######################################## Data Prep

# There are Na values in some columns. Fill with 0
df['total_lift'] = df['candj'].fillna(0) + df['snatch'].fillna(0) + df['deadlift'].fillna(0) + df['backsq'].fillna(0)

vars = ['region','gender', 'eat', 'background', 'experience', 'schedule', 'howlong','age','height','weight','candj','snatch','deadlift','backsq']
cats = ['region','gender', 'eat', 'background', 'experience', 'schedule', 'howlong']
numcs = ['age','height','weight']

x = df[numcs].fillna(0) # NAs in numeric columns, fill 0 if any
y = df['total_lift']

# train test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


xgb.train(
    params=model_params,
    dtrain=dtrain,
    callbacks=[neptune_callback],
)

######################################## Models (Linear Regression & Random Forest)
# Step 4: Train a model (You can replace this with your model training code)
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# from sklearn.linear_model import LinearRegression
# import tensorflow as tf
# import random



# # Capture Values for RF
# run["Logs/Parameters"] = ({"n_estimators": 50, "random_state": 42})
# run["Logs/Atributes"] = ({"Dataset": "Athletes.csv", 
#                           "Model": "Random Forest"})

# model = RandomForestClassifier(n_estimators=50, random_state=42)
# model.fit(x_train, y_train)

# y_pred = model.predict(x_test)
# accuracy = accuracy_score(y_test, y_pred)
# run["Accuracy"].append(accuracy)

# model = neptune.init_model(
#     name="Random Forest Model",
#     key="MOD", 
#     project="mlops-uchicago/mlops-hw2", 
#     api_token="eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiIzM2NkNDA2MS01NDVmLTQxNTItODk3Ny1iNDU1MGQxYzhmZmMifQ==", # your credentials
# )

# run.stop()

# Logging relevant information to Neptune - Model #2: Random Forest
# with neptune.start(run=neptune.create_run()):
#     # Log parameters
#     neptune.log_params({"n_estimators": 100, "random_state": 42})
    
#     # Log dataset info
#     neptune.log_text("Dataset", "Athletes dataset")
#     neptune.log_text("Model", "Random Forest")
#     neptune.log_text("Dataset Split", "80% train / 20% test")
    
#     # Log model performance on the test set
#     y_pred = model.predict(x_test)
#     accuracy = accuracy_score(y_test, y_pred)
#     neptune.log_metric("Test Accuracy", accuracy)
    
#     # Log the trained model as an artifact
#     neptune.log_model("random_forest_model", model)

# # Step 6: Close the Neptune run
# # This is optional, but it's a good practice to close the run when you're done.
# neptune.stop()