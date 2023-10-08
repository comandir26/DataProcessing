import os
import shutil
import csv


def get_full_paths(class_name: str) -> list:
    """
    Возвращает список измененных абсолютных путей для изображений

    Данная функция возвращает список абсолютных путей для всех изображений определенного
    класса, переданного в функцию, после перемещения изображений в другую директорию
    Parameters
    ----------
    class_name : str
      Имя класса
    Returns
    -------
    list
    Список абсолютных путей к изображениям
    """
    full_path = os.path.abspath('dataset2')
    image_names = os.listdir(full_path)
    image_class_names = [name for name in image_names if class_name in name]
    image_full_paths = list(
        map(lambda name: os.path.join(full_path, name), image_class_names))
    return image_full_paths


def get_rel_paths(class_name: str) -> list:
    """
    Возвращает список измененных относительных путей для изображений

    Данная функция возвращает список относительных путей для всех изображений определенного класса, 
    переданного в функцию, после перемещения изображений в другую директорию
    Parameters
    ----------
    class_name : str
      Имя класса
    Returns
    -------
    list
    Список относительных путей к изображениям
    """
    rel_path = os.path.relpath('dataset2')
    image_names = os.listdir(rel_path)
    image_class_names = [name for name in image_names if class_name in name]
    image_rel_paths = list(
        map(lambda name: os.path.join(rel_path, name), image_class_names))
    return image_rel_paths


def replace_images(class_name: str) -> list:
    """
    Изменяет имена изображений и переносит их в другую директорию

    Данная функция изменяет имена изображений, объединяя номер изображения и класс в формате class_number.jpg, 
    переносит изображения в директорию dataset и удаляет папку, где хранились изображения класса

    Parameters
    ----------
    class_name : str
      Имя класса
    Returns
    -------
    None
    """
    rel_path = os.path.relpath('dataset2')
    class_path = os.path.join(rel_path, class_name)
    image_names = os.listdir(class_path)
    image_rel_paths = list(
        map(lambda name: os.path.join(class_path, name), image_names))
    new_rel_paths = list(
        map(lambda name: os.path.join(rel_path, f'{class_name}_{name}'), image_names))
    for old_name, new_name in zip(image_rel_paths, new_rel_paths):
        os.replace(old_name, new_name)

    os.chdir('dataset2')

    if os.path.isdir(class_name):
        os.rmdir(class_name)

    os.chdir('..')


if __name__ == "__main__":

    class1 = 'polarbear'
    class2 = 'brownbear'

    old = os.path.relpath('dataset')
    new = os.path.relpath('dataset2')
    shutil.copytree(old, new)

    replace_images(class1)
    replace_images(class2)

    polarbear_full_paths = get_full_paths(class1)
    polarbear_rel_paths = get_rel_paths(class1)
    brownbear_full_paths = get_full_paths(class2)
    brownbear_rel_paths = get_rel_paths(class2)
    
    with open('paths2.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        for full_path, rel_path in zip(polarbear_full_paths, polarbear_rel_paths):
            writer.writerow([full_path, rel_path, class1])
        for full_path, rel_path in zip(brownbear_full_paths, brownbear_rel_paths):
            writer.writerow([full_path, rel_path, class2])