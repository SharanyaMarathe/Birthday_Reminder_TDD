import pytest
from date import Date_info

with open ("thismonth_test_cases.txt",mode='r') as casefile:
		res= [tuple(line.strip().split(","))for line in casefile]

@pytest.mark.parametrize('date,exp',res)
def test_nearby_dates(date,exp):
	act=Date_info(date)
	assert act==exp
