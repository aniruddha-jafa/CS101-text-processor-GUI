
'''
add more options (print by vlue or alphabetical order)

give options as to whether the user wants to print the dictionary of words or the dictionary of letters

pretty print the results

remove junk from the tect file.

'''
import sys



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

    sys.stdout = open('file.txt', 'w')

    list_sorted_keys = dic_words.keys()

    list_sorted_keys.sort()

    print " "*13 + "Word" + " "*13 + "Count" + " "* 5

    for word in list_sorted_keys:

        print "%20s     |    %5s"  %(word, dic_words[word] )

    sys.stdout.close()



if __name__ == "__main__":

    list_lines = file_to_list_strings("slide-PridePrej.txt")

    #print List_lines

    list_words = list_strings_to_list_words(list_lines)

    dic_words = list_words_to_dic_words(list_words)

    dic_letters = list_words_to_dic_letters(list_words)

    print_dic_words(dic_words)
