def count_vowels(arr):
    vowels = ['a','e','i','o','u']
    count = 0
    for ch in arr.lower():
        if ch in vowels:
            count += 1
    return count

def count_consonants(arr):
    vowels = ['a','e','i','o','u']
    count = 0
    for ch in arr.lower():
        if not ch in vowels and ch.isalpha():
            count += 1
    return count

def main():
    string = input('Enter a string of characters: ')
    v = count_vowels(string)
    c = count_consonants(string)
    print(
        'There are '+str(count_vowels(string))+' vowels, '+\
        'and '+str(count_consonants(string))+' consonants.'
    )

main()