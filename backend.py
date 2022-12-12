import requests

API_KEY = "c259ab93a74b997e885127c37aa6970b"

# http://api.openweathermap.org/data/2.5/forecast?q=atlanta&appid=c259ab93a74b997e885127c37aa6970b

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    num_values = 8 * forecast_days
    filtered_data = filtered_data[:num_values]

    return filtered_data

if __name__=="__main__":
    print(get_data(place="Atlanta", forecast_days=3))