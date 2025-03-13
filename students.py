students = [
    {
        'first_name': 'Kayra',
        'last_name': 'Çelikoğlu',
        'index_number': 35357,
        'nationality': 'Turkish',
        'starting_date': '29.07.2025',
        'courses': ["Math", "OOP", "Polish", "İntro digi tech", "Telecommunications", "Marketing"]
    },
    {
        'first_name': 'Irmak',
        'last_name': 'Bicerbay',
        'index_number': 35451,
        'nationality': 'Turkish',
        'starting_date': '12.03.2025',
        'courses': ["Math", "Physics", "Programming", "History"]
    },
    {
        'first_name': 'Mehmet',
        'last_name': 'Demir',
        'index_number': 35359,
        'nationality': 'Turkish',
        'starting_date': '31.07.2025',
        'courses': ["Marketing", "Economics", "Business Law", "Statistics"]
    }
]

for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}")
