import json
import os


def find_new_internships(current_results):

    if not os.path.exists(
        "history.json"
    ):
        return current_results

    with open(
        "history.json",
        "r"
    ) as file:

        history = json.load(file)

    history_jobs = set()

    for internship in history:

        key = (
            internship["company"].lower(),
            internship["role"].lower()
        )

        history_jobs.add(key)

    new_internships = []

    for internship in current_results:

        key = (
            internship["company"].lower(),
            internship["role"].lower()
        )

        if key not in history_jobs:

            new_internships.append(
                internship
            )

    return new_internships
