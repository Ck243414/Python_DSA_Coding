def non_repeating(s : str) -> str | None:
    from collections import Counter
    string = s.lower()
    frequency = Counter(string)
    for ch in string:
        if frequency[ch] == 1:
            return ch 
    return None
string = "Swiss"
print(non_repeating(string))
