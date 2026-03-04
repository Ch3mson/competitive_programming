"""

Given a list of flights which a user has taken, with each flight including userID, departure time, arrival time, departure airport, and arrival airport.

Write a function to return a user's location at a given time.

Follow-up: sort the list of flights based on user, then departure time 

"""

# user id 
# dep time 
# dep airport 
# arrival time
# arrival airport 

# questions:
# what happens if someone is in flight -> return the arrival destination
# is it possible to consider locations before first flgiht and after the last flight 
#   yes -> this is an edge case i have to account for 
# will the time be stored in the smae format? iso format (yes)
# do i need to account for any case sensitivity, or can i assume that it will be accounted for 

# will there every be users with no flights? assume that this is not possible

# cases 
# in flight: return the arrival airport 
# at the airport case: between two consecutive flights 
# edge case: before first flight -> return first departure airport 
# edge case: after last flight -> return last arrival airport 

# approach:

# 1. use a sorted list & store (time, airport) tuples for departure and arrival airports 
#   then use the `bisect` library (or binary search) to find the "index" of a timestamp if we were to theoretically insert it into the array 
#   this represents the location we will be at 

# 2. use a sorted list & store (time, airport) tuples for arrival airports + another hash map for storing the first destination airport (deal with the first flight edge case)
#   if the timestamp provided for a user is less than or equal to the first destination airport, return that (edge case 1 considered)
#   otherwise, use the same approach as above to find its destination (handles in flight and in between airports)
#   if we are inserting it at the end fo the array, we can handle this edge case by checking to make sure the index is in range, otherwise, subtract one (handles edge case 2)

# leaning towards 2 
# reduce the array size by half 
# departure time is irrelevant except for the first case 
# the hash map makes it easy to check times in constant time -> this can reduce time and space significantly for larger datasets 

import bisect
import json
import unittest

from collections import defaultdict
from datetime import datetime
from sortedcontainers import SortedList

class FlightProcessorApp:
	def __init__(self) -> None:
		self.file_url = "flights.json"
		self.user_flights = defaultdict(list)
		self.last_arrivals = {}
	
	def process_json(self):
		with open(self.file_url, 'r') as f:
			file_content = json.load(f)
			assert 'flights' in file_content, 'flights is missing'

			# sorted follow-up:
			new_flights = sorted(file_content['flights'], key=lambda x: (x['userId'], x['depTime']))

			for flight in new_flights:
				user_id, dep_time, arr_time, dep_airport, arr_airport = flight['userId'], datetime.fromisoformat(flight['depTime']), datetime.fromisoformat(flight['arrTime']), flight['depAirport'], flight['arrAirport']
				self.user_flights[user_id].append((dep_time, dep_airport))
				self.last_arrivals[user_id] = (arr_time, arr_airport)
			
	def fetch_user_location(self, user: str, date: str):
		assert user in self.user_flights
		date = datetime.fromisoformat(date)

		if date >= self.user_flights[user][-1][0]: # edge case 1
			return self.last_arrivals[user][1]
		
		idx = bisect.bisect_left(self.user_flights[user], (date, ""))
		return self.user_flights[user][idx][1]
		

class TestFlightProcessorApp(unittest.TestCase):
	def setup(self):
		self.app = FlightProcessorApp()
		self.app.process_json()
	
	def test_before_first_flight(self):
		self.setup()
		assert self.app.fetch_user_location('u3', '2025-08-01T06:45:00+09:00') == 'HND' # at departure time
		assert self.app.fetch_user_location('u3', '2025-07-01T06:45:00+09:00') == 'HND' # before departure time
	
	def test_after_last_flight(self):
		self.setup()
		assert self.app.fetch_user_location('u3', '2025-08-06T14:00:00+01:00') == 'LHR' # at arrival time
		assert self.app.fetch_user_location('u3', '2026-08-06T14:00:00+01:00') == 'LHR' # before departure time
	
	def test_at_airport(self):
		self.setup()
		assert self.app.fetch_user_location('u3', '2025-08-01T10:00:00+09:00') == 'ICN' # between two flights
	
	def test_in_air(self):
		self.setup()
		print(self.app.fetch_user_location('u3', "2025-08-06T13:15:00+01:00"))
		assert self.app.fetch_user_location('u3', "2025-08-06T13:15:00+01:00") == 'LHR' # in the air


if __name__ == "__main__":
	unittest.main()
