import re

def filter_internships(internships):

    hard_reject_patterns = [
        r"\bsenior\b",
        r"\bsr\b",
        r"\bstaff\b",
        r"\bprincipal\b",
        r"\blead\b",
        r"\bmanager\b",
        r"\bdirector\b",
        r"\bvp\b",
        r"\bvice president\b",
        r"\bhead\b",
        r"\bchief\b",
        r"\barchitect\b",
        r"\bconsultant\b",
        r"\badministrator\b",
        r"\badmin\b"
    ]

    hard_accept_patterns = [
        r"\bintern\b",
        r"\binternship\b",
        r"\bco-op\b",
        r"\btrainee\b",
        r"\bapprentice\b",
        r"\bresearch intern\b",
        r"\bsummer intern\b"
    ]

    accepted = []

    for internship in internships:

        role = internship["role"].lower()

        # ----------------------------
        # Stage 1 : Hard Reject
        # ----------------------------

        rejected = False

        for pattern in hard_reject_patterns:

            if re.search(pattern, role):

                rejected = True
                break

        if rejected:
            continue

        # ----------------------------
        # Stage 2 : Hard Accept
        # ----------------------------

        accepted_role = False

        for pattern in hard_accept_patterns:

            if re.search(pattern, role):

                accepted_role = True
                break

        if accepted_role:

            accepted.append(internship)
            continue

        # ----------------------------
        # Stage 3 : Score Ambiguous Jobs
        # ----------------------------

        score = 0

        scoring_keywords = {
            "ai": 20,
            "machine learning": 20,
            "ml": 15,
            "data science": 15,
            "computer vision": 15,
            "nlp": 15,
            "software engineer": 10,
            "developer": 10,
            "python": 10,
            "cloud": 10,
            "devops": 10,
            "embedded": 10,
            "iot": 10,
            "cybersecurity": 10,
            "research": 10
        }

        for keyword, points in scoring_keywords.items():

            if keyword in role:
                score += points

        if score >= 70:
            accepted.append(internship)

    return accepted
