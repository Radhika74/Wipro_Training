def frequency_of_letters(name):
    frequency = {}
    for i in name:
        if i != " ":
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
    return ", ".join(f"{k}-{v}" for k, v in frequency.items())
