import kagglehub

# Download latest version
path = kagglehub.dataset_download("insiyeah/musicfeatures")

print("Path to dataset files:", path)