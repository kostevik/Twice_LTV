import sys
import json
import string

def create_database(infile):
    infile = open(infile)
    header = ['UserID', 'Trans_type', 'Date', 'Amount']
    database = {}
    for index, line in enumerate(infile):
        data = line.strip('\n\r').split() # collects the data
        entry = dict(zip(header, data)) # packs it into a nice map for reference
        database[index] = entry
    infile.close() # important to close files if program runs a long time
    for transaction in database:
        print database[transaction]['Trans_type']
    #print database
    return database

def create_transation_type_plot:
    


def categorize_users(database):
    print database[0]['UserID']
    purchasers = {}
    sellers = {}
    both = {}
    #for transaction in database:
     #   if 
    return purchasers, sellers, both

#def match(tweets, scores):

def main():
    database = create_database('twice_transactions.txt')
    purchasers, sellers, both = categorize_users(database)


if __name__ == '__main__':
    main()
