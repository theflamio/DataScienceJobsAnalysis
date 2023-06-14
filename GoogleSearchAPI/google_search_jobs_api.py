''' Serpapi api module for googleSearch'''
import requests
import json
import pprint as pp

# Replace YOUR_API_KEY with your actual API key from SerpApi
api_key = "3e8bfad60337397b2b8fbc49bdab6e307b5cabd9f50213bd4e44c02563df84f5"

# Set up the parameters for the job search
params = {
    "engine": "google_jobs",
    "q": "data science",
    "hl": "en",
    "location": "Denmark",
    "num": 100,
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
