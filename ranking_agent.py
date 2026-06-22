def rank_internships(internships, top_count=25):

    unique = {}

    trusted_companies = [
        "google",
        "microsoft",
        "apple",
        "amazon",
        "nvidia",
        "intel",
        "meta",
        "openai",
        "tesla",
        "tiktok",
        "notion",
        "gptzero"
    ]

    for internship in internships:

        score = internship.get("score", 50)

        company = internship["company"].lower()
        role = internship["role"].lower()
        link = internship.get("link", "").lower()

        for trusted in trusted_companies:

            if trusted in company:
                score += 20

        if "ai" in role:
            score += 15

        if "machine learning" in role:
            score += 15

        if "ml" in role:
            score += 10

        if "computer vision" in role:
            score += 15

        if "nlp" in role:
            score += 15

        if "llm" in role:
            score += 20

        if "generative ai" in role:
            score += 20

        if "research" in role:
            score += 10

        if "software engineer" in role:
            score += 10

        if "developer" in role:
            score += 5

        if "careers" in link:
            score += 10

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

    return ranked[:top_count]
