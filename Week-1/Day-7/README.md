# Pipeline Inventory & Configuration Manager

## 1. Project Overview

A Python-based DevOps automation tool that reads pipeline inventory from CSV files and deployment configuration from YAML files.

It generates pipeline health summaries and automatically identifies failed deployments.

## 2. Technologies Used

- Python 3
- CSV
- YAML
- PyYAML
- Linux / Ubuntu

## 3. Project Structure

```text
Day-7/
├── pipeline_inventory.csv
├── pipeline_config.yaml
├── csv_reader.py
├── yaml_reader.py
├── pipeline_manager.py
└── README.md
```

## 4. Features

1. Reads pipeline inventory using CSV DictReader.
2. Reads deployment configuration using PyYAML.
3. Displays pipeline details.
4. Counts successful, failed and running pipelines.
5. Identifies failed pipelines and their environments.
6. Handles missing CSV and YAML files.
7. Handles invalid YAML syntax.
8. Uses exception handling to prevent unexpected execution after configuration errors.

## 5. Installation

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install PyYAML:

```bash
python -m pip install PyYAML
```

## 6. Execution

Run:

```bash
python pipeline_manager.py
```

## 7. Expected Output

The program displays:

- Deployment configuration
- Pipeline inventory
- Total pipeline count
- Successful pipeline count
- Failed pipeline count
- Running pipeline count
- Failed pipeline details

## 8. Learning Outcomes

- Python file handling
- CSV processing
- YAML parsing
- Dictionaries and lists
- Loops and conditional statements
- Exception handling
- Python virtual environments
- Exit codes in automation scripts
