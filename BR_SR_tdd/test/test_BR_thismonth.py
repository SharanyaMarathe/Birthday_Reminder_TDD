import pytest
import sys
sys.path.append('../')
from src import dateSub

with open ("data/thismonth_test_cases.txt",mode='r') as casefile:
		res= [tuple(line.strip().split(","))for line in casefile]

@pytest.mark.parametrize('date,exp',res)
def test_nearby_dates(date,exp):
	act=dateSub.Subscription(date,'15-03-1956')[0]
	assert act==exp
