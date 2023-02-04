
## Curriculum Vitae


Names = 'Muinat Abiola Olagunju'
print(type(Names))
print(Names)

Email = 'muinatabiola@gmail.com'
print(type(Email))
print(Email)

PhoneNumber = '+234703743589961'
print(type(PhoneNumber))
print(PhoneNumber)

Skills = {
        'Dental skills': ['Oral surgery','Oral pathology',' Restorative and Preventive dentistry'],
        'IT skills':['Ms Word','Excel','Powerpoint'],
        'Language skills':['English','Yoruba','German']
        }
print(type(Skills))
for s, v in Skills.items():
    print(s,v)

Education = {
    '2009 - 2016':'University of Lagos, Nigeria',
    'Certificate': 'BDS. Bachelor of Dental Surgery',
    '2001 - 2007': 'Anchor Mirrors Model College, Lagos',
    'Certificate': 'Senior School Certificate Exam'
    }

print(type(Education))
for k, v in Education.items():
    print(k,v)

WorkExperience = [
    {'2020 - 2021':'Don Dental Clinic,Lagos','Role': 'Dentist'},
    {'2019 - 2020':'Green Fountain Dental Clinic,Lagos','Role':'Dentist'},
    {'2018 - 2019': 'Lagos University teaching Hospital, Lagos','Role':'Intern'}
    ]

print(type(WorkExperience))
print(WorkExperience)

