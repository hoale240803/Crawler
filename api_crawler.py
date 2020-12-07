import requests

# step 2: send a get request, get a response object
result = requests.get(
    'https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85,ELEC&state=CA&limit=2&api_key=JSFa9M8QzzH39MePt0ddhDwbbneiNtrwn3BpWZLp')
# step 3: Get status code returns an integer on success
result.status_code
# step 4: Get data
print(result.text)
# step 5: Get data in a more readable json format
print(result.json)
