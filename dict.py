# declaram si initializam un dict
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}

# adaugam elemente
note_elevi['Sebi'] = 7

# printam dictul
print(note_elevi)

# aflam note
print(note_elevi['Sebi'])
print(note_elevi['Gigel'])
print(note_elevi.get('Ana'))

# actualizam valori
note_elevi['Costel'] = 10
print(note_elevi)

# aflam dimensiunea
print(len(note_elevi))

# stergem valori
note_elevi.pop('Ana')
print(note_elevi)
print(note_elevi.get('Ana', 'exmatriculat'))

# returneaza doar cheile
print(note_elevi.keys())
