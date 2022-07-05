import datetime
import ipaddress
import json
import requests


def get_last_monday_str():
    today = datetime.datetime.today()
    last_monday = today + datetime.timedelta(days=-today.weekday())
    return last_monday.strftime('%Y%m%d')


def get_azure_ips(save_json: bool = False) -> dict:
    last_monday_str = get_last_monday_str()
    url = f'https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_{last_monday_str}.json'
    print(url)
    response = requests.get(url).content.decode('utf-8')
    if save_json:
        with open(f'{last_monday_str}-azure-ip.json', 'w') as f:
            f.write(response)
    return json.loads(response)['values']


def get_services_ip_ranges() -> dict:
    SERVICES = ('PowerBI', 'DataFactory.WestEurope', 'AzureCloud')
    values = get_azure_ips()
    services_ip_ranges = {
        service['name'].replace('.', '_'): [
            net for net in service['properties']['addressPrefixes']
            if '::' not in net
        ]
        for service in values
        if service['name'] in SERVICES
    }
    return services_ip_ranges


def create_policy(outfile='snowflake/system/network-policies.sql'):
    ip_ranges = {
        'Dept offices': ['213.214.122.237', '89.20.163.66', '89.20.163.70', '62.96.47.178'],
        'BPD office': ['185.52.213.40'],
        'Christiaan home office': ['77.169.45.126', '213.127.69.30'],
        'BPD network': ['194.151.183.29', '82.95.156.222', '83.84.235.218', '213.125.20.146', '83.86.167.146'],
        'Azure not in ServiceTags': ['20.123.227.80', '20.23.34.233', '20.23.34.7', '20.23.34.227', '20.23.33.134', '20.123.224.118', '20.123.242.151', '20.123.242.169'],
        **get_services_ip_ranges()
    }
    ip_ranges_str = "'" + "',\n\t'".join(
        ip for ip_range in ip_ranges.values() for ip in ip_range
    ) + "'"
    network_policy = \
        "create or replace network policy AZURE_DEPT_{last_monday}\n" \
        "comment = '{comment}'\n" \
        "allowed_ip_list = (\n\t{ip_range}\n);\n" \
         "alter account set network_policy = AZURE_DEPT_{last_monday}".format(
            last_monday=get_last_monday_str(),
            ip_range=ip_ranges_str,
            comment='Policy for ' + ', '.join(ip_ranges.keys())
        )
    with open(outfile, 'w') as f:
        f.write(network_policy)


def find_azure_service(ip: str):
    def addressInNetwork(ip, net):
        return ipaddress.ip_address(ip) in ipaddress.ip_network(net)

    values = get_azure_ips()
    for service in values:
        for net in service['properties']['addressPrefixes']:
            if '::' not in net and addressInNetwork(ip, net):
                print(service['name'])


if __name__ == '__main__':
    create_policy()
