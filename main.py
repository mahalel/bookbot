import sys, getopt

def count_words(text):
    word_count = len(text.split())
    return word_count

def count_letters(text):
    letter_count = {}
    for letter in text:
        if letter.lower() not in letter_count:
            letter_count[letter.lower()] = 1
        else:
            letter_count[letter.lower()] += 1
    return letter_count
    
def main(argv):
    inputfile = ''
    # outputfile = ''
    opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg

    with open(inputfile) as f:
        text = f.read()
    print(f"--- Begin report of {inputfile} ---")
    print(f"{count_words(text)} words found in the document")
    print()
    # The 'e' character was found 46043 times
    all_letters = count_letters(text)
    letter_list = list(all_letters.keys())
    letter_list.sort()
    for letter in letter_list:
        if letter.isalpha():
            print(f"The letter {letter} is found {all_letters[letter]} times")        

if __name__ == "__main__":
   main(sys.argv[1:]) 