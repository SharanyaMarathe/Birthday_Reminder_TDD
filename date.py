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
		bday=B_day.day
		cday=C_day.day
		
		conditions = {
		'cond1':eval('bday-cday == 7'),
		'cond2':eval('(bday-cday) in [6,5,4,3]'),
		'cond3':eval('bday-cday == 2'),	
		'cond4':eval('bday-cday == 1'),
		'cond5':eval('(cday-bday) in [6,5,4,3]'),	
		'cond6':eval('cday-bday == 1'),	
		'cond7':eval('cday-bday == 2'),	
		'cond8':eval('cday-bday == 7'),
		'cond9':eval('bday-cday == 14'),
		'cond10':eval('(bday-cday) in [8,9,10,11,12,13]'),
		'cond11':eval('(cday-bday) in[8,9,10,11,12,13]'),
		'cond12':eval('(cday-bday) in [14,15,16,17,18,19,20]'),
		}	

		if conditions['cond1']:
			return("Next Sunday")
		elif(conditions['cond2']):
			return ("Coming Sunday")
		elif(conditions['cond3']):
			return("Day after Tomorrow")
		elif conditions['cond4']:
			return("Tomorrow")
		elif(conditions['cond5']):
			return(str(cday-bday) +" days before")
		elif(conditions['cond6']):
			return("Yesterday")	
		elif(conditions['cond7']):
			return("Day before Yesterday")
		elif(conditions['cond8']):
			return("Last Sunday")
		elif(conditions['cond9']):
			return("2 weeks from now")
		elif(conditions['cond10']):
			return("Next Sunday")
		elif(conditions['cond11']):
			return("In the last week")
		elif(conditions['cond12']):
			return("2 weeks ago")
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
