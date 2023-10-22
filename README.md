# ADSP 32021 ON01 Machine Learning Operations
# HW#1: Data Versioning & Privacy
### Luke Schwenke, Aaron Chan
### October 23, 2023


### Trouble Shooting Notes
* Use `tensorflow` version 2.13, 2.14 in incompatible with `tensorflow-privacy`
* [PyYAML Issue workaround](https://github.com/yaml/pyyaml/issues/736)

### Switching Data Versions with Git LFS

Assuming your dataset is being tracking using git lfs already.

1. Locate the commit ID of the data version that you want
2. Find the file path
3. Revert the file using: `git checkout [commit ID] -- path/to/file`

Note: Verify the lfs pointer using: `git lfs ls-files`. You may need to run `git lfs pull` to retrieve the data from the lfs server if you have not done so previously.

### Switching Data Versions with lakeFS

Within the lake_fs.ipynb file:

1. Go to the Data Version Switching section after running the previous cells
2. Adjust the commid_ids index value on line 6 with the ref variable to 0 or 1 for v1 (uncleaned) or v2 (cleaned)
3. Run the remaining cells and confirm the dataset version
