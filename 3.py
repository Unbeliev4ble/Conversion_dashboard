import pandas
import pandas as pd
import requests

api_url = 'https://data-charts-api.hexlet.app/'
url = 'https://httpbin.org/get'

# START = '2023-03-01'
# END = '2023-09-01' 
# 
# r = requests.get(api_url)
# r_visits = requests.get(f'{api_url}visits?begin={START}&end={END}')
# print(r.headers,'headers')
# print(r.status_code)

# print(r.content, 'content r')
# print(r.text)

# API_URL = 'https://data-charts-api.hexlet.app/'
# START = '2023-03-01'
# END = '2023-09-01'
# VISITS_FOR_THE_PERIOD = f'{api_url}visits?begin={START}&end={END}'
# REGISTRATIONS_FOR_THE_PERIOD = f'{api_url}registrations?begin={START}&end={END}'
# r_visits = requests.get(VISITS_FOR_THE_PERIOD)

# 
# visits = pd.DataFrame(r_visits.json())
# print(visits)

x = ['asd', '2222']
print('|'.join(x))
