''' Serpapi api module for googleSearch'''

from serpapi import GoogleSearch

params = {
    "api_key": "dummy",
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
