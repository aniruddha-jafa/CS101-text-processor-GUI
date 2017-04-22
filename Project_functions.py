
'''


'''

def file_to_list_strings(FileName):

    list_lines = []

    with open(FileName, 'r') as F:

        for line in F:
            s1 = line.rstrip('\n')
            s2 = s1.rstrip('\r')
            s2 = s2.lower()
            list_lines.append(s2)

        return list_lines


def list_strings_to_list_words(list_strings):

    string_words = ''

    alpha = 'abcdefghijklmnopqrstuvwxyz'



    for line in list_strings:

        line.lower()

        for character in line:

            if  character in alpha:

                string_words = string_words + character

            else:

                string_words = string_words + " "

        string_words = string_words + " "

    return string_words.split()


def list_words_to_dic_words(list_words):

    dic_words = {}

    for word in list_words:

        if word in dic_words:

            dic_words[word] += 1

        else:
            dic_words[word] = 1

    return dic_words



def list_words_to_dic_letters(list_words):

    dic_letters = {}

    for word in list_words:

        for letter in word:

            if letter in dic_letters:

                dic_letters[letter] += 1

            else:

                dic_letters[letter] = 1

    return dic_letters




def print_dic_words(dic_words):

    sys.stdout = open('myfile.txt', 'w') # what does this do?

    list_sorted_keys = dic_words.keys()

    list_sorted_keys.sort()

    print " "*13 + "Word" + " "*13 + "Count" + " "* 5

    for word in list_sorted_keys:

        print "%20s     |    %5s"  %(word, dic_words[word] )

    sys.stdout.close()


'''
    with open('myfile.txt') as f:
        for line in f:
            print line.strip()

    sys.stdout.close()
'''

def find_palindromes(dic_words):

    dic_palindromes = {}

    list_keys = dic_words.keys()
    list_keys.sort()

    for key in list_keys:
        string = ''


        for letter in key:

            string = letter + string

        print string

        if string == key and len(string) > 2:
            dic_palindromes[key] = 1

    return dic_palindromes



if __name__ == "__main__":

    list_lines = file_to_list_strings("PridePrej.txt")

    list_words = list_strings_to_list_words(list_lines)

    dic_words = list_words_to_dic_words(list_words)

    dic_letters = list_words_to_dic_letters(list_words)

    dic_palindromes = find_palindromes(dic_words)

    # print dic_palindromes

    print_dic_words(dic_words)
