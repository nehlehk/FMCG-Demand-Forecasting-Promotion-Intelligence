import kagglehub

# Download latest version
path = kagglehub.competition_download('favorita-grocery-sales-forecasting', output_dir="data/raw")

print("Path to competition files:", path)