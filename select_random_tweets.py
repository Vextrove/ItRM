import random


def main():
    '''Creates a batch file that downloads tweets from a random hour on a random day every other month'''
    username = open("username.txt", "r").read()
    random.seed(open("seed.txt", "r").read())

    with open("download_tweets.bat", "w") as output:
        for year in ['2016', '2017', '2018']:
            for month in [str(month*2).zfill(2) for month in range(1, 7)]:
                text = (
                    f"scp {username}@karora.let.rug.nl:/net/corpora/twitter2/Tweets/{year}/{month}/{year}{month}"
                    f"{str(random.randrange(1, 29)).zfill(2)}:{str(random.randrange(24)).zfill(2)}.out.gz ./tweets\n"
                )
                output.write(text)


if __name__ == "__main__":
    """Only runs the main function if this code is run directly rather than imported"""
    main()
