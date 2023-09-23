# 🐝 BeeAware Backend

Welcome to the BeeAware backend repository! This Flask-based API serves as the backend for the BeeAware app, which aims to enhance situational awareness by alerting users about crime hotspots in Almaty, Kazakhstan 🇰🇿

Link to the **iOS repository**: https://github.com/MuratovArthur/nfactorial-hackathon-ios

## Features

Interactive, scalable map highlighting areas with high crime rates in Almaty, Kazakhstan:

![Map gif](media/map.gif)

## API Documentation

### Base URL

The base URL for the BeeAware backend API is `http://localhost:5000/` when running locally.

### Endpoints

#### 1. `GET /`

- **Description:** This endpoint serves the HTML page for the BeeAware map.

- **Response:** Renders the HTML page for the BeeAware map.

#### 2. `GET /response.geojson`

- **Description:** This endpoint serves the GeoJSON data containing crime hotspot information for Almaty, Kazakhstan.

- **Response:** Returns the `response.geojson` file from the root directory.

#### 3. `GET /danger_level`

- **Description:** This endpoint calculates the danger level for a given geographic location (latitude and longitude) based on the number of crime incidents within a specified radius.

- **Parameters:**
  - `latitude` (float): The latitude of the location.
  - `longitude` (float): The longitude of the location.

- **Response:** Returns the danger level as a JSON object with the following format:

```json
{
    "danger_level": 1
}
```

### Example Usage

To retrieve the danger level for a specific location, make a GET request to the `/danger_level` endpoint with the latitude and longitude as query parameters:

```bash
GET /danger_level?latitude=43.2547&longitude=76.9280
```

## Getting Started

To get started with the BeeAware backend, follow these steps:

1. Clone this repository: `git clone https://github.com/MuratovArthur/nfactorial-hackathon-backend.git`
2. Run the Flask application: `python app.py`
