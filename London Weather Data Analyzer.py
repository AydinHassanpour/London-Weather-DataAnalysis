import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the API endpoint and parameters
url = 'https://api.open-meteo.com/v1/forecast'
params = {
    'latitude': 51.5074,
    'longitude': -0.1278,
    'hourly': 'temperature_2m',
    'current_weather': 'true',
    'timezone': 'Europe/London',
}

# Send a GET request to the API
response = requests.get(url, params=params)
data = response.json()

# Extract temperature data
temperature_data = data['hourly']['temperature_2m']
current_temperature = temperature_data[-1]  # Use the last entry for current temperature

# Create a DataFrame from the temperature data
weather_data = pd.DataFrame({'Temperature': temperature_data})

# Display basic information about the dataset
print("Basic Information about the Weather Data:")
print(weather_data.info())
print("\nSummary Statistics of Temperature:")
print(weather_data['Temperature'].describe())

# Set style for seaborn plots
sns.set(style="whitegrid")

# Plot the temperature data over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=weather_data, x=weather_data.index, y='Temperature', marker='o', color='b', label='Temperature')
plt.axhline(y=current_temperature, color='r', linestyle='--', label='Current Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature (Celsius)')
plt.title('Temperature Variation in London')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Calculate the average temperature for each month
weather_data['Month'] = pd.to_datetime(weather_data.index).to_period('M')
average_temp_by_month = weather_data.groupby('Month')['Temperature'].mean()

# Plot the average temperature by month
plt.figure(figsize=(10, 6))
sns.barplot(data=average_temp_by_month.reset_index(), x='Month', y='Temperature', color='g')
plt.xlabel('Month')
plt.ylabel('Average Temperature (Celsius)')
plt.title('Average Monthly Temperature in London')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()