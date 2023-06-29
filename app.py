from flask import Flask, jsonify, request, render_template, send_from_directory
import geopandas as gpd
from shapely.geometry import Point
from sklearn.neighbors import BallTree
import numpy as np

app = Flask(__name__)

# Load data
data = gpd.read_file("response.geojson")
data["longitude"] = data.geometry.x
data["latitude"] = data.geometry.y

# Construct ball tree
tree = BallTree(np.deg2rad(data[["latitude", "longitude"]].values), metric="haversine")

# Define radius (in kilometers)
radius = 1.0


@app.route("/")
def home():
    return render_template("map.html")


@app.route("/response.geojson")
def serve_geojson():
    return send_from_directory(".", "response.geojson")


@app.route("/danger_level", methods=["GET"])
def danger_level():
    # Parse latitude and longitude from query parameters
    latitude = float(request.args.get("latitude"))
    longitude = float(request.args.get("longitude"))

    # Query ball tree
    indices = tree.query_radius(np.deg2rad([[latitude, longitude]]), r=radius / 6371)

    # Check the number of points within radius and define danger level
    count = len(indices[0])
    print(count)
    if count > 400:
        danger_level = 3
    elif count > 300:
        danger_level = 2
    else:
        danger_level = 1

    # Return result
    return jsonify({"danger_level": danger_level})


if __name__ == "__main__":
    app.run(debug=True)
