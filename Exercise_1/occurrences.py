import string

while True:
    # Check for the constraints of n
    n = int(input("Input the number of test cases: "))
    if n < 1 or n > 10**5:
        print("Error: Invalid value for n (1 ≤ n ≤ 10^5)")
        break

    word_count = {}
    for i in range(n):
        word = input(f"Input word {i + 1}: ")
        # Check for the constraints of words
        if not 1 <= len(word) <= 10 ** 6:
            print('Error: Word should be between 1 and 10^6 characters long')
            break
        if not all(letter in string.ascii_lowercase for letter in word):
            print('Error: Word should only contain lowercase letters')
            break

        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1

    else:
        print(len(word_count))
        print(*word_count.values())
        break
