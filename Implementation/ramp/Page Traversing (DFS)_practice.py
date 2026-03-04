"""
Goal: You will be entering an HTTP maze. Your goal is to get out of it!

API:
- The maze is represented as an API with one GET endpoint
- To enter the maze, GET /
- To go to a specific step, GET /<STEP_ID>
- Each response contains {"next_step": ["step1", "step2", ...]}
- The final step returns "CONGRATS" as text

Instructions:
- Print the STEP_ID of the final step
- Handle cycles (don't revisit steps)
- Handle API failures with retries
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
        """
        Traverse the maze using DFS to find the exit.

        Requirements:
        1. For each suffix in self.suffixes, make a GET request
        2. Retry if response is not OK
        3. If response is "CONGRATS", return the current suffix
        4. Otherwise, parse JSON and get next_step list
        5. Add unvisited steps to suffixes and mark as visited
        6. Recursively call dfs() if there are more suffixes

        Returns:
            The STEP_ID of the final step, or None if not found

        Hint: Use self.visited to track visited steps (cycle detection)
        """
        # TODO: Implement this method
        pass

def main():
    app = HttpMazeApp()
    step_id = app.dfs()
    print(f"FINAL STEP: {step_id}")

if __name__ == "__main__":
    main()
