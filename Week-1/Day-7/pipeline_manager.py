import csv
import yaml
import sys


try:
    # Read CSV file
    with open("pipeline_inventory.csv", "r") as file:
        reader = csv.DictReader(file)
        pipeline_inventory = list(reader)

    # Read YAML file
    with open("pipeline_config.yaml", "r") as file:
        deployment_config = yaml.safe_load(file)

    if not isinstance(deployment_config, dict):
        raise ValueError("Invalid YAML configuration")

except FileNotFoundError as error:
    print(f"ERROR: Configuration file not found: {error.filename}")
    sys.exit(1)

except yaml.YAMLError:
    print("ERROR: Invalid YAML configuration!")
    sys.exit(1)

except ValueError as error:
    print(f"ERROR: {error}")
    sys.exit(1)

print("Deployment Configuration")
print("Agent:", deployment_config["deployment"]["agent"])
print("Trigger:", deployment_config["deployment"]["trigger"])

print("\nPipeline Inventory")

for pipeline in pipeline_inventory:
    print(
        pipeline["pipeline"],
        pipeline["environment"],
        pipeline["status"]
    )

# Pipeline Health Summary

status_count = {
    "succeeded": 0,
    "failed": 0,
    "running": 0
}

for pipeline in pipeline_inventory:
    status = pipeline["status"]

    if status in status_count:
        status_count[status] += 1

print("\n========== PIPELINE HEALTH SUMMARY ==========")
print("Total Pipelines:", len(pipeline_inventory))
print("Successful:", status_count["succeeded"])
print("Failed:", status_count["failed"])
print("Running:", status_count["running"])
print("============================================")

# Identify Failed Pipelines

failed_pipelines = []

for pipeline in pipeline_inventory:
    if pipeline["status"] == "failed":
        failed_pipelines.append(pipeline)

print("\n========== FAILED PIPELINES ==========")

if failed_pipelines:
    for pipeline in failed_pipelines:
        print(
            pipeline["pipeline"],
            "-",
            pipeline["environment"]
        )
else:
    print("No failed pipelines!")

print("======================================")