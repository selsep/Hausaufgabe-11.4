# Forensics Programm

DNA = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

print (DNA)

#1 GENDER

gender_female = "TGAAGGACCTTC"

gender_male = "TGCAGGAACTTC"

if gender_female in DNA:
    print("The offender is female")

if gender_male in DNA:
    print("The offender is male")

#2 RACE

race_white = "AAAACCTCA"

race_black = "CGACTACAG"

race_asian = "CGCGGGCCG"

if race_white in DNA:
    print("The offender is white")

if race_black in DNA:
    print("The offender is black")

if race_asian in DNA:
    print("The offender is asian")

#3 HAIR COLOR

haircolor_black = "CCAGCAATCGC"

haircolor_brown = "GCCAGTGCCG"

haircolor_blonde = "TTAGCTATCGC"

if haircolor_black in DNA:
    print("The offender has black hair")

if haircolor_brown in DNA:
    print("The offender has brown hair")

if haircolor_blonde in DNA:
    print("The offender has blonde hair")

#4 EYE COLOR

eyecolor_blue = "TTGTGGTGGC"

eyecolor_green = "GGGAGGTGGC"

eyecolor_brown = "AAGTAGTGAC"

if eyecolor_blue in DNA:
    print("The offender has blue eyes")

if eyecolor_green in DNA:
    print("The offender has green eyes")

if eyecolor_brown in DNA:
    print("The offender has brown eyes")

#5 FACIAL SHAPE

square_face = "GCCACGG"

round_face = "ACCACAA"

oval_face = "AGGCCTCA"

if square_face in DNA:
    print("The offender has a square face")

if round_face in DNA:
    print("The offender has a round face")

if oval_face in DNA:
    print("The offender has an oval face")

# WHO ATE THE ICE CREAM?

if gender_female in DNA and race_white in DNA and haircolor_blonde in DNA and eyecolor_blue in DNA and square_oval in DNA:
    print("The offender is Eva")

if gender_female in DNA and race_white in DNA and haircolor_brown in DNA and eyecolor_brown in DNA and square_oval in DNA:
    print("The offender is Larisa")

if gender_male in DNA and race_white in DNA and haircolor_black in DNA and eyecolor_blue and DNA and square_oval in DNA:
    print("The offender is Matej")

if gender_male in DNA and race_white in DNA and haircolor_brown in DNA and eyecolor_green in DNA and square_face in DNA:
    print("The offender is Miha")