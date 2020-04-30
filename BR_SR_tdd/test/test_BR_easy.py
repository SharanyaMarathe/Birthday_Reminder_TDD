import pytest
import sys
sys.path.append('../')
from src import dateSub

with open ("data/easy_test_cases.txt",mode='r') as case1file:
		res1= [tuple(line.strip().split(","))for line in case1file]


@pytest.mark.parametrize('date,exp',res1)
def test_easy_case(date,exp):
	act=dateSub.Subscription(date,'15-03-1956')[0]
	assert act==exp









