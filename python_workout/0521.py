import glob
import os
print('Chapter 05 - Exercise 21')
print('')
print('Longest word per file')

# Three ways to list files in a dir
# glob.glob
# os.listdir
# pathlib
# I'm just using glob to scan through a hardcoded directory


def find_longest_word(thefile):
    """
    Find the longest word in the file
    except urls
    """
    longest_word_count = 0
    with open(thefile) as f:
        for one_line in f:
            for w in one_line.split():
                if len(w) > longest_word_count and not '/' in w:
                    longest_word_count = len(w)
                    longest_word = w
    return longest_word


def find_all_longest_words(containing_path) -> dict:
    '''
        return {<filename>: <longest_word>}
    '''
    longest_words = {}
    for f in glob.glob(f'{containing_path}/*.txt'):
        longest_words[os.path.basename(f)] = find_longest_word(f)
    return longest_words


if __name__ == '__main__':
    DIR = os.path.join('.', 'python_workout',
                       'supporting_files', '0521_longest_words_files')
    res = find_all_longest_words(DIR)
    for filename, word in res.items():
        print(f"{filename}: {word}")
