import re
import amino_acid_dictionary

class Sequence:
    def __init__(self, fasta):
        self.f = fasta
        self.lines, self.count = self.parsing()
        self.string = "".join(self.lines)
        self.proteins_start = self.protein_search()
        self.actual_proteins = self.protein_finish()
        self.protein_object_list = []

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
        for idx, val in enumerate(self.actual_proteins):
            nid = idx+1
            self.protein_object_list.append(Protein(self.f, nid, val))
        print(Protein.counter)


class Protein:
    counter = 0

    def __init__(self, fasta, number, base_sequence):
        self.fasta_origin = fasta
        self.order_in_fasta = number
        self.base_sequence = base_sequence
        Protein.counter += 1
        self.base_list = self.pre_translate()
        self.amino_list = self.translate()

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


s = Sequence("sequence.fasta.txt")
s.protein_factory()
b = s.protein_object_list[0]
print(b.base_list)
print(b.amino_list)
