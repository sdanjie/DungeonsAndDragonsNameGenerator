# CSC121 Lab: Name Generator 
# This program reads a file's contents into a list. 
# Danjie Song
# 10/25/2016
import random

def main():
    
    # Get the lists
    nameList = loadFile("names.txt")
    titleList = loadFile("titles.txt")   
    descrList = loadFile("descriptors.txt")
    
    # Generate 10 character names
    NUMBER_OF_CHARACTERS = 10
    characters = [''] * NUMBER_OF_CHARACTERS
    for count in range(10):
        characters[count] = generateChar(nameList, titleList, descrList)
        print(characters[count])
       
    # Write to a file
    dumpFile(characters)
    print('\nThe characters have been saved to characterName.txt.')

def loadFile(txtFile):
    infile = open(txtFile, 'r')
    array = infile.readlines()
    infile.close()   
    for index in range(len(array)):
        array[index] = array[index].rstrip('\n')
    return array

def generateChar(names, ttls, descrpts):
    char = ( '{0} {1} {2} the {3}'.format(ttls[generateRadomIndex(ttls)],\
            names[generateRadomIndex(names)], \
            names[generateRadomIndex(names)], \
            descrpts[generateRadomIndex(descrpts)]))
    return char 

def generateRadomIndex(list):
    return random.randrange(len(list));

def dumpFile(array):
    outfile = open('CharacterNames.txt', 'w')
    for item in array:
        outfile.write(item + '\n')
    outfile.close()
main()