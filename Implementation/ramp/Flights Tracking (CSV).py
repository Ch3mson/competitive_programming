"""
Given a list of flights which a user has taken, with each flight including userID, departure time, arrival time, departure airport, and arrival airport.

Write a function to return a user's location at a given time.
"""

from datetime import datetime
from collections import defaultdict
from sortedcontainers import SortedList

import bisect
import csv
import unittest

class LocationDetectionApp:
	def __init__(self, file_url: str): 
		self.file_url = file_url
		self.flights = defaultdict(SortedList)
	
	def process_csv(self):
		with open(self.file_url, 'r') as f:
			file_content = csv.reader(f)
			next(file_content) # headers

			for row in file_content:
				user_id, leave, arrive, start, end = row 
				self.flights[user_id].add((datetime.fromisoformat(arrive), end, "In Flight"))
				self.flights[user_id].add((datetime.fromisoformat(leave), "In Flight", start))
	
	def fetch_user_location(self, user_id: str, time: datetime):
		idx = bisect.bisect_right(self.flights[user_id], (time, "", ""))
		return self.flights[user_id][idx-1][1] if idx - 1 >= 0 else self.flights[user_id][idx][2]

class TestLocationDetectionApp(unittest.TestCase):
	def setup(self):
		self.app = LocationDetectionApp("example_flights.csv")
		self.app.process_csv()
	
	def test_fetch_between_cities(self):
		self.setup()
		city = self.app.fetch_user_location("1", datetime(2023, 7, 3))
		assert city == 'LAX'

	def test_before_first_flight(self):
		self.setup()
		city = self.app.fetch_user_location("1", datetime(2023, 6, 3))
		print(city)
		assert city == 'JFK'
	
	def test_after_last_flight(self):
		self.setup()
		city = self.app.fetch_user_location("1", datetime(2023, 8, 3))
		assert city == 'ORD'

	def test_in_flight(self):
		self.setup()
		city = self.app.fetch_user_location("1", datetime.fromisoformat("2023-07-01T09:00:00"))
		assert city == 'In Flight'


if __name__ == "__main__":
	app = LocationDetectionApp("example_flights.csv")
	app.process_csv()
	unittest.main()


