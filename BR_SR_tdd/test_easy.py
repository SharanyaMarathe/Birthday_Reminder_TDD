import pytest
from dateSub import Date_info

with open ("easy_test_cases.txt",mode='r') as case1file:
		res1= [tuple(line.strip().split(","))for line in case1file]


@pytest.mark.parametrize('date,exp',res1)
def test_easy_case(date,exp):
	act=Date_info(date,'15-03-2020')[0]
	assert act==exp








