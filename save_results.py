import json
import os


def save_results(internships):

    # Latest results
    with open(
        "internships.json",
        "w"
    ) as file:

        json.dump(
            internships,
            file,
            indent=4
        )

    # Load history
    history = []

    if os.path.exists(
        "history.json"
    ):

        with open(
            "history.json",
            "r"
        ) as file:

            history = json.load(file)

    # Existing jobs
    existing = set()

    for internship in history:

        key = (
            internship["company"].lower(),
            internship["role"].lower()
        )

        existing.add(key)

    # Add new jobs
    for internship in internships:

        key = (
            internship["company"].lower(),
            internship["role"].lower()
        )

        if key not in existing:

            history.append(
                internship
            )

            existing.add(key)

    # Save history
    with open(
        "history.json",
        "w"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )
