# Sampath Thennakoon
# 16/04/2023

import xml.etree.ElementTree as ET
import glob
import os

annotations_dir = "validation/"

def train_full_analyse_xml_data():

    all_annotations_files = glob.glob(os.path.join(annotations_dir, '*.xml'))
    SA_LABEL = 'SA'
    BL_LABEL = 'BL'
    JB_LABEL = 'JB'
    RA_LABEL = 'RA'
    DM_LABEL = 'DM'
    CL_LABEL = 'CL'
    SRA_LABEL = 'SRA'
    SL_LABEL = 'SL'
    PC_LABEL = 'PC'
    SLA_LABEL = 'SLA'
    LA_LABEL = 'LA'

    SA_COUNT = 0
    BL_COUNT = 0
    JB_COUNT = 0
    RA_COUNT = 0
    DM_COUNT = 0
    CL_COUNT = 0
    SRA_COUNT = 0
    SL_COUNT = 0
    PC_COUNT = 0
    SLA_COUNT = 0
    LA_COUNT = 0

    print('Full Analyse Of Train XML Files')
    train_dict = {}
    for fil in all_annotations_files:
        tree = ET.parse(fil)
        root = tree.getroot()
        for obj in root.findall('object'):
            label = obj.find("name").text
            if label not in train_dict:
                train_dict[label] = 0
            train_dict[label] += 1

    for fil in all_annotations_files:
        tree = ET.parse(fil)
        root = tree.getroot()
        for obj in root.findall('object'):
            label = obj.find("name").text
            if label == SA_LABEL:
                SA_COUNT += 1
            elif label == BL_LABEL:
                BL_COUNT += 1
            elif label == JB_LABEL:
                JB_COUNT += 1
            elif label == RA_LABEL:
                RA_COUNT += 1
            elif label == DM_LABEL:
                DM_COUNT += 1
            elif label == CL_LABEL:
                CL_COUNT += 1
            elif label == SRA_LABEL:
                SRA_COUNT += 1
            elif label == SL_LABEL:
                SL_COUNT += 1
            elif label == PC_LABEL:
                PC_COUNT += 1
            elif label == SLA_LABEL:
                SLA_COUNT += 1
            elif label == LA_LABEL:
                LA_COUNT += 1

    print(train_dict)
    print("===================================")
    print('SA_COUNT: ',SA_COUNT)
    print('BL_COUNT: ',BL_COUNT)
    print('JB_COUNT: ',JB_COUNT)
    print('RA_COUNT: ',RA_COUNT)
    print('DM_COUNT: ',DM_COUNT)
    print('CL_COUNT: ',CL_COUNT)
    print('SRA_COUNT: ',SRA_COUNT)
    print('SL_COUNT: ',SL_COUNT)
    print('PC_COUNT: ',PC_COUNT)
    print('SLA_COUNT: ',SLA_COUNT)
    print('LA_COUNT: ',LA_COUNT)

if __name__ == '__main__':
    train_full_analyse_xml_data()
