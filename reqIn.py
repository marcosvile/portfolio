from itsdangerous import json
import requests
import json

# url = 'https://www.linkedin.com/in/pleiterson/details/recommendations/?detailScreenTabIndex=0'
# res = requests.get(url)
# html_page = res.text

# print (html_page)


res=requests.get('https://www.linkedin.com/in/pleiterson/details/recommendations/?detailScreenTabIndex=0')

print(res)
























# api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
# api_key = '5c3b3893-5e9a-4898-b906-eaf7786a9e0f'
# header_dic = {'Authorization': 'Bearer ' + api_key}
# params = {
#     'url': 'https://www.linkedin.com/in/marcosvile/',
#     "recommendations": [],
# }
# response = requests.get(api_endpoint,
#                         params=params,
#                         headers=header_dic)

# print (response.text)