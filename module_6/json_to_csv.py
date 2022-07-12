import csv
import json
from pathlib import Path

DATA_FILE = Path('people_db.json')
RESULT_FILE = Path('invite.csv')


def rules(person):
    return all(
        (
            not person['company_name'],
            person['phone'],
            'software' in person['job_title'].lower(),
        )
    )


with open(DATA_FILE) as people_file:
    people = json.load(people_file)


with open(RESULT_FILE, 'w') as result_file:
    csv_writer = csv.DictWriter(result_file, fieldnames=people[0].keys())
    csv_writer.writeheader()
    for person in filter(rules, people):
        csv_writer.writerow(person)
