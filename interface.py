from Sequence import *


def compare():
    suspect_protein = []
    for protein in s.protein_object_list:
        x = protein.Kda_weight / float(size)
        if (1 + float(error)) >= x >= (1 - float(error)):
            suspect_protein.append(protein)
    return suspect_protein


while True:

    print('Hello!')
    print('Bioproyect1 is a tool designed to help you find a possible sequence for your protein!')
    print('You need a genome in FASTA format to start as well as a weight in KDa to compare it with')
    print('Please input your full FASTA sequence file name or "q" to quit')

    val = input('>')
    if val == "q":
        break

    s = Sequence(val)

    print('Perfect!')
    print('Now what is the size of the unknown protein in KDa?(Write just the number)')

    size = input('>')

    print('What is the weight percentage error you want to get in your search?')
    print('Make sure it is a number between 0 and 1, the smaller the number the more precise')

    error = input('>')

    suspect_proteins = compare()
    print('We found', len(suspect_proteins), 'proteins with comparable sizes')

    if len(suspect_proteins) > 0:
        while True:
            print('Witch one would you like to see? (type in a number between 1 and', len(suspect_proteins),
                  'type something else to quit)')
            index = (input('>'))
            if index.isalpha():
                break
            if index.isdigit():
                if int(index) <= len(suspect_proteins):
                    index0 = (int(index) - 1)
                    b = suspect_proteins[index0]
                    b.protein_display()
            else:
                break
