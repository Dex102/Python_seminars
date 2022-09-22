def numbers_langs(number):
    result = []
    sum = 0

    for i, j in number:
        for l in j:
            sum += ord(l)
        if sum % i == 0:
            result.append((sum, j))
    return result

programming_languages = ['Python', 'C#', 'Java', 'Java_script', 'C++', 'PHP', 'Ruby']
programming_languages = list(map(lambda lang: lang.upper(), programming_languages))

numbers = [i for i in range(1, len(programming_languages) + 1)]

lang_numbers = list(zip(numbers, programming_languages))
print(lang_numbers)

print(numbers_langs(lang_numbers))


