import pytest
from dateSub import Date_info

with open ("easymonth_test_cases.txt",mode='r') as casefile:
		res= [tuple(line.strip().split(","))for line in casefile]


@pytest.mark.parametrize('date,exp',res)
def test_easy_cases(date,exp):
	act=Date_info(date)[1]
	assert act==exp
