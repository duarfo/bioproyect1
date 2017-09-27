# bioproyect1
protein finder and translator
Well, this is suppose to be a a biotechnology research tool. The idea is to help solve a more or less common problem of 
finding an interesting protein in an extract and knowing the relative size, the idea of the program is to feed it a 
FASTA sequence of the organism you are investigating and the size of your protein of interest. This program would 
then find all codon starting points witht their respecting finishing points and transalte them to aminoacid. After doing 
that it would calculate the weight and size of the protein and give you back the closest matches with the deviation from
your initial data.

At the moment we can parse and process a DNA fasta sequence, getting the number and sequence of each and every start codon
and their closest end sequence, getting then a list of theoretical proteins in the DNA genome. All of this is done by 
instantiating a Sequence class with the FASTA.txt file as the only parameter, the only function that you should call at the
moment is the print_protein_list function on a list you want to print.

At the moment I am working on translating to aminoacids, the first step to actually get the weight of the protein.
