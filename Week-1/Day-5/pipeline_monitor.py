import json
import logging

logging.basicConfig(
    filename="pipeline_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

try:
    with open("pipeline_data.json", "r") as file:
        pipeline_data = json.load(file)

    pipeline_name = pipeline_data["pipeline"]
    environment = pipeline_data["environment"]
    status = pipeline_data["status"]
    duration = pipeline_data.get("duration", 0)

    logging.info(f"Pipeline: {pipeline_name}")
    logging.info(f"Environment: {environment}")
    logging.info(f"Status: {status}")
    logging.info(f"Duration: {duration} seconds")

    if status == "failed":
        logging.error("Production deployment failed!")

    elif status == "succeeded":
        logging.info("SUCCESS: Production deployment completed!")

    else:
        logging.error("WARNING: Unknown pipeline status!")

except FileNotFoundError:
    logging.error("ERROR: Pipeline configuration file not found!")

except json.JSONDecodeError:
    logging.error("ERROR: Invalid JSON configuration!")

except KeyError as error:
    logging.error(f"ERROR: Required configuration field missing: {error}")