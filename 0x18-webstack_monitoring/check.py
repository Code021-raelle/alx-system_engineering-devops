import requests

api_key = '80defb96091924d17c903da8d652e226'
app_key = 'd567de68ecdf3bfff099ff160b1c13024be9d5f6'

headers = {
        'DD-API-KEY': api_key,
        'DD-APPLICATION-KEY': app_key,
        'Content-Type': 'application/json'
}

response = requests.get('https://api.datadoghq.com/api/v1/dashboard', headers=headers)

if response.status_code == 200:
    dashboards = response.json()['dashboards']
    for dashboard in dashboards:
        if dashboard['title'] == "Gabriel's Dashboard Wed, May 8, 10:25:16 am":
            dashboard_id = dashboard['id']
            break

    print("Dashboard ID:", dashboard_id)
else:
    print("Failed to retrieve dashboards. Status code:", response.status_code)

