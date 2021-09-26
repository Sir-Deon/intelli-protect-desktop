import platform
from datetime import datetime
import modules.network as network

end_time = datetime(2021, 1, 1, 20)

if platform.system() == 'Windows':
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == 'Linux' or platform.system() == 'Darwin':
    hosts_path = '/etc/hosts'


redirect = "127.0.0.1"
sites_to_block = []
sites_to_unblock = []


def commander():
    # Get sites
    sites = network.getSites()
    for site in sites:
        if(site['blocked'] == True):
            sites_to_block.append("www." + site['name'])
            sites_to_block.append(site['name'])
            block_website()
        else:
            sites_to_unblock.append(site['name'])
            unblock_website()


def getBlockedSites():
    try:
        with open('blocked_sites.txt', 'r') as file:
            sites = file.readlines()
            return sites
    except:
        return "No sites found !!"


def block_website():
    print("Blocked site")
    with open(hosts_path, 'r+') as hostfile:
        hosts_content = hostfile.read()
        for site in sites_to_block:
            if site not in hosts_content:
                hostfile.write(redirect + ' ' + site + '\n')

    with open('blocked_sites.txt', 'r+') as file:
        sites = file.read()
        for site in sites_to_block:
            if site not in sites:
                file.write(site + '\n')


def unblock_website():
    print('Unblock site')
    with open(hosts_path, 'r+') as hostfile:
        lines = hostfile.readlines()
        hostfile.seek(0)
        for line in lines:
            if not any(site in line for site in sites_to_unblock):
                hostfile.write(line)
        hostfile.truncate()
    with open('blocked_sites.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(site in line for site in sites_to_unblock):
                file.write(line)
        file.truncate()


commander()
