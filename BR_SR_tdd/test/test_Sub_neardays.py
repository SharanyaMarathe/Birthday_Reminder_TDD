import pytest
import sys
sys.path.append('../')
from src import dateSub

with open ("data/neardays_test_cases.txt",mode='r') as case2file:
		res2= [tuple(line.strip().split(","))for line in case2file]

@pytest.mark.parametrize('date,exp',res2)
def test_nearby_dates(date,exp):
	act=dateSub.Subscription(date,'15-03-1956')[1]
	assert act==exp
