def verify_internship(internship):

    score = 0

    company = internship["company"].lower()
    role = internship["role"].lower()

    tier1_companies = [
        "google",
        "microsoft",
        "nvidia",
        "amazon",
        "meta",
        "apple",
        "openai"
    ]

    tier2_companies = [
        "intel",
        "tesla",
        "tiktok",
        "notion",
        "gptzero",
        "tencent",
        "point72"
    ]

    ai_keywords = [
        "ai",
        "machine learning",
        "ml",
        "deep learning",
        "computer vision",
        "nlp",
        "llm",
        "generative ai",
        "artificial intelligence"
    ]

    software_keywords = [
        "software",
        "engineer",
        "developer",
        "python",
        "cloud",
        "backend",
        "frontend",
        "fullstack",
        "full stack"
    ]

    research_keywords = [
        "research",
        "scientist",
        "quant",
        "optimization"
    ]

    internship_keywords = [
        "intern",
        "internship",
        "co-op",
        "trainee"
    ]

    negative_keywords = [
        "sales",
        "marketing",
        "support",
        "helpdesk",
        "recruiter",
        "accounting"
    ]

    # Company quality

    if any(company_name in company for company_name in tier1_companies):
        score += 30

    elif any(company_name in company for company_name in tier2_companies):
        score += 20

    # Internship relevance

    if any(word in role for word in internship_keywords):
        score += 25

    # AI relevance

    for word in ai_keywords:
        if word in role:
            score += 15

    # Software relevance

    for word in software_keywords:
        if word in role:
            score += 5

    # Research relevance

    for word in research_keywords:
        if word in role:
            score += 10

    # Negative signals

    for word in negative_keywords:
        if word in role:
            score -= 20

    # Bonus combinations

    if "research" in role and "ai" in role:
        score += 10

    if "machine learning" in role and "engineer" in role:
        score += 10

    if "computer vision" in role:
        score += 10

    if "generative ai" in role:
        score += 15

    return score
