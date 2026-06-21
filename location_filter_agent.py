REGIONS = {
    "india": [
        "india", "chennai", "bangalore", "bengaluru",
        "hyderabad", "pune", "mumbai", "delhi",
        "gurgaon", "noida", "kolkata", "coimbatore"
    ],

    "singapore": [
        "singapore"
    ],

    "malaysia": [
        "malaysia", "kuala lumpur", "penang"
    ],

    "australia": [
        "australia", "sydney", "melbourne",
        "brisbane", "perth", "adelaide"
    ],

    "newzealand": [
        "new zealand", "auckland",
        "wellington", "christchurch"
    ],

    "china": [
        "china", "beijing", "shanghai",
        "shenzhen", "guangzhou"
    ],

    "europe": [
        "uk", "united kingdom", "london",
        "germany", "berlin", "munich",
        "france", "paris",
        "netherlands", "amsterdam",
        "spain", "madrid",
        "italy", "milan",
        "sweden", "stockholm",
        "ireland", "dublin",
        "switzerland", "zurich"
    ],

    "usa": [
        "united states", "usa",
        "california", "new york",
        "texas", "washington",
        "seattle", "san francisco",
        "mountain view", "palo alto",
        "santa clara"
    ]
}


def filter_by_location(internships, region):

    if region.lower() == "all":
        return internships

    region = region.lower()

    if region not in REGIONS:
        return internships

    filtered = []

    for internship in internships:

        location = internship["location"].lower()

        for keyword in REGIONS[region]:

            if keyword in location:

                filtered.append(
                    internship
                )

                break

    return filtered
