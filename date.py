import datetime
conditions1={   0 : "Today",
		7 : "Next Sunday",
		1 : "Tomorrow",
		2:"Day after Tomorrow",
		14:"2 weeks from now",
		-1:"Yesterday",
		-2:"Day before Yesterday",
		-7:"Last Sunday",
		}

conditions2={}

def newkeys_conditions1(conditions1):
	for key in range(3,7):
		conditions1[key] = "Coming Sunday"
	for key in range(-6,-2): 
		conditions1[key] = str((-1*key)) +" days before"
	for key in range(8,14):
		conditions1[key] = "Next Sunday"
	for key in range(-13,-7):
		conditions1[key] = "In the last week"
	for key in range(-16,-13):
		conditions1[key] = "2 weeks ago"
	return conditions1



def newkeys_conditions2(conditions2):
	for key in range(17,21): 
		conditions2[key] = "2 weeks ago"
	for key in range(21,28):
		conditions2[key] = "3 weeks ago"
	for key in range(28,31):
		conditions2[key] = "Almost a month ago"
	for key in range(31,62):
		conditions2[key] = "Last month"
	return conditions2


def Birth_Date_info(B_date):
	B_date=B_date.split("-")
	dates_detail=datetime.date(int(2020),int(B_date.month),int(B_date.day))
	day=dates_detail.strftime("%A")
	month=dates_detail.strftime("%B")
	return day,dates_detail,month

def Current_date_info(C_date):
	Current_date=C_date.split("-")
	C_dates_detail=datetime.date(int(2020),int(Current_date[1]),int(Current_date[0]))
	C_day=C_dates_detail.strftime("%A")
	return C_dates_detail,C_day
	

def condition_for_same_month(b_day,c_day):
		newkeys_conditions1(conditions1)
		return (conditions1[b_day-c_day])



def condition_for_previous_month(b_day,c_day):	
		newkeys_conditions2(conditions2)	
		return (conditions2[c_day-b_day])



def Notification(B_day,C_day):
	if(B_day.month > C_day.month):
		return  (str(B_day.month - C_day.month)+" Months from Now")

	elif((B_day.month - C_day.month)< -1 ): 
		return (str(C_day.month - B_day.month) +" Months Ago")

	else:
		birth_day=B_day.day
		current_day=C_day.day
		if(B_day.month == C_day.month):
			return condition_for_same_month(birth_day,current_day)
		else:
			return condition_for_previous_month(birth_day,current_day+31)

			

def Date_info(date,date_birth):
	
	Birth_day=Birth_Date_info(date_birth)
	Current_date = Current_date_info(date)
	Birthday_notify=Notification(Birth_date,Current_date[0])
	#return ("On "+day+","+ dates[0],dates_detail.strftime("%B"))
	print("Birthday : ",Current_date[0]," ",Current_date[1]," ",Birthday_notify,"  ||  ","On ",Birth_day[0],", ",Birth_day[1].day,"th of",Birth_day[2])
	return Birthday_notify

if __name__ == "__main__":
	dates=input("Enter the date: ")
	Birth_date=input("Enter your birthday: ")
	Date_info(dates,Birth_date)


