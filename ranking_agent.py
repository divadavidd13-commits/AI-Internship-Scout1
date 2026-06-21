def rank_internships(internships):

    unique = {}

    for internship in internships:

        score = internship.get("score", 50)

        company = internship["company"].lower()
        role = internship["role"].lower()
        link = internship.get("link", "").lower()

        trusted_companies = [
            "google",
            "microsoft",
            "apple",
            "ibm",
            "amazon",
            "nvidia",
            "intel",
            "jpmorgan"
        ]

        for trusted in trusted_companies:
            if trusted in company:
                score += 20

        if "careers" in link:
            score += 20

        internship["final_score"] = score

        key = (
            internship["company"].lower(),
            internship["role"].lower()
        )

        if key not in unique:
            unique[key] = internship

        elif internship["final_score"] > unique[key]["final_score"]:
            unique[key] = internship

    ranked = sorted(
        unique.values(),
        key=lambda x: x["final_score"],
        reverse=True
    )

    return ranked[:10]
