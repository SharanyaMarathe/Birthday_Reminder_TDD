import pytest
from date import Current_Date_info,Birth_Date_info


test_current_date=[("02-04-2020","Thursday"),("01-01-2020","Wednesday"),("11-08-2020","Tuesday"),("10-04-2020","Friday")]
test_Birth_date=[("15-03-1995","Sunday"),("02-11-1997","Monday")]

@pytest.mark.parametrize('date,exp',test_current_date)
def test_Current_day(date,exp):
    act=Current_Date_info(date)
    assert act==exp


@pytest.mark.parametrize('date,exp',test_Birth_date)
def test_Birthday(date,exp):
	act=Birth_Date_info(date)
	assert act==exp
