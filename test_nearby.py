import pytest
from date import Date_info

with open ("nearby_test_cases.txt",mode='r') as case2file:
		res2= [tuple(line.strip().split(","))for line in case2file]

@pytest.mark.parametrize('date,exp',res2)
def test_nearby_dates(date,exp):
	act=Date_info(date,'15-03-1955')
	assert act==exp
