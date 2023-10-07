import os
import csv


def get_full_paths(class_name):
    full_path = os.path.abspath('dataset')
    class_path = os.path.join(full_path, class_name)
    image_names = os.listdir(class_path)
    image_full_paths = list(
        map(lambda name: os.path.join(class_path, name), image_names))
    return image_full_paths


def get_rel_paths(class_name):
    rel_path = os.path.relpath('dataset')
    class_path = os.path.join(rel_path, class_name)
    image_names = os.listdir(class_path)
    image_rel_paths = list(
        map(lambda name: os.path.join(class_path, name), image_names))
    return image_rel_paths


class1 = 'polarbear'
class2 = 'brownbear'

polarbear_full_paths = get_full_paths(class1)

polarbear_rel_paths = get_rel_paths(class1)

brownbear_full_paths = get_full_paths(class2)

brownbear_rel_paths = get_rel_paths(class2)

with open('paths.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
    writer.writerow(['Full path', 'Relative path', 'Class'])
    for full_path, rel_path in zip(polarbear_full_paths, polarbear_rel_paths):
        writer.writerow([full_path, rel_path, class1])
    for full_path, rel_path in zip(brownbear_full_paths, brownbear_rel_paths):
        writer.writerow([full_path, rel_path, class2])
