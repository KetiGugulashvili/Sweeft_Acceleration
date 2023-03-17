import string


def bigger_Is_greater(w):
    # Check for the constraints of word
    if not 1 <= len(w) <= 10 ** 6:
        return 'Error: Word should be between 1 and 100 characters long'
    if not all(letter in string.ascii_lowercase for letter in w):
        return 'Error: Word should only contain lowercase letters'

    # Find the pivot point in the word
    w = list(w)
    pivot_index = len(w) - 1
    for i in range(pivot_index, 0, -1):
        if w[i] > w[i - 1]:
            pivot_index = i
            break
    else:
        return "No Answer"

    # Find the largest suffix of the word
    largest_suffix_index = pivot_index - 1
    for j in range(len(w) - 1, largest_suffix_index, -1):
        if w[largest_suffix_index] < w[j]:
            largest_suffix_index = j
            break

    # Swap the pivot index with the largest suffix index
    w[pivot_index - 1], w[largest_suffix_index] = w[largest_suffix_index], w[pivot_index - 1]

    # Reverse the suffix
    w[pivot_index:] = w[len(w) - 1:pivot_index - 1:-1]

    return ''.join(w)


# Check for the constraints of T and test the function
T = int(input("Input the number of test cases: "))
if T < 1 or T > 10**5:
    print("Error: Invalid value for T (1 ≤ T ≤ 10^5)")
else:
    for _ in range(T):
        word = input("Input the word: ")
        print(bigger_Is_greater(word))
