import datetime

def Birth_Date_info(B_date):
	
	dates_detail=datetime.date(int(2020),int(B_date.month),int(B_date.day))
	day=dates_detail.strftime("%A")
	month=dates_detail.strftime("%B")
	return day,month


def Notification(B_day,C_day):
	if(B_day.month > C_day.month):
		return  (str(B_day.month - C_day.month)+" Months from Now")

	elif((B_day.month - C_day.month)< -1 ): 
		return (str(C_day.month - B_day.month) +" Months Ago")

	else:
		if(B_day.month == C_day.month):
			bday=B_day.day
			cday=C_day.day
			conditions1={   0 : "Today",
					7 : "Next Sunday",
			  		1 : "Tomorrow",
					2:"Day after Tomorrow",
					14:"2 weeks from now",
					-1:"Yesterday",
					-2:"Day before Yesterday",
					-7:"Last Sunday",
					}
			for key in range(3,7):
				conditions1[key] = "Coming Sunday"
			for key in range(-6,-2): 
				conditions1[key] = str(cday-bday) +" days before"
			for key in range(8,14):
				conditions1[key] = "Next Sunday"
			for key in range(-13,-7):
				conditions1[key] = "In the last week"
			for key in range(-16,-13):
				conditions1[key] = "2 weeks ago"

			return (conditions1[bday-cday])
		
		else:
			bday=B_day.day
			cday=C_day.day+31
			conditions2={}
			for key in range(17,21): 
				conditions2[key] = "2 weeks ago"
			for key in range(21,28):
				conditions2[key] = "3 weeks ago"
			for key in range(28,31):
				conditions2[key] = "Almost a month ago"
			for key in range(31,62):
				conditions2[key] = "Last month"
			
			return(conditions2[cday-bday])



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

