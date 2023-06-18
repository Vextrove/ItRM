import gzip
import json
import os
from collections import Counter

TRIGGER_WORDS = open("conjunctions.txt", "r").read().split()
includeRetweets = False


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
                elif includeRetweets is True:
                    tweets.append(tweet)

        print('Extracted', str(file_paths.index(file_path) + 1).zfill(1), 'out of', str(len(file_paths)), 'tweets...')
    return tweets


def count_conjunctions(tweet, conjunctions, hits):
    '''Counts occurrences of each conjunction in a given list of words'''
    hit = False

    for word in tweet.split():
        if word in TRIGGER_WORDS:
            conjunctions[word] += 1
            hit = True

    if hit is True:
        hits += 1
    return conjunctions, hits


def main():
    '''Runs the module with a test sentence containing a conjunction'''
    file_paths_before, file_paths_after = get_file_paths()
    conjunctions_before, conjunctions_after = Counter(), Counter()
    for word in TRIGGER_WORDS:
        conjunctions_before[word], conjunctions_after[word] = 0, 0
    hits_before, hits_after = 0, 0

    print('Extracting tweets...')
    tweets_before = extract_tweets(file_paths_before)
    print('\nExtracting more tweets...')
    tweets_after = extract_tweets(file_paths_after)

    try:
        for tweet in tweets_before:
            conjunctions_before, hits_before = count_conjunctions(tweet, conjunctions_before, hits_before)
        for tweet in tweets_after:
            conjunctions_after, hits_after = count_conjunctions(tweet, conjunctions_after, hits_after)
    except KeyboardInterrupt:
        pass

    conjunction_count_before = sum(conjunctions_before.values())
    conjunction_count_after = sum(conjunctions_after.values())
    tweet_amount_before, tweet_amount_after = len(tweets_before), len(tweets_after)

    print('\nAmount of measured tweets')
    print('Before 2017:', tweet_amount_before)
    print('After 2017:', tweet_amount_after)

    print('\nAmount of conjunctions per tweet')
    print('Before 2017:', round(conjunction_count_before / tweet_amount_before, 5))
    print('After 2017:', round(conjunction_count_after / tweet_amount_after, 5))

    print('\nPercentage of tweets containing conjunctions')
    print('Before 2017:', str(round(100 * hits_before / tweet_amount_before, 2)) + '%')
    print('After 2017:', str(round(100 * hits_after / tweet_amount_after, 2)) + '%')

    print('\nFrequency of each conjunction')
    print('Before 2017:', conjunctions_before)
    print('After 2017:', conjunctions_after)


if __name__ == "__main__":
    """Only runs the main function if this code is run directly rather than imported"""
    main()
