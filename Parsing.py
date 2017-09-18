def parsing(fasta):

    file = open(fasta, 'r')
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


parsing('sequence.fasta.txt')