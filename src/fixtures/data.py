from faker import Faker

from organizer.models import (
    Tag,
    Company,
    Partner,
    Job
)
from resume.models import (
    Skill,
    Experience,
    Institution,
    Education,
    Personal,
    Other,
    Resume,
    ApplicationSubmission,
)

from datetime import datetime
from random import randint

faker = Faker()

tags_number = 20
skills_number = 10
locations_number = 10
companies_number = 10
partners_number = 10
personal_number = 10
experiences_number = 15
institutions_number = 10
educations_number = 10
other_number=10
degrees_number = 10
resumes_number = 5
jobs_number = 10
applications_number = 10

# Tags fixtures
Tag.objects.all().delete()
Company.objects.all().delete()
Partner.objects.all().delete()
Personal.objects.all().delete()
Experience.objects.all().delete()
Institution.objects.all().delete()
Education.objects.all().delete()
Skill.objects.all().delete()
Resume.objects.all().delete()
print("Deleted all previous data")


set_tags = set([faker.word() for _ in range(tags_number)])
tags = []
for tag in set_tags:
    tags.append(Tag.objects.create(name=tag.title()))

print(f"Added tags {len(tags)}")

# Companies and Partners fixtures
locations = [faker.address() for _ in range(locations_number)]

companies = [
    Company.objects.create(
        name=f"{' '.join(faker.words(3)).title()}",
        location=locations[i%len(locations)],
    )
    for i in range(companies_number)
]
for cp in companies:
    for _ in range(2):
        choice = randint(0, len(tags)-1)
        cp.tags.add(tags[choice])


partners = []
for i in range(partners_number):
    name = faker.words(3)
    partners.append(
        Partner.objects.create(
            name=f"{' '.join(name).title()}",
            location=locations[i%len(locations)],
            email=f"contact@{''.join(name)}.com",
            description=f"{faker.text()}",
            website=f"{''.join(name)}.com",
        )
    )

for pt in partners:
    for _ in range(3):
        choice = randint(0, len(tags)-1)
        pt.tags.add(tags[choice])

print(f"Added Companies {len(companies)} and partners {len(partners)}")

# Personal contact fixtures
def get_personal_type(type):
    if type == "P":
        return faker.phone_number()
    if type == "E":
        return faker.email()
    elif type == "R":
        return f"github.com/{faker.slug()}"
    elif type == "W":
        return faker.domain_name()
    else:
        return f"twitter.com/{faker.slug()}"

personal_type = ["P", "E", "R", "W", "O"]
personal = [
    Personal.objects.create(
        personal_type=personal_type[i%5],
        data=get_personal_type(personal_type[i%5]),
    )
    for i in range(personal_number)
]
print(f"Added personal contacts {len(personal)}")
# Experiences fixtures

exps = [
    Experience.objects.create(
        job_title=faker.job(),
        company=companies[i%companies_number].name,
        location=" ".join(locations[i%locations_number].split(' ')[-3:-1]),
        started_at=faker.date_time_this_decade(),
        ended_at=faker.date_time_this_year(),
        current=False,
        tasks=f'{faker.text()}\n{faker.text()}\n{faker.text()}'
    )
    for i in range(experiences_number)
]
print(f"Added experiences {len(exps)}")

# Institutions fixtures
school_types = ["High School", "College", "University", "Institute"]
ins = [
    Institution.objects.create(
        name=f"{' '.join(faker.words(2))} {school_types[i%4]}",
        location=locations[i%locations_number]
    )
    for i in range(institutions_number)
]
print(f"Added institutions {len(ins)}")

# Education fixtures
ed_options = ["Science", "Art", "Therapy"]
degree_types = ["HSI", "HS", "AS", "AAS", "BS", "BA", "MS", "MA", "Phd"]
degrees = [el for el in set([f'{faker.word().title()} {ed_options[i%3]}' for i in range(degrees_number)])]
eds = [
    Education.objects.create(
        degree_type=degree_types[i%len(degree_types)],
        degree=degrees[i%len(degrees)],
        institution=ins[i%institutions_number],
        started_at=faker.date_time_this_decade(),
        ended_at=faker.date_time_this_decade(),
        current=False,
    )
    for i in range(educations_number)
]
print(f"Added educations {len(eds)}")

# Skills fixtures
set_skills = set([' '.join(faker.words(2)).title() for i in range(skills_number)])
skills = []
for skill in set_skills:
    skills.append(
        Skill.objects.create(
            name=skill,
            description=faker.text(),
        )
    )
print(f"Added Skills {len(skills)}")

for sk in skills:
    for _ in range(2):
        choice = randint(0, len(tags)-1)
        sk.tags.add(tags[choice])
print(f"Added Tags to Skills")

# Other fixtures
other_possible = ["Reference", "Note"]
others = [
    Other.objects.create(
        type_data=other_possible[i%len(other_possible)],
        data=" ".join(faker.words(5)).title()
    ) for i in range(other_number)
]

# Resumes fixtures
resumes = [
    Resume.objects.create(
        title=f"{' '.join(faker.words(2)).title()}",
    )
    for i in range(resumes_number)
]

ps_num = [i for i in range(len(personal))]
ed_num = [i for i in range(len(eds))]
sk_num = [i for i in range(len(skills))]
ex_num = [i for i in range(len(exps))]
other_num = [i for i in range(len(others))]

for r in resumes:
    for _ in range(int(len(personal)/len(resumes))):
        r.personal.add(personal[ps_num.pop()])
    for _ in range(int(len(exps)/len(resumes))):
        r.experiences.add(exps[ex_num.pop()])
    for _ in range(int(len(eds)/len(resumes))):
        r.educations.add(eds[ed_num.pop()])
    for _ in range(int(len(skills)/len(resumes))):
        r.skills.add(skills[sk_num.pop()])
    for _ in range(int(len(others)/len(resumes))):
        r.other.add(others[other_num.pop()])
    r.save()

print(f"Added resumes {len(resumes)}")

# Jobs fixtures
Job.objects.all().delete()
jobs = [
    Job.objects.create(
        title=f"{faker.job()}",
        text=faker.text(),
        pub_date=faker.date_time_this_year(),
        partner=partners[i%len(partners)],
    )
    for i in range(jobs_number)
]
for job in jobs:
    for _ in range(5):
        choice = randint(0, len(tags)-1)
        job.tags.add(tags[choice])
print(f"Added jobs {len(jobs)}")

# ApplicationSubmission fixtures
ApplicationSubmission.objects.all().delete()
apps = 0
for i in range(applications_number):
    ApplicationSubmission.objects.create(
        job=jobs[i%len(jobs)],
        resume=resumes[i%len(resumes)]
    )
    ApplicationSubmission.objects.create(
        job=jobs[i%len(jobs)],
        resume=resumes[(i+5)%len(resumes)]
    )
    apps += 2
print(f"Added submissions {apps}")
