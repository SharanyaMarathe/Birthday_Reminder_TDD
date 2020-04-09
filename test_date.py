import pytest
from date import Date_info

easy_test_cases =[("12-01-2020","2 Months from Now"),("20-05-2020","2 Months Ago"),("15-06-2020","3 Months Ago"),("25-07-2020","4 Months Ago"),("29-08-2020","5 Months Ago"),("02-09-2020","6 Months Ago"),("05-10-2020","7 Months Ago"),("30-11-2020","8 Months Ago"),("30-12-2020","9 Months Ago")]


@pytest.mark.parametrize('date,exp',easy_test_cases)
def test_Birthday(date,exp):
	act=Date_info(date)
	assert act==exp
