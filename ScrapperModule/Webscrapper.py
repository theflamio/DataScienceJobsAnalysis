""" https://www.linkedin.com/home """

""" xpath = '/html/body/div[2]/p' """ 'chose the second div in the body of the html'

''' xpath = '//span[@class="span-class"]' '''

import requests

response = requests.get('https://www.linkedin.com/jobs/search?keywords=Data%20Science&location=Denmark&geoId=104514075&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0')

print(response.text)