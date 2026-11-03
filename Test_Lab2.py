import Lab2

def test_find_min_max():
    input_arr = [1, 2, 3, 4, 5]
    result = Lab2.find_min_max(input_arr)
    assert result == [1, 5]

def test_calc_average():
    input_arr = [10, 20, 30]
    result = Lab2.calc_average(input_arr)
    assert result == 20.0

def test_calc_median_temperature():
    input_arr = [10, 20, 30, 40]
    result = Lab2.calc_median_temperature(input_arr)
    assert result == 25.0