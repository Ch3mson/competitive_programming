"""
Given a list of flights which a user has taken, with each flight including
userID, departure time, arrival time, departure airport, and arrival airport.

Write a function to return a user's location at a given time.

Follow-up: sort the list of flights based on user, then departure time

Edge cases to consider:
- In flight: return the arrival airport
- At airport: between two consecutive flights
- Before first flight: return first departure airport
- After last flight: return last arrival airport
"""

import bisect
import json
import unittest

from collections import defaultdict
from datetime import datetime

class FlightProcessorApp:
    def __init__(self) -> None:
        self.file_url = "flights.json"
        self.user_flights = defaultdict(list)
        self.last_arrivals = {}

    def process_json(self):
        """
        Read flights.json and process the data.

        Requirements:
        1. Sort flights by (userId, depTime)
        2. For each flight, store (dep_time, dep_airport) in user_flights[user_id]
        3. Track the last arrival for each user in last_arrivals

        Hint: Use sorted() with a lambda key
        """
        # TODO: Implement this method
        pass

    def fetch_user_location(self, user: str, date: str):
        """
        Return the user's location at the given date/time.

        Requirements:
        1. If date >= last departure time, return last arrival airport
        2. Otherwise, use bisect to find the correct location

        Hint: bisect.bisect_left finds insertion point
        """
        # TODO: Implement this method
        pass


class TestFlightProcessorApp(unittest.TestCase):
    def setup(self):
        self.app = FlightProcessorApp()
        self.app.process_json()

    def test_before_first_flight(self):
        self.setup()
        assert self.app.fetch_user_location('u3', '2025-08-01T06:45:00+09:00') == 'HND'
        assert self.app.fetch_user_location('u3', '2025-07-01T06:45:00+09:00') == 'HND'

    def test_after_last_flight(self):
        self.setup()
        assert self.app.fetch_user_location('u3', '2025-08-06T14:00:00+01:00') == 'LHR'
        assert self.app.fetch_user_location('u3', '2026-08-06T14:00:00+01:00') == 'LHR'

    def test_at_airport(self):
        self.setup()
        assert self.app.fetch_user_location('u3', '2025-08-01T10:00:00+09:00') == 'ICN'

    def test_in_air(self):
        self.setup()
        assert self.app.fetch_user_location('u3', "2025-08-06T13:15:00+01:00") == 'LHR'


if __name__ == "__main__":
    unittest.main()
