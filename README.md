# Simple Weather CLI Reporter

A command-line tool to fetch and display current weather data using the OpenWeatherMap API.

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/hmdfrds/simple-weather-cli
cd simple-weather-cli
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set API key:**

```bash
OPENWEATHER_API_KEY=YOUR-API-KEY
```

replace `YOUR-API-KEY` with your `OpenWeatherMap` API key.

## Usage

Run the script and enter a city name:

```bash
python get_weather.py
```

## Testing

Run unit tests:

```bash
python -m unittest test_get_weather.py
```

## License

MIT
