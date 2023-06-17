from random import random, randrange


def main():
    '''Creates a batch file containing $scp commands to download tweets'''
    years = ['2016', '2017', '2018']
    months = [str(month).zfill(2) for month in range(1, 13)]
    hours = [str(hour).zfill(2) for hour in range(24)]
    username = open("username.txt", "r").read()
    random.seed(open("seed.txt", "r").read())
    print(randrange(24))
    random.seed(open("seed.txt", "r").read())
    print(randrange(24))

    for year in years:
        for month in months:
            print('scp', username + '@karora.let.rug.nl:/net/corpora/twitter2/Tweets/' + year + '/' + month + '/' + year + month + '01' + ':' + hours[randrange(24)] + '.out.gz ./Tweets')


if __name__ == "__main__":
    """Only runs the main function if this code is run directly rather than imported"""
    main()
