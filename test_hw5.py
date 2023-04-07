import pytest

from edits import edit_distance_bwd, edit_distance_fwd
from seamcarve import SeamCarve

def test_edits():
    # TODO: add more test functions with assertions on edit_distance_fwd 
    # and edit_distance_bwd based on examples you've seen or make yourself
    assert edit_distance_fwd("", "") == 0

def test_seamcarve():
    # TODO: add more assertions and/or test functions to test seamcarve
    # cell E1 from 5x5 spreadsheet
    test_image = [[[255, 255, 255], [0, 0, 0], [125, 125, 125], [0, 0, 0],\
        [255, 255, 255]], [[0, 0, 0], [125, 125, 125], [0, 0, 0],
        [255, 255, 255], [0, 0, 0]], [[255, 255, 255], [125, 125, 125],
        [255, 255, 255], [0, 0, 0], [255, 255, 255]], [[0, 0, 0],
        [255, 255, 255], [125, 125, 125], [255, 255, 255], [0, 0, 0]], 
        [[255, 255, 255], [0, 0, 0], [255, 255, 255], [125, 125, 125],
        [255, 255, 255]]]
    expected_seam = [2, 1, 1, 2, 3]

    my_sc = SeamCarve(image_matrix = test_image)

    importance_vals = my_sc.calculate_importance_values()
    calculated_seam = my_sc.find_least_important_seam(importance_vals)

    assert expected_seam == calculated_seam