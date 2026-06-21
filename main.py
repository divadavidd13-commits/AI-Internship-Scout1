from search_linkedin import search_linkedin
from filter_agent import filter_internships
from verification_agent import verify_internship
from ranking_agent import rank_internships
from save_results import save_results
from compare_results import find_new_internships
from email_agent import send_email
from location_filter_agent import filter_by_location

keyword = input(
    "Enter internship keyword: "
)

location_mode = input(
    "Region (india/usa/europe/singapore/malaysia/australia/newzealand/china/all): "
)

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

    if score >= 60:

        internship["score"] = score

        verified_results.append(
            internship
        )

top_internships = rank_internships(
    verified_results
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
