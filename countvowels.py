def count_vowels_consonants(s:str)-> tuple[int, int]:
    vowels =set("aeiouAEIOU")
    vowel_count = consonant_count = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                vowel_count+=1
            else:
                consonant_count+=1
    return vowel_count,consonant_count

test = input("Enter a string:")
v, c = count_vowels_consonants(test)
print(f"Vowels: {v}, Consonants: {c}")
