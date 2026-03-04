"""

Goal
You will be entering an HTTP maze. Your goal is to get out of it!
API

ENDPOINT = "https://adapter-cingular-ill-operations.trycloudflare.com"

The maze will be represented as an API with one GET endpoint.
To enter the maze, head over to ‹ENDPOINT>
To go to a specific step in the maze, GET /<STEP_ ID>
The final step of the maze will return a "CONGRATS" message.
Instructions

Print the STEP_ID of the final step

"""

import requests

from http import HTTPStatus

class HttpMazeApp:
	def __init__(self) -> None:
		self.api_url = "http://127.0.0.1:5000"
		self.visited = set()
		self.suffixes = [""]
		self.visited.add("")
	
	def dfs(self):
		for suffix in self.suffixes:
			new_api_url = f"{self.api_url}/{suffix}"

			response = requests.get(new_api_url)

			while response.status_code != HTTPStatus.OK and response.text != "CONGRATS":
				response = requests.get(new_api_url)
			
			if response.text == "CONGRATS":
				return suffix 
			
			data = response.json()
			assert 'next_step' in data, "next step is missing"

			self.suffixes = []

			for next_step in data['next_step']:
				if next_step not in self.visited:
					self.visited.add(next_step)
					self.suffixes.append(next_step)
		
		if self.suffixes:
			return self.dfs()
		
		return None

def main():
	app = HttpMazeApp()
	step_id = app.dfs()
	print(f"FINAL STEP: {step_id}")

if __name__ == "__main__":
	main()


