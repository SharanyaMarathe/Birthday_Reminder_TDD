import datetime

def Current_Date_info(date):
	dates=date.split("-")
	dates_detail=datetime.date(int(dates[2]),int(dates[1]),int(dates[0]))
	day=dates_detail.strftime("%A")
	return day

def Birth_Date_info(date):
	dates=date.split("-")
	dates_detail=datetime.date(int(2020),int(dates[1]),int(dates[0]))
	day=dates_detail.strftime("%A")
	return day
