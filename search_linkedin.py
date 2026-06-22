import requests
from bs4 import BeautifulSoup


def search_linkedin(keyword, region="all"):

    keywords = [
        k.strip()
        for k in keyword.split(",")
        if k.strip()
    ]

    internships = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for item in keywords:

        search_term = item + " intern"

        
        url = (
            "https://www.linkedin.com/jobs/search/"
            "?keywords="
            + search_term.replace(" ", "%20")
        )

        if region.lower() != "all":

            url += (
                "&location="
                + region.replace(" ", "%20")
            )

        response = requests.get(
            url,
            headers=headers
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        jobs = soup.find_all(
            "div",
            class_="base-search-card"
        )

        for job in jobs:

            title = job.find(
                "h3",
                class_="base-search-card__title"
            )

            if not title:
                continue

            company = job.find(
                "h4",
                class_="base-search-card__subtitle"
            )

            location = job.find(
                "span",
                class_="job-search-card__location"
            )

            link_tag = job.find(
                "a",
                class_="base-card__full-link"
            )

            internships.append(
                {
                    "company":
                        company.get_text(strip=True)
                        if company else "Unknown",

                    "role":
                        title.get_text(strip=True),

                    "location":
                        location.get_text(strip=True)
                        if location else "Unknown",

                    "link":
                        link_tag.get("href")
                        if link_tag else ""
                }
            )

    # Remove duplicate internships using LinkedIn URL

    unique = {}

    for internship in internships:

        link = internship.get(
            "link",
            ""
        ).strip()

        if link and link not in unique:

            unique[link] = internship

    internships = list(
        unique.values()
    )

    return internships
