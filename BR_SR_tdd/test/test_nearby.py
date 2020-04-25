import pytest
import dateSub

with open ("nearby_test_cases.txt",mode='r') as case2file:
		res2= [tuple(line.strip().split(","))for line in case2file]

@pytest.mark.parametrize('date,exp',res2)
def test_nearby_dates(date,exp):
	act=dateSub.Subscription(date,'15-03-1956')[0]
	assert act==exp
