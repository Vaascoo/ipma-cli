from os.path import join
import requests
import enum

API_URL = "https://api.ipma.pt/open-data"

class IPMA:

    class When(enum.Enum):
        TODAY = 0
        TOMORROW = 1
        AFTER_TOMORROW = 2

    def __init__(self, use_session = False):
        if use_session:
            self.session = requests.session()
        else:
            # work around to avoid verbosity
            self.session = requests

    def list_locations(self):
        url = join(API_URL, "distrits-islands.json")
        response = self.session.get(url)
        assert response.status_code == 200
        return response.json()

    def daily_report(self, when: When = When.TODAY):
        url = join(API_URL, f"forecast/meteorology/cities/daily/hp-daily-forecast-day{when.value}.json")
        response = self.session.get(url)
        assert response.status_code == 200
        return response.json()
