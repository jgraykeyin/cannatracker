import os
import boto3

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Establish a connection to AWS S3
s3 = boto3.resource("s3")
bucket = s3.Bucket("cannabucket")
bucket.download_file("strains.txt",os.path.join(__location__,"strains.txt"))

def gatherFileData(filename,mode):
    '''
        Description: Opens a file and reads all content of file. 
        It then takes each line and dumps it into a list using readlines().
        Returns a list
    '''
    data = open(os.path.join(__location__,filename),mode)
    data_content = data.readlines()
    data.close()

    return data_content

def getStrains():
    '''
        Description: Get the list of strains from the file and append into a python list.
        Returns a list
    '''
    strains = []
    strain_content = gatherFileData("strains.txt","r")
    
    for s in strain_content:
        
        s_content = s.split(":")
        d = {"name":s_content[0],"type":s_content[1],"thc":s_content[2],"cbd":s_content[3],"form":s_content[4]}
        
        strains.append(d)
    
    return strains

def addNewStrain():
    '''
        Description: Adds a new strain into the list of available strains and uploads it back to S3 bucket
    '''

    s_name = input("Strain name: ")
    s_type = input("Type (Salvia, Indica, Hybrid): ")
    s_thc = input("THC content in %: ")
    s_cbd = input("CBD content in %: ")
    s_form = input("Form (Whole Flower, Oil, Edible)")

    

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

        print("\nSelect Strain [#] to create new journal entry")
        print("Other commands: [A]dd new strain // [Q]uit")
        user_cmd = input(">> ")

        if user_cmd.lower() == "q":
            break
        elif user_cmd.lower() == "a":
            addNewStrain()


appLoop()