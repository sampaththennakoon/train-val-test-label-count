# Sampath Thennakoon
# 16/04/2023

import numpy as np
import matplotlib.pyplot as plt

def draw_chart():
    X = ['SA', 'LA', 'RA', 'SLA', 'SRA', 'DM', 'PC', 'JB', 'SL', 'BL', 'CL']
    Ytrain = [971, 108, 235, 165, 56, 688, 548, 120, 66, 127, 55]
    Yvalidation = [117, 10, 25, 15, 2, 82, 63, 8, 6, 15, 6]
    Ztest = [353, 44, 92, 61, 22, 277, 228, 44, 28, 21, 49]


    X_axis = np.arange(len(X))

    plt.figure(1, figsize=(15, 7.5))
    plt.bar(X_axis - 0.2 , Ytrain, 0.2, label='Train')
    plt.bar(X_axis, Yvalidation, 0.2, label='Validation')
    plt.bar(X_axis + 0.2, Ztest, 0.2, label='Test')

    plt.xticks(X_axis, X)
    plt.xlabel("Road Marking Classes")
    plt.ylabel("Number of Occurrences")
    plt.title("Road Marking Class Distribution Over The Train, Validation And Test Data Set")
    plt.legend()

    plt.savefig('1.png', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    draw_chart()
