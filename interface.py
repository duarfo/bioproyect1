from Sequence import *


def protein_display(protein):
    # It is a display function that makes the display of the protein more simple and easier to read. It needs a protein
    # object in order to work properly.
    print('Your protein has', len(protein.base_sequence), 'Base Sequences')
    print('It has', (len(protein.amino_list) - 1), 'amino acids and a weight of', protein.Kda_weight, 'KDa')
    while True:
        print('Type "a" to see the amino acid sequence, "b" to see the base sequence and "q" to quit')
        answer = input('>')
        if answer == 'a':
            x = len(protein.amino_list)
            y = x / 10
            print_size = 10
            y_ground = math.floor(y)
            if x <= print_size:
                print(protein.amino_list)
            if x > print_size:
                s_index = 0
                n_index = print_size
                for c in range(int(y_ground)):
                    print(protein.amino_list[s_index:n_index])
                    s_index += print_size
                    n_index += print_size
                    if n_index >= x:
                        print(protein.amino_list[s_index:])
        if answer == 'b':
            x = len(protein.base_list)
            y = x / 10
            print_size = 10
            y_ground = math.floor(y)
            if x <= print_size:
                print(protein.base_list)
            if x > print_size:
                s_index = 0
                n_index = print_size
                for c in range(int(y_ground)):
                    print(protein.base_list[s_index:n_index])
                    s_index += print_size
                    n_index += print_size
                    if n_index >= x:
                        print(protein.base_list[s_index:])
        if answer == 'q':
            break


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

    suspect_proteins = s.compare(size, error)

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
                    protein_display(b)
            else:
                break
