import datetime
import date

def before_subdates(cdate,sdate):
	
		if(sdate.month == cdate.month):
			due_date=date.condition_for_same_month(sdate.day,cdate.day)
			return due_date
		else:
			month_remained=sdate.month-cdate.month
			return str(month_remained )+" Months from Now"
	
def for_year(cdate,sdate):
	if(cdate.year==2020):	
		return before_subdates(cdate,sdate)
	else:
		sdate.year=cdate.year
		return before_subdates(cdate,sdate)

def Subscription(C_date,S_date):
	B_day=date.Date_info(C_date,S_date)
	C_dateInfo=date.Current_date_info(C_date)
	S_dateInfo=date.Birth_Date_info(S_date)
	
	

	if(int(C_dateInfo[0].month)  > int(S_dateInfo[1].month)):
		S_notify=date.months_display(C_dateInfo[0],S_dateInfo[1])
		sub_notify=str(12-int(S_notify[0]))+" Months from Now"
	else:
		sub_notify=str(before_subdates(C_dateInfo[0],S_dateInfo[1]))
	
	
	Bday=(str(B_day[5]))
	print(sub_notify)
	return Bday,sub_notify

	
if __name__ == "__main__":
	dates=input("Enter the date: ")
	date_Sub=input("Enter the Subscription date: ")
	Subscription(dates,date_Sub)
#print("Subscription",C_dateInfo[0]," ",C_dateInfo[1]," ",sub_notify,"  ||  ","On ",S_dateInfo[0],", ",S_dateInfo[1].day,"th of",S_dateInfo[2])
