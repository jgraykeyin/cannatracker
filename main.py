import os
import boto3

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Establish a connection to AWS S3
s3 = boto3.resource("s3")
bucket = s3.Bucket("cannabucket")
bucket.download_file("strains.txt",os.path.join(__location__,"strains.txt"))

def getStrains():
    '''
        Description: Get the list of strains from the file and append into a python list.
        Returns a list
    '''
    strains = []
    strain_data = open(os.path.join(__location__,"strains.txt"),"r")
    strain_content = strain_data.readlines()

    for s in strain_content:
        
        s_content = s.split(":")
        d = {"name":s_content[0],"type":s_content[1],"thc":s_content[2],"cbd":s_content[3],"form":s_content[4]}
        
        strains.append(d)
    
    return strains

def appLoop():
    '''
        Description: Main loop for the program to take user input
    '''
    
    while True:
        print("-*- CannaTrackerPy 0.1 -*-")
        print("Saved strains: ")
        
        x=1
        strains = getStrains()
        for s in strains:
            print("[{}] {} ({})".format(x,s["name"],s["type"]))
            x+=1

        print("\nSelect Strain # to create new journal entry")
        print("Other commands: [A]dd new strain")
        user_cmd = input(">> ")




appLoop()