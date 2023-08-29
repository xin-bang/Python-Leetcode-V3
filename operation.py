#usr/bin/python 
import pandas as pd
from Bio import SeqIO
import argparse 

parser = argparse.ArgumentParser(
    description="Catch 'fish fasta' according the 'bait fasta id'"
    )
parser.add_argument("-f1",type=str,
                    help="fish fasta")
parser.add_argument("-f2",type=str,
                    help="bait file contain the fasta id you need")
args = parser.parse_args()



def get_fasta(file_name,index):

    column = ["Fasta_id","Fasta_len(bp)","Fasta_seq"]
    bait = []
    fish = []
    with open (index,"r") as index:
        for index_Id in index:
            bait.append(index_Id.strip())

    with open(file_name, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            for i in bait:
                if record.description == i:
                    j = record.id +"\t" + str(len(record.seq)) + "\t" + str(record.seq) #record.seq结尾处默认带有"\n"
                    fish.append(j)
                else:
                    pass
    fish = [x.split("\t") for x in fish]
    fish_pd = pd.DataFrame(fish,columns=column)
    return fish_pd



def main():
    fish = get_fasta(args.f1,args.f2)
    fish.to_csv("fish.txt",sep="\t",index=False)

if __name__ == "__main__":
    main()



