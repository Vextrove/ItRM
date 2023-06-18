import gzip
import json
import os
from collections import Counter


def get_file_paths():
    """Obtains file paths of tweets"""
    file_paths_before, file_paths_after = [], []
    for root, dirs, files in os.walk('./tweets'):
        for file in files:
            if int(file[:4]) < 2017:
                file_paths_before.append(os.path.join(root, file))
            else:
                file_paths_after.append(os.path.join(root, file))
    return file_paths_before, file_paths_after


def extract_tweets(file_paths):
    '''Extracts a list of tweets from files in a given list of file paths'''
    tweets = []
    for file_path in file_paths:
        with gzip.open(file_path, 'rt') as raw_tweets:
            for tweet in raw_tweets:
                tweet = json.loads(tweet)['text']
                if tweet[0:2] != 'RT':
                    tweets.append(tweet)
    return tweets


def count_conjunctions(tweet, conjunctions, hits):
    '''Counts occurrences of each conjunction in a given list of words'''
    trigger_words = open("conjunctions.txt", "r").read().split()
    hit = False

    for word in tweet.split():
        if word in trigger_words:
            conjunctions[word] += 1
            hit = True

    if hit is True:
        hits += 1

    return conjunctions, hits


def main():
    '''Runs the module with a test sentence containing a conjunction'''
    file_paths_before, file_paths_after = get_file_paths()
    tweets = extract_tweets(file_paths_before)

    conjunctions = Counter()
    trigger_words = open("conjunctions.txt", "r").read().split()
    for word in trigger_words:
        conjunctions[word] = 0
    hits = 0

    for tweet in tweets:
        conjunctions, hits = count_conjunctions(tweet, conjunctions, hits)
    print(conjunctions)
    print(hits)


if __name__ == "__main__":
    """Only runs the main function if this code is run directly rather than imported"""
    main()
