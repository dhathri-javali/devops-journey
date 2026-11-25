import yaml

with open("pipeline_config.yaml", "r") as file:
    pipeline_data = yaml.safe_load(file)

pipeline_name = pipeline_data["pipeline"]["name"]
environment = pipeline_data["pipeline"]["environment"]
status = pipeline_data["pipeline"]["status"]
duration = pipeline_data["pipeline"]["duration"]

print("Pipeline:", pipeline_name)
print("Environment:", environment)
print("Status:", status)
print("Duration:", duration)
print("Deployment Agent:", pipeline_data["deployment"]["agent"])
print("Deployment Trigger:", pipeline_data["deployment"]["trigger"])

if status == "succeeded":
    print("Deployment successful")

elif status == "failed":
    print("Deployment failed")

elif status == "running":
    print("Deployment is still running")
    
else:
    print("Unknown status")



