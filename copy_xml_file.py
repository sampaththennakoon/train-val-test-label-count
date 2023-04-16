# Sampath Thennakoon
# 16/04/2023

import glob
import os
import shutil

annotations_dir = "annotations/"
train_dir = "train/"
validation_dir = "validation/"

def extract_data():

    all_train_files = glob.glob(os.path.join(train_dir, '*.txt'))
    all_validation_files = glob.glob(os.path.join(validation_dir, '*.txt'))

    for train_file in all_train_files:
        #print(train_file)
        #print(os.path.basename(train_file))
        #print(os.path.splitext(os.path.basename(train_file))[0])
        xml_file_path = 'annotations/' + os.path.splitext(os.path.basename(train_file))[0] + '.xml'
        dst_train = 'train/' + os.path.splitext(os.path.basename(train_file))[0] + '.xml'
        shutil.copyfile(xml_file_path, dst_train)

    for validation_file in all_validation_files:
        xml_file_path = 'annotations/' + os.path.splitext(os.path.basename(validation_file))[0] + '.xml'
        dst_validation = 'validation/' + os.path.splitext(os.path.basename(validation_file))[0] + '.xml'
        shutil.copyfile(xml_file_path, dst_validation)

if __name__ == '__main__':
    extract_data()
