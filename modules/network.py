import requests
import modules.configs as configs
import webbrowser


# Get all the sites
webbrowser.open('http://localhost:5001')


def getSites(user):
    response = requests.get(configs.baseUrl + f"/get_sites/{user}")
    return response.json()
