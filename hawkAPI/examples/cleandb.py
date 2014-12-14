from pymongo import *
import sys
import argparse


usage = 'cleandb -c "client"'
parser = argparse.ArgumentParser(description="Delete Database from mongo",epilog=usage)
parser.add_argument("-c","--client",help="clientdb",type=str,required=True)
opt = parser.parse_args()
if len(sys.argv) < 1:
     parser.print_help()
     sys.exit()

client = MongoClient('localhost', 27017)
c = Connection()
c.drop_database(opt.client)
