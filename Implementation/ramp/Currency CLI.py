"""
Create a Command-Line Interface (CLI) tool that fetches and prints currency exchange rates for a specified time range. The tool should allow the user to provide the following arguments:

Start Date: The beginning of the date range for fetching exchange rates.
End Date: The end of the date range for fetching exchange rates.
From Currency: The base currency to convert from (e.g., USD).
To Currency: The target currency to convert to (e.g., EUR).
Requirements:

The tool should call a currency exchange rate API to fetch the rates.

GET https://v6.exchangerate-api.com/v6/YOUR-API-KEY/history/USD/YEAR/MONTH/DAY
"""

import requests
import unittest
import argparse



from datetime import datetime, timedelta
class ExchangeRateApp:
	def __init__(self):
		self.api_url = f"https://v6.exchangerate-api.com/v6/{_API_KEY}"
	
	def convert_rates(self):
		while True:
			user_input = input("Indicate start date, end-date, starting currency, desired currency: ")
			start_date, end_date, start_curr, end_curr = user_input.split()

			start, end = datetime.fromisoformat(start_date), datetime.fromisoformat(end_date)
			delta = timedelta(days=1)

			while start <= end:
				response = requests.get(f"{self.api_url}/history/{start_curr}/{start.year}/{start.month}/{start.day}")

				if response.ok:
					print(f"Conversion rate: {response['conversion_rates'][end_curr]}")
				
				start += delta

if __name__ == "__main__":
	app = ExchangeRateApp()
	app.convert_rates()
