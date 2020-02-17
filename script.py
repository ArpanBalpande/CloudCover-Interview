# importing libraries
import argparse
import json
from datetime import datetime

# Creation of the parser client
parser = argparse.ArgumentParser(description='Finding older images.')

# Collecting the arguments
parser.add_argument('path_to_file', help='Path of the file')
parser.add_argument('retention_days', type=int, help='Number of the days before which to identify the images')
parser.add_argument('object_prefix', help='Object name prefix identifier')

# Extracting the arguments
args = parser.parse_args()

# Opening file and reading the json data and storing it in a variable
with open(args.path_to_file) as file:
    data = json.load(file)

# Getting today's date
todayDate = datetime.strptime( datetime.today().strftime('%Y-%m-%d'), '%Y-%m-%d')

# Logic
for d in data:
    if d['name'][:4] == args.object_prefix:
        fileDate = datetime.strptime(d['creationTimestamp'][:10], '%Y-%m-%d')
        if ((todayDate-fileDate).days >= args.retention_days):
            # print("Deleting file", d['name'])
            print("File", d['name'], "is" ,(todayDate-fileDate).days, "days old. i.e Greater than the Retention days of", args.retention_days ,"Hence - Deleting")
        else:
            print("File", d['name'], "is" ,(todayDate-fileDate).days, "days old. i.e Lesser than the Retention days of", args.retention_days ,"Hence - Retaining")