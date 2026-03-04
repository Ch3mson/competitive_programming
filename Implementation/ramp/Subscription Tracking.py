"""
Your company runs a personal finance app that helps its users track how they spend their money. Your goal is to identify recurring subscriptions users have so that they may cancel unused ones.

You have been provided a CSV file with one user's transactions. Each row corresponds to one transaction and contains
the timestamp the transaction occurred, formatted as an ISO-8601 string. Find all recurring charges that happen WEEKLY,
then print the merchant, amount, and interval.

Example output:
OrangeNews: $10.00 / week

import csv  
from collections import defaultdict  
import datetime  
transaction_data = requests.get("https://assets.ramp.com/interview/recurring_transactions/sample_transactions.txt")
"""

"""
Your company runs a personal finance app that helps its users track how they spend their money. Your goal is to identify recurring subscriptions users have so that they may cancel unused ones.

You have been provided a CSV file with one user's transactions. Each row corresponds to one transaction and contains
the timestamp the transaction occurred, formatted as an ISO-8601 string. Find all recurring charges that happen WEEKLY,
then print the merchant, amount, and interval.

Example output:
OrangeNews: $10.00 / week
transaction_data = requests.get("https://assets.ramp.com/interview/recurring_transactions/sample_transactions.txt")
"""

# 1. read the csv 
# 2. read each row and categorize dates by the transaction (hash) 
#     key: merchant, amount
#    value: list of dates 
# 3. use sorted list to add the element into the existing list & compare with its neighbours 
# 4. if both are weekly, then we can continue on assuming this is a valid subscription

# datetime class -> timedelta (weeks=1) use this to find the difference between different dates 
# for each subscription, we will add the dates to a list and then sort it, and then we check the neighbours to ensure they are all 1 week apart 
#    if they are one week apart for all of them, add them to a subscriptions array 

# one purchase doesn't count 
# case sensitive 
# currency is the same 
# amount has to be the same 

from collections import defaultdict
from datetime import datetime, timedelta
from http import HTTPStatus
from io import StringIO
from sortedcontainers import SortedList

import requests
import csv

class SubscriptionApp:
	def __init__(self) -> None:
		self.subscriptions = defaultdict(SortedList)
		self.valid_subs = set()
		self.delta = timedelta(weeks=1)
		self.endpoint_url = "https://assets.ramp.com/interview/recurring_transactions/sample_transactions.txt"

	def process_file(self):
		response = requests.get(self.endpoint_url)

		if response.status_code == HTTPStatus.OK:
			file_content = csv.reader(StringIO(response.text))
			next(file_content)

			for row in file_content:
				created_at, merchant, amount, _ = row
				self.subscriptions[(merchant, amount)].add(datetime.fromisoformat(created_at))

	def find_subscriptions(self):
		for (merchant, amount), times in self.subscriptions.items():
			if len(times) <= 1:
				continue 
				
			isSub = True

			for i in range(len(times) - 1):
				if times[i + 1] - times[i] != self.delta:
					isSub = False
					break 
			
			if isSub:
				self.valid_subs.add((merchant, amount))
	
	def print_weekly_subs(self):
		for merchant, amount in self.valid_subs:
			print(f"{merchant}: ${amount} / weekly")
				

if __name__ == "__main__":
	app = SubscriptionApp()
	app.process_file()
	app.find_subscriptions()
	app.print_weekly_subs()
