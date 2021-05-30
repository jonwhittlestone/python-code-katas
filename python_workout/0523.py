import json
import os
import glob
import pathlib
print('Chapter 05 - Exercise 23')
print('')
print('JSON')

# Example data structure to hold values
# scores = {
#     '9a': {
#         'literature': {
#             'min': 0,
#             'max': 0,
#             'average': 0
#         },
#         'science': {
#             'min': 0,
#             'max': 0,
#             'average': 0
#         },
#         'maths': {
#             'min': 0,
#             'max': 0,
#             'average': 0
#         },
#     }
# }

scores = {}


def collect_class_scores(path) -> dict:
    p = pathlib.Path(path)
    class_scores = {}
    for row in json.loads(p.read_text()):
        for subj, score in row.items():
            try:
                class_scores[subj].append(score)
            except KeyError:
                class_scores[subj] = []
                class_scores[subj].append(score)
    return class_scores


def collect_stats(path) -> dict:
    ret = {}
    class_scores = collect_class_scores(path)
    for subj, scores in class_scores.items():
        ret[subj] = {}
        # try:
        ret[subj] = {
            'max': max(scores),
            'min': min(scores),
            'average': round(sum(scores) / len(scores), 2)
        }
    return ret


def print_scores():
    '''
        In scores directory, prints
        the following

        scores/9a.json
            science: min 75, max 97, average 86.4
            literature: min 78, max 98, average 83.6
            math: min 65, max 100, average 85.0
        scores/9b.json
            science: min 35, max 95, average 82.0
            literature: min 38, max 98, average 72.0
            math: min 38, max 100, average 77.0
    '''

    DIR = os.path.join('.', 'python_workout',
                       'supporting_files', '0523_scores_json')

    for f in glob.glob(f'{DIR}/*.json'):
        scores[os.path.basename(f)] = collect_stats(f)

    # print output
    for c, subjects in scores.items():
        print(c)
        for subj, stats in subjects.items():
            print(f"\t{subj}: ", end='')
            cleaned_stats = str(stats).replace(
                '{', '').replace('}', '').replace("'", "")
            print(cleaned_stats)


if __name__ == '__main__':

    print_scores()
