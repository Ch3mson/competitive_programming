"""
Your company runs a personal finance app that helps its users track how
they spend their money. Your goal is to identify recurring subscriptions
users have so that they may cancel unused ones.

You have been provided a CSV file with one user's transactions. Each row
corresponds to one transaction and contains the timestamp the transaction
occurred, formatted as an ISO-8601 string.

Find all recurring charges that happen WEEKLY, then print the merchant,
amount, and interval.

Example output:
OrangeNews: $10.00 / week

API endpoint:
https://assets.ramp.com/interview/recurring_transactions/sample_transactions.txt

Notes:
- One purchase doesn't count as recurring
- Case sensitive merchant names
- Amount must match exactly
"""

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
        """
        Fetch CSV from endpoint and process transactions.

        Requirements:
        1. Fetch the CSV from self.endpoint_url
        2. Parse each row (created_at, merchant, amount, ...)
        3. Group transactions by (merchant, amount) key
        4. Store datetimes in self.subscriptions[(merchant, amount)]

        Hint: Use csv.reader(StringIO(response.text)) to parse
        """
        # TODO: Implement this method
        pass

    def find_subscriptions(self):
        """
        Find all weekly recurring subscriptions.

        Requirements:
        1. For each (merchant, amount) group, check if times are weekly
        2. Skip groups with only 1 transaction
        3. All consecutive transactions must be exactly 1 week apart
        4. Add valid subscriptions to self.valid_subs

        Hint: Compare times[i+1] - times[i] with self.delta
        """
        # TODO: Implement this method
        pass

    def print_weekly_subs(self):
        """Print all valid weekly subscriptions."""
        for merchant, amount in self.valid_subs:
            print(f"{merchant}: ${amount} / weekly")


if __name__ == "__main__":
    app = SubscriptionApp()
    app.process_file()
    app.find_subscriptions()
    app.print_weekly_subs()
