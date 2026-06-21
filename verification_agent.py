def verify_internship(internship):

    score = 50

    company = internship["company"].lower()
    role = internship["role"].lower()

    trusted_companies = [
        "microsoft",
        "google",
        "apple",
        "ibm",
        "jpmorgan",
        "nvidia",
        "intel",
        "amazon",
        "tesla",
        "notion",
        "gptzero"
    ]

    for company_name in trusted_companies:

        if company_name in company:

            score += 30

    if "intern" in role:
        score += 10

    if "engineer" in role:
        score += 10

    if "ai" in role:
        score += 10

    if "machine learning" in role:
        score += 10

    if "data science" in role:
        score += 10

    return score
