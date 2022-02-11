import json

datas = [
    {
        'name': 'Katherine J. Baron',
        'address': '1801 Buck Drive, Kearns, UT 84118',
        'phone_number': '801-982-3001',
        'e_mail': 'KatherineJBaron@teleworm.us',
        'website': 'deejayjaycee.com',
        'skills': [
            {
                'skill': '- Database design'
            },
            {
                'skill': '- Implementation and Management'
            },
            {
                'skill': '- Software Development'
            },
            {
                'skill': '- Frameworks'
            },
            {
                'skill': '- Games and Virtual Reality Software Design'
            },
            {
                'skill': '- User Interface Design'
            }
        ],
        'job1': 'Game Programmer',
        'job2': 'Game Programmer',
        'experience1': [
            {
                'date': '2002-2008',
                'company': 'Roblox',
                'place': 'Ottawa, Canada',
                'desc': '- Develop and program games and gaming systems for children'
            }
        ],
        'experience2': [
            {
                'date': '2009-2014',
                'company': 'Riot',
                'place': 'Moscow, Russia',
                'desc': '- Write code to determine the mechanics and gameplay of new software'
            }
        ],
        'date1': '1994-1998',

        'academic': [
            {
                'school': 'Polytechnic University of the Philippines',
                'course': 'Bachelor of Science in Computer Engineering',
                'place': 'Sta. Mesa, Manila'
            }
        ]
    }
]

export = json.dumps(datas, indent=4)
with open('assignment8_data.json', 'w') as file:
    file.write(export)
    file.close()