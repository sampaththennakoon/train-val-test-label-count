# Sampath Thennakoon
# 16/04/2023

import xml.etree.ElementTree as ET
import glob
import os

annotations_dir = "annotations/"
train_dir = "train/"
validation_dir = "validation/"

def analyse_xml_data():

    all_train_files = glob.glob(os.path.join(train_dir, '*.xml'))
    all_validation_files = glob.glob(os.path.join(validation_dir, '*.xml'))

    print('Analyse Train XML Files')
    train_dict = {}
    for fil in all_train_files:
        basename = os.path.basename(fil)
        filename = os.path.splitext(basename)[0]
        tree = ET.parse(fil)
        root = tree.getroot()
        for obj in root.findall('object'):
            label = obj.find("name").text
            if label not in train_dict:
                train_dict[label] = 0
            train_dict[label] += 1

    print(train_dict)

    print('Analyse Validation XML Files')
    validation_dict = {}
    for fil in all_validation_files:
        basename = os.path.basename(fil)
        filename = os.path.splitext(basename)[0]
        tree = ET.parse(fil)
        root = tree.getroot()
        for obj in root.findall('object'):
            label = obj.find("name").text
            if label not in validation_dict:
                validation_dict[label] = 0
            validation_dict[label] += 1

    print(validation_dict)

if __name__ == '__main__':
    analyse_xml_data()
