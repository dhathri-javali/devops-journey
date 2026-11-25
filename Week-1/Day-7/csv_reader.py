import csv

def count_pipelines_by_status(pipeline_inventory):

    status_count = {
        "succeeded": 0,
        "failed": 0,
        "running": 0
    }

    for pipeline in pipeline_inventory:

        status = pipeline["status"]

        if status in status_count:
            status_count[status] += 1

    return status_count 

def find_failed_pipelines(pipeline_inventory):

    failed_pipelines = []

    for pipeline in pipeline_inventory:

        if pipeline["status"] == "failed":

            failed_pipelines.append(pipeline)

    return failed_pipelines

with open("pipeline_inventory.csv", "r") as file:

    reader = csv.DictReader(file)

    pipeline_inventory = list(reader)

    for pipeline in pipeline_inventory:

        print("Pipeline:", pipeline["pipeline"])
        print("Environment:", pipeline["environment"])
        print("Status:", pipeline["status"])
        print("----------------------")

    result = count_pipelines_by_status(pipeline_inventory)

    print("\n========== PIPELINE INVENTORY ==========")

    print("Total Pipelines:", len(pipeline_inventory))
    print("Successful:", result["succeeded"])
    print("Failed:", result["failed"])
    print("Running:", result["running"])

    print("========================================")

failed = find_failed_pipelines(pipeline_inventory)

print("\nFailed Pipelines:")

for pipeline in failed:
    print(pipeline["pipeline"], "-", pipeline["environment"])