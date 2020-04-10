import datetime

def Birth_Date_info(B_date):
	
	dates_detail=datetime.date(int(2020),int(B_date.month),int(B_date.day))
	day=dates_detail.strftime("%A")
	month=dates_detail.strftime("%B")
	return day,month


def Notification(B_day,C_day):
	if(B_day.month > C_day.month):
		return  (str(B_day.month - C_day.month)+" Months from Now")

	elif(B_day.month < C_day.month): 
		return (str(C_day.month - B_day.month) +" Months Ago")

	else:
		b=B_day.day
		c=C_day.day
		if(b-c == 7):
			return("Next Sunday")

		elif((b-c==6) or (b-c==5) or (b-c==4) or (b-c==3)):
			return ("Coming Sunday")

		elif(b-c == 2):
			return("Day after Tomorrow")

		elif(b-c == 1):
			return("Tomorrow")
		
		elif((c-b==6) or (c-b==5) or (c-b==4) or (c-b==3)):
			return(str(c-b) +" days before")

		elif(c-b == 7):
			return("Last Sunday")


		elif(c-b == 2):
			return("Day before Yesterday")

		elif(c-b == 1):
			return("Yesterday")
		else:
			return("Today")


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
