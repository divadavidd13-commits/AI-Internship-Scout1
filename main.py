from search_linkedin import search_linkedin
from filter_agent import filter_internships
from verification_agent import verify_internship
from ranking_agent import rank_internships
from save_results import save_results
from compare_results import find_new_internships
from email_agent import send_email
from location_filter_agent import filter_by_location

keyword = input(
    "Enter internship keyword (or 'all'): "
).strip().lower()

location_mode = input(
    "Region (india/usa/europe/singapore/malaysia/australia/newzealand/china/all): "
)

top_count = input(
    "How many results? (10/25/50): "
).strip()

if top_count not in ["10", "25", "50"]:
    top_count = "25"

top_count = int(top_count)

if keyword == "all":

    keywords = [
        "ai",
        "machine learning",
        "data science",
        "software engineer",
        "python",
        "web development",
        "cloud",
        "devops",
        "cybersecurity",
        "electronics",
        "embedded systems",
        "iot"
    ]

    results = []

    for kw in keywords:

        print(f"Searching: {kw}")

        jobs = search_linkedin(
            kw,
            location_mode
        )

        results.extend(jobs)

    unique_jobs = {}

    for job in results:

        link = job.get("link")

        if link:
            unique_jobs[link] = job

    results = list(unique_jobs.values())

else:

    results = search_linkedin(
        keyword,
        location_mode
    )

filtered_results = filter_internships(
    results
)

verified_results = []

for internship in filtered_results:

    score = verify_internship(
        internship
    )

    if score >= 50:

        internship["score"] = score

        verified_results.append(
            internship
        )

top_internships = rank_internships(
    verified_results,
    top_count
)

top_internships = filter_by_location(
    top_internships,
    location_mode
)

new_internships = find_new_internships(
    top_internships
)

save_results(
    top_internships
)

print("\nTotal Found:", len(results))
print("After Filter:", len(filtered_results))
print("Verified:", len(verified_results))
print("Ranked:", len(top_internships))

print(
    "\nNEW INTERNSHIPS:",
    len(new_internships)
)

if not new_internships:

    print("No new internships found.")

for internship in new_internships:

    print("\n----------------")
    print("Company:", internship["company"])
    print("Role:", internship["role"])
    print("Location:", internship["location"])
    print("Score:", internship["final_score"])
    print("Link:", internship["link"])

send_email(
    new_internships
)

print(
    "\nResults saved to internships.json"
)
