import datetime
import date

def before_subdates(cdate,sdate):
	if(cdate.year==2020):
		month_remained=sdate.month-cdate.month
	return month_remained


def Subscription(C_date,S_date):
	B_day=date.Date_info(C_date,S_date)
	C_dateInfo=date.Current_date_info(C_date)
	S_dateInfo=date.Birth_Date_info(S_date)
	
	
	try:
	#if(int(C_dateInfo[0].month)  > int(S_dateInfo[1].month)):
		S_notify=date.months_display(C_dateInfo[0],S_dateInfo[1])
		sub_notify=str(12-int(S_notify[0]))+" Months from Now"
	except ValueError as err:
		sub_notify=str(before_subdates(C_dateInfo[0],S_dateInfo[1]))+" Months from Now"
	
	Bday=(str(B_day[5]))
	#print(sub_notify)
	print(sub_notify)
	return Bday,sub_notify

	
if __name__ == "__main__":
	dates=input("Enter the date: ")
	date_Sub=input("Enter the Subscription date: ")
	Subscription(dates,date_Sub)
#print("Subscription",C_dateInfo[0]," ",C_dateInfo[1]," ",sub_notify,"  ||  ","On ",S_dateInfo[0],", ",S_dateInfo[1].day,"th of",S_dateInfo[2])



