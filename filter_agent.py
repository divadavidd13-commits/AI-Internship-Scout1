def filter_internships(internships):

    keywords = [
        "AI",
        "Machine Learning",
        "Data",
        "Data Science",
        "Data Engineer",
        "Software",
        "Developer",
        "Cloud",
        "AWS",
        "Azure",
        "GCP",
        "DevOps",
        "Platform",
        "Infrastructure",
        "Embedded",
        "IoT",
        "Python",
        "Engineering",
        "IT"
    ]

    filtered = []

    for internship in internships:

        role = internship["role"]

        for keyword in keywords:

            if keyword.lower() in role.lower():

                filtered.append(internship)
                break

    return filtered
