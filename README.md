# 🌤️ Weather App

A sleek desktop weather application built with Python and Tkinter that provides real-time weather information for any city worldwide.

<img src="https://github.com/MohamedZidane11/python-weather-app/blob/main/images/Capture5.PNG" width=850>

## ✨ Features

- **🌡️ Real-time Weather Data**: Get current weather conditions including temperature, humidity, wind speed, and atmospheric pressure
- **🔍 City Search**: Search for weather information in any city around the world
- **🎨 Visual Weather Icons**: Intuitive weather icons that display current conditions (sunny, cloudy, rainy, stormy)
- **📊 Detailed Metrics**: View comprehensive weather data including:
  - Current temperature and "feels like" temperature
  - 💨 Wind speed
  - 💧 Humidity percentage
  - 🌡️ Atmospheric pressure
  - ☁️ Weather description
- **🕐 Time Display**: Shows current local time for the searched location
- **✨ Clean UI**: Modern, user-friendly interface with an attractive color scheme

## 🛠️ Technologies Used

- **🐍 Python**: Core programming language
- **🖥️ Tkinter**: GUI framework for the desktop interface
- **🌐 Requests**: HTTP library for API calls to weather services
- **🗺️ Geopy**: Geocoding library for location services
- **⏰ Timezonefinder**: Library for timezone detection based on coordinates
- **📅 Datetime**: Date and time handling
- **🌍 Pytz**: Timezone calculations and conversions

## 📦 Installation

1. Clone this repository:
```bash
git https://github.com/MohamedZidane11/python-weather-app.git
cd python-weather-app
```

2. Install the required dependencies:
```bash
pip install requests geopy timezonefinder pytz
```

3. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api) (or your preferred weather API provider) 🔑

4. Add your API key to the configuration file or as an environment variable

## 🚀 Usage

1. Run the application:
```bash
python main.py
```

2. Enter a city name in the search box 📍

3. Click the search button or press Enter ⏎

4. View the current weather information displayed in the interface 📱

## 📸 Screenshots

The app displays weather information in an organized layout with:
- 🏙️ City name and current time
- 🌡️ Large temperature display with weather icon
- 📊 Detailed weather metrics in an easy-to-read format

## ⚙️ Requirements

- 🐍 Python 3.13 or higher
- 🌐 Internet connection for API calls
- 📋 All dependencies listed in requirements.txt

## 🔌 API Integration

This application integrates with weather APIs to fetch real-time data. Make sure to:
- 🔑 Sign up for a free API key
- ⚡ Respect API rate limits
- 🛡️ Handle API errors gracefully

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements or bug fixes.

## 📄 License

This project is open source and available under the MIT License.

## 🔮 Future Enhancements

- 📅 5-day weather forecast
- 🚨 Weather alerts and notifications
- ⭐ Favorite cities list
- 🌡️ Temperature unit conversion (Celsius/Fahrenheit)
- 📈 Weather history tracking
