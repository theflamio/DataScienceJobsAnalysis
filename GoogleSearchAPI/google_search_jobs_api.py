''' Serpapi api module for googleSearch'''

from serpapi import GoogleSearch

params = {
    "api_key": "8452f12ed3998f8207bbd3063f25e8517b5231966f4fa2fa71e64b3ddf9be75d",
    "device": "desktop",
    "engine": "google_jobs",
    "google_domain": "google.com",
    "q": "data scientist"
}

search = GoogleSearch(params)
results = search.get_dict()
jobs_results = results["jobs_results"]

print(type(jobs_results))

print(jobs_results)

for job in jobs_results:
    print(job)
