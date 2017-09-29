import re
import amino_acid_dictionary
import Weight_dictionary



class Sequence:
    # The Sequence class is in mainly charge of parsing and processing a FASTA type file into a Python readable sequence
    # ,it also keeps a list of proteins found on the sequence. All methods call themselves upon an instantiation so that
    # you can continue to process your data. The only parameter it needs is a FASTA.txt file.
    def __init__(self, fasta):
        self.f = fasta
        self.lines, self.count = self.parsing()
        self.string = "".join(self.lines)
        self.proteins_start = self.protein_search()
        self.actual_proteins = self.protein_finish()
        self.protein_object_list = self.protein_factory()

    def parsing(self):
        # Parsing is the method in charge of reading the FASTA.txt file, cleaning out the comments and names
        # and finally returning a list of lines as well as a count of characters. As long as the sequence follows FASTA
        # format it should be easy to parse.
        file = open(self.f, 'r')
        y = file.read()
        real_lines = y.split('\n')
        base_count = 0
        for element in real_lines:
            if element[0] == ">":
                real_lines.remove(element)
            elif element[0] == ';':
                real_lines.remove(element)
        for line in real_lines:
            for base in line:
                if base:
                    base_count += 1
        print('Your sequence has', base_count, 'base pairs!')
        print('Your Sequence has', len(real_lines), 'lines of code!')
        return real_lines, base_count

    def protein_search(self):
        # Protein_search is in charge of looking through the unified string of the FASTA sequence for start codons, in
        # this case only ATG. It uses partition in order to get the sequence starting at ATG and unto the end of the
        # sequence, forming a list of this possible proteins.
        protein_start = []
        split_list = self.string
        while True:
            partition_list = split_list.partition('ATG')
            pre_protein = partition_list[1] + partition_list[2]
            protein_start.append(pre_protein)
            split_list = partition_list[2]
            if len(split_list) < 4:
                break
        return protein_start

    def protein_finish(self):
        # Protein_finish comes after protein_search, it looks into the list formed by protein search un regular
        # expressions in order to find actual proteins starting with ATG, reading in a 3 base frame, and finally the
        # first stop codon it encounters, making a list of the sequence of the actual protein.
        real_proteins = []
        for element in self.proteins_start:
            pattern = r"(A[UT]G)([A-Z]{3})*?(([UT]AA)|([UT]AG)|([UT]GA))"
            search = re.search(pattern, element)
            if search:
                real_proteins.append(search.group())
        print('found', len(real_proteins), 'proteins')
        return real_proteins

    @ staticmethod
    def print_protein_list(p_list):
        # A static method created for checking functionality of the code, it was built to print lists, including all the
        # elements and the first 5 characters and the last 5 to check the regular expression as well as the length of
        # the protein it is not currently used by the program but rather for new code implementation.
        for element in p_list:
            print(element[0:5], '...', element[-5:], 'size', len(element), 'bp')

    def protein_factory(self):
        # This method starts with the list of base sequences of proteins returned by protein_finish and transforms this
        # string list into a list of Protein class objects by instantiating each string as a Protein object, it gives id
        # parameters that are needed for instantiation so that you can keep proper track of each protein object.
        list0 = []
        for idx, val in enumerate(self.actual_proteins):
            nid = idx+1
            list0.append(Protein(self.f, nid, val))
        return list0

    def compare(self, size, error):
        # The only function not called at initiation, compare is a method that is used to look for the users target
        # protein. It uses the users input in order to find the possib e protein of the user, creating an object list of
        # the match. Size is the weight in KDa of the users protein and error is the percentage of variation of this
        # weight that the user inputs, as a number form 0 to 1.
        suspect_protein = []
        for protein in self.protein_object_list:
            x = protein.Kda_weight / float(size)
            if (1 + float(error)) >= x >= (1 - float(error)):
                suspect_protein.append(protein)
        return suspect_protein


class Protein:
    # Class Protein is a class that finally processes each and every protein sequence found by the Sequence class. Upon
    # instantiation it parses the string, translates and processes the weight of the protein saving it upon itself as a
    # self variable.
    counter = 0

    def __init__(self, fasta, number, base_sequence):
        self.fasta_origin = fasta
        self.order_in_fasta = number
        self.base_sequence = base_sequence
        Protein.counter += 1
        self.base_list = self.pre_translate()
        self.amino_list = self.translate()
        self.Kda_weight = self.weight()

    def pre_translate(self):
        # Pre_translate is a parsing method that processes the complete string of the protein sequence into a list of
        # 3 character string needed to use the dictionaries, basically into codons, for amino acid translations, it
        # returns a list of codons.
        seq = self.base_sequence
        index0 = 0
        list1 = []
        while True:
            c = seq[index0:(index0+3)]
            list1.append(c)
            index0 += 3
            if index0 >= (len(seq)):
                break
        return list1

    def translate(self):
        # The translate function looks into the list of codons acquired from the pre_translate function and translates
        # them with the use of a dictionary that returns the 3 letter abbreviation of the amino acid the codon codifies
        # for, saving a list of amino acids.
        bases = self.base_list
        dict0 = amino_acid_dictionary.amino_acids
        list0 = []
        for base in bases:
            list0.append(dict0[base])
        return list0

    def weight(self):
        # Accesses a dictionary where the weight in KDa of each amino acid is saved, therefore adding and calculating
        # the total weight of the protein and saving it to the object.
        protein = self.amino_list
        dict0 = Weight_dictionary.Kda_weight
        weight = 0
        for base in protein:
            val = dict0[base]
            weight += val
        return weight
