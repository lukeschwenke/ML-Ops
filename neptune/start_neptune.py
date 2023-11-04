import neptune

# Create a Neptune run object
run = neptune.init_run(
    project = "mlops-uchicago/mlops-hw2",
    # api_token = SET_AS_ENV_PARAM
) 

###########################
### Log Hyperparameters ###
###########################

# Create a metadata field called algorithm and assign the value ConvNet
run["algorithm"] = "ConvNet"

params = {
    "activation": "sigmoid",
    "dropout": 0.25,
    "learning_rate": 0.1,
    "n_epochs": 5,
}

# Create various metadata field of hyperparameters and store
# These will be stored in the parameters namespace under the model namepsace
run["model/parameters"] = params

# Change existing value
run["model/parameters/activation"] = "ReLU" # was sigmoid

# Add new field
run["model/parameters/batch_size"] = 64

###########################
####### Log Metrics #######
###########################

# This creates the namespaces train and eval, each with a loss and acc field.
for epoch in range(params["n_epochs"]):
    # this would normally be your training loop
    run["train/loss"].append(0.99**epoch)
    run["train/acc"].append(1.01**epoch)
    run["eval/loss"].append(0.98**epoch)
    run["eval/acc"].append(1.02**epoch)

###############################
### Track Data File Version ###
###############################

run["data_versions/train"].track_files("athletes.csv")

###############################
############## Stop Run #######
###############################

run["f1_score"] = 0.95
run.stop()