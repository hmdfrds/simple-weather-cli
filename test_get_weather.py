import unittest
from unittest.mock import patch, Mock
import io
import sys
import requests
from get_weather import get_weather

class TestGetWeather(unittest.TestCase):

    @patch('get_weather.requests.get')
    def test_valid_response(self, mock_get):
        expedted_data = {
            "name": "London",
            "main": {
                "temp": 15.0,
                "feels_like": 14.0,
                "humidity": 70,
            },
            "weather": [{
                "description": "clear sky"
            }],
            "wind": {
                "speed": 3.5
            }
        }

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expedted_data
        mock_get.return_value = mock_response

        captured_output = io.StringIO()
        sys.stdout = captured_output

        get_weather("London")

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Weather in London:", output)
        self.assertIn("Temperature: 15.0C", output)
        self.assertIn("Feels Like : 14.0C",output)
        self.assertIn("Description: clear sky", output)
        self.assertIn("Humidity   : 70%",output)
        self.assertIn("Wind Speed : 3.5 m/s", output)

    @patch('get_weather.requests.get')
    def test_city_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        captured_output = io.StringIO()
        sys.stdout = captured_output

        get_weather("NonexistentCity")

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Error: City not found", output)

    @patch('get_weather.requests.get')
    def test_authentication_failed(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 401
        mock_get.return_value = mock_response

        captured_output = io.StringIO()
        sys.stdout = captured_output

        get_weather("London")

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self. assertIn("Error: Authentication failed", output)

    @patch('get_weather.requests.get')
    def test_network_error(self,mock_get):
        mock_get.side_effect =  requests.exceptions.RequestException("Network error")

        captured_output = io.StringIO()
        sys.stdout = captured_output

        get_weather("London")

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Error: Could not retrieve weather data", output)

if __name__ == "__main__":
    unittest.main()