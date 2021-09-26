import requests
import modules.configs as configs


# Get all the sites
def getSites():
    response = requests.get(configs.baseUrl + "/get_sites")
    return response.json()
