import json
import os,sys
import concurrent.futures
import requests
import re
os.chdir(sys.path[0])

with open("1.json",'r',encoding='utf-8') as f:
    dic1 = json.loads(f.read())
with open("2.json",'r',encoding='utf-8') as f:
    dic2 = json.loads(f.read())

site1 = dic1['sites']['data']
site2 = dic2['sites']

print(dic1.keys())
print(dic2.keys())

dic = dict()
dic["site"] = []

with open('valid.txt','r',encoding='utf-8') as f:
    valid = f.read().splitlines()
# print(valid)
api_urls = []
id = 1
for i in range(len(site1)):
    if site1[i]['api'] in valid and site1[i]['api'] not in api_urls:
        site1[i]['id'] = id
        dic["site"].append(site1[i])
        id+=1
        api_urls.append(site1[i]['api'])

for i in range(len(site2)):
    if site2[i]['api'] in valid and site2[i]['api'] not in api_urls:
        site2[i]['id'] = id
        dic["site"].append(site2[i])
        id+=1
        api_urls.append(site2[i]['api'])

with open('sites.json','w',encoding='utf-8') as f:
    f.write(json.dumps(dic,ensure_ascii=False))

# api_urls = []
# valid_api_urls = []

# for i in range(len(site1)):
#     api_urls.append(site1[i]['api'])
# for i in range(len(site2)):
#     api_urls.append(site2[i]['api'])
# api_urls = list(set(api_urls))

# def check_api_validity(api_url):
#     try:
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             print(f"API {api_url} is valid.")
#             with open('valid.txt','a',encoding='utf-8') as f:
#                 f.write(api_url+'\n')
#         else:
#             print(f"API {api_url} returned a non-200 status code: {response.status_code}")
#     except requests.RequestException as e:
#         print(f"Error while checking API {api_url}: {e}")

# def main():
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         executor.map(check_api_validity, api_urls)

# if __name__ == "__main__":
#     main()

