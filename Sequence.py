import re
import amino_acid_dictionary
import Weight_dictionary
import math

class Sequence:
    def __init__(self, fasta):
        self.f = fasta
        self.lines, self.count = self.parsing()
        self.string = "".join(self.lines)
        self.proteins_start = self.protein_search()
        self.actual_proteins = self.protein_finish()
        self.protein_object_list = self.protein_factory()

    def parsing(self):
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
        real_proteins = []
        for element in self.proteins_start:
            pattern = r"(A[UT]G)([A-Z]{3})*?(([UT]AA)|([UT]AG)|([UT]GA))"
            search = re.search(pattern, element)
            if search:
                real_proteins.append(search.group())
        print('found', len(real_proteins), 'proteins')
        return real_proteins

    def print_protein_list(self, p_list):
        for element in p_list:
            print(element[0:5],'...',element[-5:],'size', len(element), 'bp')

    def protein_factory(self):
        list0 = []
        for idx, val in enumerate(self.actual_proteins):
            nid = idx+1
            list0.append(Protein(self.f, nid, val))
        return list0


class Protein:
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
        bases = self.base_list
        dict0 = amino_acid_dictionary.amino_acids
        list0 =[]
        for base in bases:
            list0.append(dict0[base])
        return list0

    def weight(self):
        protein = self.amino_list
        dict0 = Weight_dictionary.Kda_weight
        weight = 0
        for base in protein:
            val = dict0[base]
            weight += val
        return weight

    def protein_display(self):
        print('Your protein has', len(self.base_sequence), 'Base Sequences')
        print('It has', (len(self.amino_list)-1), 'amino acids and a weight of', self.Kda_weight, 'KDa')
        while True:
            print('Type "a" to see the amino acid sequence, "b" to see the base sequence and "q" to quit')
            answer = input('>')
            if answer == 'a':
                x = len(self.amino_list)
                y = x/10
                print_size = 10
                y_ground = math.floor(y)
                if y <= print_size:
                    print(self.amino_list)
                if y > print_size:
                    index = 0
                    n_index = print_size
                    for c in range(int(y_ground)):
                        print(self.amino_list[index:n_index])
                        index += print_size
                        n_index += print_size
                        if n_index >= x:
                            print(self.amino_list[index:])


            if answer == 'b':
                print(self.base_sequence)
            if answer == 'q':
                break
