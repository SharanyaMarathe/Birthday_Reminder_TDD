import pytest
from date import Date_info

with open ("easy_test_cases.txt",mode='r') as case1file:
		res1= [tuple(line.strip().split(","))for line in case1file]

with open ("nearby_test_cases.txt",mode='r') as case2file:
		res2= [tuple(line.strip().split(","))for line in case2file]


@pytest.mark.parametrize('date,exp',res1)
def test_easy_case(date,exp):
	act=Date_info(date)
	assert act==exp


@pytest.mark.parametrize('date,exp',res2)
def test_nearby_dates(date,exp):
	act=Date_info(date)
	assert act==exp




