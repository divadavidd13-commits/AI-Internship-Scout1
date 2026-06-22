# AI Internship Scout

An AI-powered internship discovery system that automates internship searching, filtering, verification, ranking, and notification.

## Features

* Search internship opportunities using LinkedIn
* Filter internships by preferred location
* Verify opportunities using Gemini AI
* Rank internships using a custom scoring algorithm
* Save internship data automatically
* Track internship history
* Email shortlisted opportunities
* Modular agent-based architecture

## Tech Stack

* Python
* Gemini API
* Requests
* BeautifulSoup4
* JSON
* SMTP (Email Automation)

## Project Structure

main.py                  # Main workflow controller
search_linkedin.py       # Internship search agent
location_filter_agent.py # Location filtering
verification_agent.py    # Internship verification
gemini_verification.py   # Gemini AI validation
ranking_agent.py         # Internship scoring
filter_agent.py          # Additional filtering
save_results.py          # Save results
compare_results.py       # Compare opportunities
email_agent.py           # Email notifications
config.py                # Configuration settings

## Installation

pip install -r requirements.txt

## Run

python main.py

## Workflow

User Input
→ Search Agent
→ Location Filter Agent
→ Verification Agent
→ Ranking Agent
→ Save Results
→ Email Agent

## Authors

* Harshinidevi R
* Dhivashyajos D

