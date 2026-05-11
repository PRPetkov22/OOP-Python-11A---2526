from Main_character_iterator import Main_character_iterator

characters = [
    {"name": "Ириней Константинов", "role": "Главен герой, интелектуалец", "appearances": 50, "importance": 10, "group": "главен"},
    {"name": "Борис Морев", "role": "Второстепенен герой, приятел", "appearances": 30, "importance": 8, "group": "второстепенен"},
    {"name": "Фауст", "role": "Епизодичен герой", "appearances": 5, "importance": 3, "group": "епизодичен"},
    {"name": "Ирина", "role": "Главна героиня", "appearances": 40, "importance": 9, "group": "главен"},
    {"name": "Павел Морев", "role": "Второстепенен герой", "appearances": 20, "importance": 7, "group": "второстепенен"},
    {"name": "Костов", "role": "Епизодичен герой", "appearances": 10, "importance": 5, "group": "епизодичен"},
    {"name": "Борис Морев", "role": "Главен герой", "appearances": 45, "importance": 10, "group": "главен"},
    {"name": "Лили", "role": "Второстепенна героиня", "appearances": 15, "importance": 6, "group": "второстепенен"}
]

print("1. Имена на всички герои:")
char_iter = iter(characters)
for _ in characters:
    char = next(char_iter)
    print(char['name'])

print("\n2. Главни герои:")
main_iter = Main_character_iterator(characters)
for char in main_iter:
    print(char['name'])

print("\n3а. Сортирани по име (възходящо):")
sorted_by_name = sorted(characters, key=lambda x: x['name'])
for char in sorted_by_name:
    print(char['name'])

print("\n3б. Сортирани по важност (низходящо):")
sorted_by_importance = sorted(characters, key=lambda x: x['importance'], reverse=True)
for char in sorted_by_importance:
    print(f"{char['name']} - {char['importance']}")

print("\n3в. Сортирани по брой появявания (низходящо):")
sorted_by_appearances = sorted(characters, key=lambda x: x['appearances'], reverse=True)
for char in sorted_by_appearances:
    print(f"{char['name']} - {char['appearances']}")

group_order = {'главен': 0, 'второстепенен': 1, 'епизодичен': 2}
print("\n4. Сортирани по група, важност (низходящо), име (възходящо):")
sorted_multi = sorted(characters, key=lambda x: (group_order[x['group']], -x['importance'], x['name']))
for char in sorted_multi:
    print(f"{char['group']} - {char['importance']} - {char['name']}")

def important_characters(characters):
    for char in characters:
        if char['importance'] > 7:
            yield char

print("\n5. Важни герои (важност > 7):")
for char in important_characters(characters):
    print(f"{char['name']} - {char['importance']}")