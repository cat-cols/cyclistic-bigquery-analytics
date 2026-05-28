
import geopandas as gpd
import pandas as pd

# Load your GeoJSON file (Census Tract boundaries)
tracts = gpd.read_file('Boundaries - Census Tracts - 2010.geojson')

# Load your bikeshare data (CSV with start_lat and start_lng)
bikeshare_data = pd.read_csv('bikeshare_data.csv')

# Convert bikeshare data to GeoDataFrame with geometry (points)
bikeshare_gdf = gpd.GeoDataFrame(bikeshare_data, geometry=gpd.points_from_xy(bikeshare_data.start_lng, bikeshare_data.start_lat))

# Perform the spatial join (matching points with tracts)
result = gpd.sjoin(bikeshare_gdf, tracts, how="left", op="within")

# Save the result as a CSV to load into Tableau Public
result.to_csv('bikeshare_with_tracts.csv', index=False)

# import geopandas as gpd
# import pandas as pd

# # Load your GeoJSON file (Census Tract boundaries)
# tracts = gpd.read_file('Boundaries - Census Tracts - 2010.geojson')

# # Load your bikeshare data (CSV with start_lat and start_lng)
# bikeshare_data = pd.read_csv('Geo_Hour.csv')

# # Convert bikeshare data to GeoDataFrame with geometry (points)
# bikeshare_gdf = gpd.GeoDataFrame(bikeshare_data, geometry=gpd.points_from_xy(bikeshare_data.start_lng, bikeshare_data.start_lat))

# # Perform the spatial join (matching points with tracts)
# result = gpd.sjoin(bikeshare_gdf, tracts, how="left", op="within")

# # Save the result as a CSV to load into Tableau Public
# result.to_csv('bikeshare_with_tracts.csv', index=False)