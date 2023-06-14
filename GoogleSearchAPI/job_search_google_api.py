''' Serpapi api module for googleSearch'''
import requests
import json
import pprint as pp


# missing docstring
def fecth_jobs_data(job_title, location, number_of_jobs, api_key) -> None:

    # Set up the parameters for the job search
    params = {
    "engine": "google_jobs",
    "q": job_title,
    "hl": "en",
    "location": location,
    "num": number_of_jobs,
    "api_key": api_key
    }

    # Make a request to SerpApi with the parameters
    response = requests.get("https://serpapi.com/search", params=params)

    # Parse the JSON response into a Python object
    data = json.loads(response.text)

    # Extract the job listings from the response
    job_listings = data["jobs_results"]

    #pp.pprint(job_listings)

    # Print the job titles and companies for the first 10 listings
    for i in range(len(job_listings)):
        print("Job_id:", job_listings[i]["job_id"])
        print("Job title:", job_listings[i]["title"])
        print("Company:", job_listings[i]["company_name"])
        print("Location:", job_listings[i]["location"])
        print("job_highlights:", job_listings[i]["job_highlights"])
        print("\n")