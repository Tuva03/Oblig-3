from leap.leapYear import IsLeapYear


def test1_is_leap_year():
    assert IsLeapYear.isLeapYear(2020) == True
    assert IsLeapYear.isLeapYear(2016) == True


def test2_year_is_dividable_with_4_but_not_100():
    assert IsLeapYear.isLeapYear(2024) == True
    assert IsLeapYear.isLeapYear(1980) == True


def test3_year_is_dividable_with_400():
    assert IsLeapYear.isLeapYear(2000) == True
    assert IsLeapYear.isLeapYear(1600) == True


def test4_is_not_leap_year():
    assert IsLeapYear.isLeapYear(2100) == False
    assert IsLeapYear.isLeapYear(1800) == False


def test5_year_is_not_dividable_with_4():
    assert IsLeapYear.isLeapYear(2023) == False


def test6_year_is_dividable_with_100_but_not_400():
    assert IsLeapYear.isLeapYear(1900) == False
    assert IsLeapYear.isLeapYear(1700) == False