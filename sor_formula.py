# SOR formula given an output image
import numpy as np


def compute_sor(out_im_arr):
    '''
    This formula can be used for the whole image or for a sub-image.
    Thus it can be used to increase the size of the dataset.
    ----
    Inputs:
    out_im_arr = Output image after water injection, numpy.array
    ----
    Outputs:
    computed_sor = SOR value for the block
    '''
    non_solid_image = out_im_arr[out_im_arr > 1]
    oil_ratio = np.mean(1. * (non_solid_image[non_solid_image > 1] >= 4))
    computed_sor = oil_ratio

    return computed_sor
