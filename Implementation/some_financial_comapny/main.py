"""
1. Print the frist 10 coordinates

arr[:10] get first 10 elements of array

2. Make an HTTP POST request to 

https://httpbin.org/post
httpbin.org

passing json request body:

{

}

3. Create a new object to send to this endpoint
Group these coordinates.

has a key called labels 
first label is "Waterloo", isStart: true. is first coordinate in test.json

second label is last label "name": Toronto, "coordinate": last in test.json, isStart: false

paths:
Alternate path color from Waterloo -> Toronto
alternate red and blue.

Every 5 swap with blue

"""
import requests
import json

def get_coordinates():
    with open('test.json', 'r') as file:
        data = json.load(file)

    return data["features"][0]["geometry"]["coordinates"]

def request_httpbin():
    body = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": {
                "name": "Sample Line with 100 Coordinates"
            },
            "geometry": {
                "type": "LineString",
                "coordinates": get_coordinates()[:10]
            }
        }]
    }
    
    url = "https://httpbin.org/post"

    response = requests.post(url, json = body)
    data = response.json()
    print("DATA:", data)
    print("REQUEST STATUS CODE:", response.status_code)

def create_labels_paths(labels):
    """
    args:
    labels: [{"isStart", "name", "coordinate"}, ...]
    """
    with open('test.json', 'r') as file:
        data = json.load(file)
    
    coordinates = data["features"][0]["geometry"]["coordinates"]

    paths = []
    colors = ["red", "blue"]

    i = 0
    color_index = 0
    coordinates_length = 5
    
    while i < len(coordinates):
        k = 0
        coordinate_grouping = []
        while k < coordinates_length:
            coordinate_grouping.append(coordinates[i])
            k += 1
            i += 1
        
        paths.append({
            "colour": colors[color_index % len(colors)],
            "coordiantes": coordinate_grouping
        })
        
        color_index += 1
    
    body = {
        "labels": labels,
        "paths": paths
    }

    url = "https://httpbin.org/post"

    response = requests.post(url, json = body)
    data = response.json()
    print("DATA:", data)
    print("REQUEST STATUS CODE:", response.status_code)
        


if __name__ == "__main__":

    with open('test.json', 'r') as file:
        test_json = json.load(file)

    data = [
        {
            "isStart": True,
            "name": "Waterloo",
            "coordinate": test_json["features"][0]["geometry"]["coordinates"][0]
        },
        {
            "isStart": False,
            "name": "Toronto",
            "coordinate": test_json["features"][0]["geometry"]["coordinates"][-1]
        }
    ]

    create_labels_paths(data)