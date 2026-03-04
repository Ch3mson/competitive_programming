from flask import Flask, jsonify
import random

app = Flask(__name__)

# Define the maze graph
maze = {
    "": ["a", "b", "c"],       # root -> /, gives 3 next steps
    "a": ["d", "e"],
    "b": ["f"],
    "c": ["g", "h"],
    "d": ["i"],                # path continues deeper
    "e": ["b"],                # cycle: e -> b
    "f": ["j", "k"],
    "g": ["e"],                # cycle: g -> e
    "h": ["l"],
    "i": ["m"],
    "j": ["n"],
    "k": ["o"],
    "l": ["p", "q"],
    "m": ["r"],
    "n": [],                   # dead end
    "o": [],                   # dead end
    "p": [],                   # dead end
    "q": ["x"],                # eventually leads to victory
    "r": ["s"],
    "s": ["c"],                # cycle back up
    "x": "CONGRATS"            # WIN condition
}

@app.route("/", defaults={"step": ""})
@app.route("/<step>")
def maze_step(step):
    if step not in maze:
        # simulate occasional errors for realism
        if random.random() < 0.2:
            return "Server hiccup, retry!", 500
        return jsonify({"error": "Invalid step"}), 404

    result = maze[step]
    if result == "CONGRATS":
        return "CONGRATS"
    return jsonify({"next_step": result})

if __name__ == "__main__":
    app.run(debug=True)
