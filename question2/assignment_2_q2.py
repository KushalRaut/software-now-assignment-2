import glob
import pandas as pd

# Function to map month to Australian season
def get_season(month):
    if month in [12, 1, 2]:
        return 'Summer'
    elif month in [3, 4, 5]:
        return 'Autumn'
    elif month in [6, 7, 8]:
        return 'Winter'
    elif month in [9, 10, 11]:
        return 'Spring'

# Load all CSV files from the temperatures folder
all_files = glob.glob('temperatures/*.csv')
dfs = []

for file in all_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all dataframes
all_data = pd.concat(dfs, ignore_index=True)

# Convert Date to datetime and extract month
all_data['Date'] = pd.to_datetime(all_data['Date'])
all_data['Month'] = all_data['Date'].dt.month
all_data['Season'] = all_data['Month'].apply(get_season)

# Seasonal Average
seasonal_avg = all_data.groupby('Season')['Temperature'].mean().round(1)

# Save to average_temp.txt
with open('average_temp.txt', 'w') as f:
    for season, avg in seasonal_avg.items():
        f.write(f"{season}: {avg}°C\n")

# Temperature Range
station_max = all_data.groupby('Station')['Temperature'].max()
station_min = all_data.groupby('Station')['Temperature'].min()
station_range = (station_max - station_min).round(1)

max_range = station_range.max()
largest_range_stations = station_range[station_range == max_range].index.tolist()

# Save to largest_temp_range_station.txt
with open('largest_temp_range_station.txt', 'w') as f:
    for station in largest_range_stations:
        max_temp = station_max[station].round(1)
        min_temp = station_min[station].round(1)
        rng = station_range[station]
        f.write(f"{station}: Range {rng}°C (Max: {max_temp}°C, Min: {min_temp}°C)\n")

# Temperature Stability
station_std = all_data.groupby('Station')['Temperature'].std().round(1)

min_std = station_std.min()
max_std = station_std.max()