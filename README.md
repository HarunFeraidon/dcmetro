# DC Metro Command Line Tool
![Imgur](https://i.imgur.com/rE4AKgU.gif)

## What is it
[![PyPI version](https://badge.fury.io/py/dcmetro.svg)](https://badge.fury.io/py/dcmetro)

A command line app for sending commands to get live information on the DC Metro. You can find the shortest path between two stations, an estimation of the rail time between two stations, and the current arrival times for your metro station.
[PyPi page here](https://pypi.org/project/dcmetro/0.1.3/)

## Setup
1. Setup a python virtual environment. `python3 -m venv venv`
2. Activate your python virtual environment. `source venv/bin/activate`
3. Install with `pip install dcmetro`.
4. (OPTIONAL, BUT RECOMMENDED) Skipping this step means you will be using a community API key. Creating your own API token will be more reliable. Setup a WMATA API token [here](https://developer.wmata.com). Run `echo 'API_KEY = "<YOUR TOKEN HERE>"' > .env`
5. Run `dcmetro` to start.

Useful commands include:
- `when <location>` to view incoming trains.
- `length <from_location> to <to_location>` to get an estimated length of rail time (not including stops, which will vary)
- `path <from_location> to <to_location>` to get the shortest path from one location to the other.

# How it works
The DC Metro has an [API](https://developer.wmata.com)! This API includes some useful endpoints with the information needed to build out commands, such as the ones above.

The command `path <from_location> to <to_location>` uses a graph respresentation of the DC Metro. Because it is fully connected, it should be possible to get the path from any spot to another. Additionally, if the distance between two nodes was provided, then the shortest path can even be calculated. Luckily, the API has some endpoints that provide enough information to build this. One endpoint provides all the stations on a specific train colors route, from one of its ends to the other. The distance to the previous station was also provided. 
So, having the stations, in order, of a specific route color, and with distances to the previous station, you are able to create a graph with weighted edges, by iterating through all route colors' list of stations and distances between stations. 

*This was enough to complete a fully connected graph with weighted edges.*
From here, Dijkstra's algorithm is utilized to find the shortest path between any two nodes in the graph.

<img src="https://i.imgur.com/RQmR9qo.png"  width="40%" height="40%">

Finally, the [Textual](https://textual.textualize.io) Python library is used for the terminal user interface.

