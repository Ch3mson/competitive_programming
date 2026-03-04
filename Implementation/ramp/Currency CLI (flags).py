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

import asyncio
import httpx
import argparse
from http import HTTPStatus
from tabulate import tabulate



from datetime import datetime, timedelta
class ExchangeRateApp:
	def __init__(self, start_time: str, end_time: str, start_curr: str, end_curr: str):
		self.start_time = datetime.fromisoformat(start_time)
		self.end_time = datetime.fromisoformat(end_time)
		self.delta = timedelta(days=1)
		self.times = []

		while self.start_time <= self.end_time:
			self.times.append(self.start_time)
			self.start_time += self.delta
		
		self.start_curr = start_curr
		self.end_curr = end_curr
		self.api_url = f"https://api.freecurrencyapi.com/v1/historical?apikey={_API_KEY}"
	
	async def fetch_conversion(self, date: datetime):
		response = await client.get(f"{self.api_url}&date={date}&base_currency={self.start_curr}&currencies={self.end_curr}")
		
		if response.status_code == HTTPStatus.OK:
			data = response.json()
			return data['data'][date.date().isoformat()][self.end_curr]
						  
	async def convert_rates(self):
		async with httpx.AsyncClient() as client:
			results = await asyncio.gather(*(self.fetch_conversion(client, time) for time in self.times))
			return results

	async def print_table(self):
		rates = await self.convert_rates()
		data = [[self.times[i], self.start_curr, self.end_curr, rates[i]] for i in range(len(rates))]
		headers = ["Date", "Base Currency", "Converted Currency", "Conversion Rate"]
		print(tabulate(data, headers=headers, tablefmt="grid"))

async def main():
	args = argparse.ArgumentParser()
	args.add_argument("--start-time", type=str, required=True, help="what are the start times of the currency conversions?")
	args.add_argument("--end-time", type=str, required=True, help="what are the end times of the currency conversions?")
	args.add_argument("--start-curr", type=str, required=True, help="what are the starting currencies?")
	args.add_argument("--end-curr", type=str, required=True, help="What currencies are you trying to convert to?")

	parsed_args = args.parse_args()
	app = ExchangeRateApp(parsed_args.start_time, parsed_args.end_time, parsed_args.start_curr, parsed_args.end_curr)
	await app.convert_rates()
	await app.print_table()

if __name__ == "__main__":
	asyncio.run(main())

async def main():
	args = argparse.ArgumentParser()
	args.add_argument("--start-time", type=str, required=True, help="what are the start times of the currency conversions?")
	args.add_argument("--end-time", type=str, required=True, help="what are the end times of the currency conversions?")
	args.add_argument("--start-curr", type=str, required=True, help="what are the starting currencies?")
	args.add_argument("--end-curr", type=str, required=True, help="What currencies are you trying to convert to?")

	parsed_args = args.parse_args()
	app = ExchangeRateApp(parsed_args.start_time, parsed_args.end_time, parsed_args.start_curr, parsed_args.end_curr)
	await app.convert_rates()
	await app.print_table()

if __name__ == "__main__":
	asyncio.run(main())
