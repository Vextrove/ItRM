import random


def main():
    '''Creates a batch file that downloads tweets from a random hour on a random day every other month'''
    username = open("username.txt", "r").read()
    random.seed(open("seed.txt", "r").read())

    with open("download_tweets.bat", "w") as output:
        for year in ['2015', '2016', '2018', '2019']:
            for month in [str(month).zfill(2) for month in range(1, 13)]:
                day = str(random.randrange(1, 29)).zfill(2)
                hour = str(random.randrange(24)).zfill(2)
                text = (
                    f"scp {username}@karora.let.rug.nl:/net/corpora/twitter2/Tweets/{year}/{month}/{year}{month}"
                    f"{day}:{hour}.out.gz ./tweets/{year}_{month}_{day}_{hour}.gz\n"
                )
                output.write(text)


if __name__ == "__main__":
    """Only runs the main function if this code is run directly rather than imported"""
    main()
