favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for n in favorite_languages.keys():
    print(n.title())

friends = ['phil','sarah']
for x in favorite_languages.keys():
    if x in friends:
        language = favorite_languages[x].title()
        print(f"Hi {x.title()}, I see you love {language}!")
    else:
        print(f"Hi {x.title()}!")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    