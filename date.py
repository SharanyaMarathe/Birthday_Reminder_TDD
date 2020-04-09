iimport datetime

def Birth_Date_info(B_date):
	
	dates_detail=datetime.date(int(2020),int(B_date.month),int(B_date.day))
	day=dates_detail.strftime("%A")
	month=dates_detail.strftime("%B")
	return day,month


def Notification(B_day,C_day):
	if(B_day.month > C_day.month):
		return  (str(B_day.month - C_day.month)+" Months from Now")

	else: 
		return (str(C_day.month - B_day.month) +" Months Ago")

	
	#return("SomeDay")


def Date_info(date):
	Birth_date=datetime.date(1995,3,15)
	Birth_day=Birth_Date_info(Birth_date)
	dates=date.split("-")
	dates_detail=datetime.date(int(2020),int(dates[1]),int(dates[0]))
	day=dates_detail.strftime("%A")
	notify=Notification(Birth_date,dates_detail)
	#return ("On "+day+","+ dates[0],dates_detail.strftime("%B"))
	print(dates_detail," ",day," ",notify,"  ||  ","On ",Birth_day[0],", ",Birth_date.day,"th of",Birth_day[1])
	return notify


if __name__ == "__main__":
	dates=input("Enter the date: ")
	Date_info(dates)


