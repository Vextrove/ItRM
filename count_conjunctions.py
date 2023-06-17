from collections import Counter


def count_conjunctions(text):
    '''Counts occurrences of each conjunction in a given list of words'''
    conjunctions = Counter()
    trigger_words = open("conjunctions.txt", "r").read().split()

    for word in trigger_words:
        conjunctions[word] = 0

    for word in text:
        if word in trigger_words:
            conjunctions[word] += 1

    return conjunctions


def main():
    '''Runs the module with a test sentence containing a conjunction'''
    text = "Deze zin bevat een conjunctie, waardoor iets zal gebeuren"
    print(count_conjunctions(text.split()))


if __name__ == "__main__":
    """Only runs the main function if this code is run directly rather than imported"""
    main()
