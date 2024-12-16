import csv
from datetime import datetime
from Bio import Entrez
Entrez.email = "talia.baer@weizmann.ac.il"

#RUN ONLY ONCE TO CREATE THE CSV FILE:

#csv_header = ["date","database","term","max","total"]
#with open("ncbi_searches.csv", mode="w", newline="") as file:
    #writer = csv.writer(file)
    #writer.writerow(csv_header)


def ncbi_search(db, term, number):
    handle = Entrez.esearch(db=db, term=term, idtype="acc", retmax=number)
    record = Entrez.read(handle)
    idlist = record["IdList"]
    for id in idlist:
        download = Entrez.efetch(db=db, id=id, rettype="gb", retmode="text")
        data = download.read()
        download.close()
        filename = id
        with open(filename, 'w') as fh:
            fh.write(data)
        print(filename)
    search_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_search = [[search_date,db,term,number,record["Count"]]]
    with open("ncbi_searches.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(current_search)
    with open("ncbi_searches.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--database', required=False, type=str, default="nucleotide")
parser.add_argument('--term', required=True, type=str)
parser.add_argument('--number', required=False, type=int, default=10)
args = parser.parse_args()
db = args.database
term = args.term
number = args.number

ncbi_search(db, term, number)
