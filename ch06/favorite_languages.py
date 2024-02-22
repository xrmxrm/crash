favorite_languages = {
      'horace': [],
      'jen': ['python', 'rust'],
      'sarah': ['c'],
      'edward': ['rust', 'go'],
      'phil': ['python', 'haskell'],
      }

for name, languages in favorite_languages.items():
    test_len = len(languages)
    if test_len == 0:
        print(f"\n{name.title()}'doesn't play favorites.")
    elif test_len == 1:
        print(f"\n{name.title()}'s favorite languages is {languages[0]}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}", end=' ')
        
    print("\n\n")

people_to_poll = ['jen', 'jack', 'sally', 'phil', 'george']

for name in people_to_poll:
    if name in favorite_languages.keys():
        print(f"Thanks, {name.title()}, for responding!")
    else:
        print(f"{name.title()}, please take the survey. Thanks.")

print("\n\n")