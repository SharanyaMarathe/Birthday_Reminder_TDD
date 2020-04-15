import datetime


def Birth_Date_info(B_date):
	
	dates_detail=datetime.date(int(2020),int(B_date.month),int(B_date.day))
	day=dates_detail.strftime("%A")
	month=dates_detail.strftime("%B")
	return day,month

def Current_date_info(C_date):
	Current_date=C_date.split("-")
	C_dates_detail=datetime.date(int(2020),int(Current_date[1]),int(Current_date[0]))
	C_day=C_dates_detail.strftime("%A")
	return C_dates_detail,C_day
	


def Notification(B_day,C_day):
	if(B_day.month > C_day.month):
		return  (str(B_day.month - C_day.month)+" Months from Now")

	else:
		return (str(C_day.month - B_day.month)+" Months Ago")
			

def Date_info(date):
	#collecting birthday information and giving results
	Birth_date=datetime.date(1995,3,15)
	Birth_day=Birth_Date_info(Birth_date)
	Current_date = Current_date_info(date)
	Birthday_notify=Notification(Birth_date,Current_date[0])
	#to print reminder to Birthday
	print("Birthday",Current_date[0]," ",Current_date[1]," ",Birthday_notify,"  ||  ","On ",Birth_day[0],", ",Birth_date.day,"th of",Birth_day[1])
	#collecting subscription information and giving results
	Subscribe_date=datetime.date(2020,3,15)
	Subscribe_day=Birth_Date_info(Subscribe_date)
	Current_date = Current_date_info(date)
	Subscribe_notify=Notification(Current_date[0],Birth_date)
	sub_notify=str(12-int(Subscribe_notify[0]))+" Months from Now"
	print("Subscription",Current_date[0]," ",Current_date[1]," ",sub_notify,"  ||  ","On ",Birth_day[0],", ",Birth_date.day,"th of",Birth_day[1])
	return Birthday_notify,sub_notify
	#return Subscribe_notify


if __name__ == "__main__":
	dates=input("Enter the date: ")
	Date_info(dates)


