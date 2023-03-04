import requests

# Replace "yourusername" with the MuckRock username you want to track
username = "yourusername"
api_url = f"https://www.muckrock.com/api_v1/foia/?user={username}&status="

# Fetch data from MuckRock API
results = []
page_count = 1
while True:
    response = requests.get(api_url + f"&page={page_count}")
    if response.status_code == 200:
        data = response.json()
        results += data["results"]
        if data["next"] is None:
            break
        page_count += 1
    else:
        # Handle errors if any
        print(f"Error fetching data from MuckRock API: {response.status_code}")
        break

# Extract number of FOIA requests made by the user
requests_count = len(results)

# Display the request count and status of each request
print(f"This user has made {requests_count} FOIA requests on MuckRock.")
print("Request ID    |    Status")
print("--------------------------")
for result in results:
    request_id = result["id"]
    status = result["status"]
    print("{:<14}|    {}".format(request_id, status))
