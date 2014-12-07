from temperament import *
from nose.tools import *

def test():
    assert True

def test_triad_mean_tempering():
   input = np.array([400.0, 700.0, 300.0])
   assert_equal(31.283, round(mean_tempering(input), 3))

def test_hz_to_cents():
   assert_equal(386.3137, round(hz_to_cents(5./4.), 4))

def test_key_tempering_error():
    intervals = np.array([[0, 4, 7], [2, 5, 9]])
    ideals = np.array([hz_to_cents(JUST_MAJOR_TRIAD), hz_to_cents(JUST_MINOR_TRIAD)])
    tempering = key_tempering(EQUAL_TEMPERAMENT, intervals, ideals)
    assert_equal(31.283, round(tempering, 3))

def test_combinatorial_difference():
    input = np.array([90., 200., 300.])
    expected = [110., 210., 100.]
    assert_list_equal(expected, list(combinatorial_difference(input)))
