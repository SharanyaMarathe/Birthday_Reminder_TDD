import pytest
import sys
sys.path.append('../')
from src import dateSub

with open ("data/easymonth_test_cases.txt",mode='r') as casefile:
		res= [tuple(line.strip().split(","))for line in casefile]


@pytest.mark.parametrize('date,exp',res)
def test_easy_cases(date,exp):
	act=dateSub.Subscription(date,'15-03-1995')[1]
	assert act==exp
