from jobsplatform.models import Job
from organizer.models import Tag
from organizer.models import Company, Partner
from resume.models import Skill, Experience, Task, Institution, Education, Contact, Link, Resume

from datetime import datetime

sk1 = Skill.objects.create(
    name="Dog Walker",
    description="Walks dogs around the park",
)

sk2 = Skill.objects.create(
    name="Web Designer",
    description="Designs web sites",
)

cp1 = Company.objects.create(
    name='Cool Walker',
    location='NY/New York'
)

exp1 = Experience.objects.create(
    company=cp1,
    started_at=datetime.today(),
    current=False
)

tsk1 = Task.objects.create(
    experience=exp1,
    description='This is a description',
)

ins1 = Institution.objects.create(
    name='Cool School',
    location='NY/Brooklyn'
)

ins2 = Institution.objects.create(
    name='Cool University',
    location='NY/New York'
)

ed1 = Education.objects.create(
    degree_type='HS',
    institution=ins1,
    started_at=datetime.today(),
    ended_at=datetime.today(),
    current=False
)

exp1 = Experience.objects.create(
    company=cp1,
    started_at=datetime.today(),
    current=False
)

exp2 = Experience.objects.create(
    company=pt1,
    started_at=datetime.today(),
    current=False)

tsk1 = Task.objects.create(
    experience=exp1,
    description='This is a description',
)

ed1 = Education.objects.create(
    degree_type='HS',
    institution=ins1,
    started_at=datetime.today(),
    ended_at=datetime.today(),
    current=False
)

ed2 = Education.objects.create(
    degree_type='BS',
    institution=ins2,
    started_at=datetime.today(),
    ended_at=datetime.today(),
    current=False
)

ct1 = Contact.objects.create(
    contact_type="P",
    contact='97889172389',
)

ct2 = Contact.objects.create(
    contact_type="E",
    contact='email@example.com',
)

lk1= Link.objects.create(
    link_type='W',
    link='www.mysite.com',
)

lk2 = Link.objects.create(
    link_type='R',
    link='www.github.com/user',
)

pt1 = Partner.objects.create(
    name='Walkery Walk',
    location='NY/New York',
    contact='980912830',
    description='Makes appointments between dog walkers and customers',
    website='walkery.com',
)

rs1 = Resume.objects.create(
    title='Resume 1',
)

rs1.contacts.add(ct1)
rs1.contacts.add(ct2)
rs1.educations.add(ed1)
rs1.educations.add(ed2)
rs1.skills.add(sk1)
rs1.skills.add(sk2)
rs1.links.add(lk1)
rs1.links.add(lk2)
rs1.experiences.add(exp1)
rs1.experiences.add(exp2)
rs1.save()