@'
# Python Pipeline Monitor

## Overview
A Python-based DevOps automation project that monitors deployment pipeline status using an external JSON configuration file.

## Features
- Reads pipeline configuration from JSON.
- Extracts pipeline name, environment, status and duration.
- Identifies successful and failed deployments.
- Handles unknown pipeline statuses.
- Handles missing configuration files.
- Handles invalid JSON.
- Handles missing mandatory configuration fields.
- Records execution details using Python logging.

## Technologies
- Python 3
- JSON
- Python Logging
- Git and GitHub

## Project Structure

```text
Day-5/
├── pipeline_monitor.py
├── pipeline_data.json
└── README.md
