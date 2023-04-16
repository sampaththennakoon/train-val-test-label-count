# Sampath Thennakoon
# 16/04/2023

import glob
import os

annotations_dir = "annotations/"
train_dir = "train/"
validation_dir = "validation/"

def file_diff():

    all_annotations_files = glob.glob(os.path.join(annotations_dir, '*.xml'))
    all_train_files = glob.glob(os.path.join(train_dir, '*.xml'))
    all_validation_files = glob.glob(os.path.join(validation_dir, '*.xml'))

    all_annotations_arr = []
    all_train_arr = []
    all_validation_arr = []
    all_item_arr = []

    for _file in all_annotations_files:
        all_annotations_arr.append(os.path.splitext(os.path.basename(_file))[0])

    for _file in all_train_files:
        all_train_arr.append(os.path.splitext(os.path.basename(_file))[0])
        all_item_arr.append(os.path.splitext(os.path.basename(_file))[0])

    for _file in all_validation_files:
        all_validation_arr.append(os.path.splitext(os.path.basename(_file))[0])
        all_item_arr.append(os.path.splitext(os.path.basename(_file))[0])

    all_annotations_size = len(all_annotations_arr)
    all_train_size = len(all_train_arr)
    all_item_size = len(all_item_arr)
    all_validation_size = len(all_validation_arr)

    print('======================================')
    print('all_annotations_size: ', all_annotations_size)
    print('all_train_size: ', all_train_size)
    print('all_item_size: ', all_item_size)
    print('all_validation_size: ', all_validation_size)
    print('======================================')
    print('all_annotations_arr: ', all_annotations_arr)
    print('all_train_arr: ', all_train_arr)
    print('all_validation_arr: ', all_validation_arr)
    print('======================================')
    difference = set(all_annotations_arr) - set(all_item_arr)
    print('difference: ', difference)
    print('======================================')
    intersection = set(all_train_arr).intersection(set(all_validation_arr))
    print('intersection: ', intersection)
    print('======================================')


if __name__ == '__main__':
    file_diff()
