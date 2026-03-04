"""
Goal: Navigate through an HTTP maze to find the exit.

API Details:

Base URL: https://example.com
To move: GET /<step_id>
Victory: You'll see a "CONGRATS" message
Task: Find and provide the step_id of the final step (the one with the CONGRATS message).

For example:

GET "example.com/" -> reseponse {next_step: ["abc", cde", "fgh"]},
GET "example.com/abc" -> response {next_step: []},
GET "example.com/cde" -> response {next_step: [a]}
...
GET "example.com/jkdf -> response "CONGRATS"
Additional notes:

You need to use GET requests in python
some routes will error so you will have to retry
can do DFS or BFS
Some edge cases to consider:

Cycle
"""
import asyncio
import httpx
import requests

from http import HTTPStatus

class WebCrawlerApp:
	def __init__(self, base_url: str) -> None:
		self.base_url = base_url
		self.visited = set() #deal with cycles 
		self.steps = [""]
	
	async def dfs(self, client: httpx.AsyncClient, step: str):
		if step not in self.visited:
			self.visited.add(step)
			response = await client.get(f"{self.base_url}/{step}")

			if response.status_code == HTTPStatus.OK:
				try:
					data = response.json()
					return (data["next_step"], step)

				except ValueError:
					return ("CONGRATS", step)
	
	async def process_steps(self):
		async with httpx.AsyncClient() as client:
			results = await asyncio.gather(*(self.dfs(client, step) for step in self.steps))
			self.steps = []
			
			for result in results:
				if result is None:
					continue 
			
				next_step, step = result

				self.steps += next_step
				if next_step == "CONGRATS":
					return step 
			
			return -1
	
	async def traverse_maze(self):
		result = await self.process_steps()

		while result == -1:
			result = await self.process_steps()
		
		return result
	

if __name__ == "__main__":
	app = WebCrawlerApp("http://127.0.0.1:5000")
	res = asyncio.run(app.traverse_maze())
	print(res)

----------

"""
Goal: Navigate through an HTTP maze to find the exit.

API Details:

Base URL: https://example.com => FAKE URL: http://127.0.0.1:5000
To move: GET /<step_id>
Victory: You'll see a "CONGRATS" message
Task: Find and provide the step_id of the final step (the one with the CONGRATS message).

For example:

GET "example.com/" -> reseponse {next_step: ["abc", cde", "fgh"]},
GET "example.com/abc" -> response {next_step: []},
GET "example.com/cde" -> response {next_step: [a]}
...
GET "example.com/jkdf -> response "CONGRATS"
Additional notes:

You need to use GET requests in python
some routes will error so you will have to retry
can do DFS or BFS
Some edge cases to consider:

Cycle
"""

# bfs/dfs graph question 
# lead to next steps if successful 
# cycles are possible 
# there is a chance it is going to be 500 
#    try again until it returns 200 
#.   CONGRATS will be returned as a string, not as a json -- no status code 
#. no, no other strings will be returned -> we can check if the instance of the response is a string and if it equals congrats 

# visited set to detect cycles 
# dfs with the children (next steps) of the current url until we reach congrats 
# initialize a while loop to check the status of the request (if the request is equal to congrats (type is a string))
# asyncio to run api calls at the same time 

import asyncio
import httpx

from http import HTTPStatus

class WebCrawlerApp:
    def __init__(self):
        self.base_api = "http://127.0.0.1:5000"
        self.steps = [""]
        self.visited = set()
    
    async def dfs(self, client: httpx.AsyncClient, step: str):
        if step in self.visited:
            return None
    
        self.visited.add(step)

        updated_url = f"{self.base_api}/{step}"
        response = await client.get(updated_url)

        while response.text != "CONGRATS" and response.status_code != HTTPStatus.OK:
            response = await client.get(updated_url)
        
        if response.text == "CONGRATS":
            return ("CONGRATS", step)
        
        data = response.json()
        return (data['next_step'], step)

    async def fetch_next_steps(self):
        async with httpx.AsyncClient() as client:
            results = await asyncio.gather(*(self.dfs(client, step) for step in self.steps))
            self.steps = []

            for result in results: 
                if result is None:
                    continue 
            
                if result[0] == "CONGRATS":
                    return result[1]
                
                self.steps += result[0]
            
            return None
    
    async def find_end(self):
        result = await self.fetch_next_steps()

        while result is None:
            result = await self.fetch_next_steps()
        
        return result

async def main():
    app = WebCrawlerApp()
    result = await app.find_end()
    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())

