import kagglehub

# Download latest version
path = kagglehub.dataset_download("bilalabdulmalik/top-300-asian-universities-qs-rankings-2024")

print("Path to dataset files:", path)