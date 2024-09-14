
# Python Weather API

import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt, QLine


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temparature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox  = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temparature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temparature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temparature_label.setObjectName("temparature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: calibri;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temparature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):

        api_key = "a34e5c4b51db606b824ff2b25ceb9998"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                    case 400:
                        self.display_error("Bad request\nPlease check your input")
                    case 401:
                        self.display_error("Unauthorize\nInvalid API key")
                    case 403:
                        self.display_error("Forbidden\nAccess is denied")
                    case 404:
                        self.display_error("Not Found\nCity not found")
                    case 500:
                        self.display_error("Internal Server Error\nPlease try again later")
                    case 502:
                        self.display_error("Bad Gateway\nInvalid response from the server")
                    case 503:
                        self.display_error("Service Unavailable\nServer is down")
                    case 504:
                        self.display_error("Gateway Timeout\nNo response from the server")
                    case _:
                        self.display_error(f"HTTP error occured\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\n Check your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\n The request timed out")
        except requests.exceptions.ToomanyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")


    def display_error(self, message):
        self.temparature_label.setStyleSheet("font-size: 30px;")
        self.temparature_label.setText(message)

    def display_weather(self, data):
        self.temparature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 259.67
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"]["0"]["description"]



        self.temparature_label.setText(f"{temperature_f:.0f}°F")  # hold alt click 0176 °
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        match weather_id:
            case _ if 200 <= weather_id <= 232:
                return "⛈️"
            case _ if 300 <= weather_id <= 321:
                return "🌦️"
            case _ if 500 <= weather_id <= 531:
                return "🌧️"
            case _ if 600 <= weather_id <= 622:
                return "❄️"
            case _ if 701 <= weather_id <= 741:
                return "💨"
            case _ if 762:
                return "🌋"
            case _ if 771:
                return "☁️"
            case _ if 781:
                return "🌪️"
            case _ if 800:
                return "☀️"
            case _ if 801 <= weather_id <= 804:
                return "☁️"
            case _:
                return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

