import math 
import datetime
##### Siderial Time Calculator ##########
###### INPUTS #######



####Covert Normal date to Julian date
def date_julian_date(date_data):
	d=int(date_data[0:2])
	m=int(date_data[2:4])
	y=int(date_data[4:8])
	#print(d,m,y)
	##### Formula collected from Karttunen page 44
	return 367*y-((7*(y+(m+9)//12))//4)-((3*(((y+(m-9)//7)//100))+1)//4)+((275*m)//9)+d+1721029


def convert_sec_to_day_hmmss(x):
	seconds = int((x % 60))
	minutes = int((x % 3600) / 60)
	hours = int((x % 86400) / 3600)
	days = int((x / (24*3600))) 
	return days,hours,minutes,seconds
######### Calculation GMST at 0 UT
def GMST0(J):
	T=(J-2451545.0)/(36525)
	#print("#"*10,T)
	#Collected from  Meeus Book page 87
	#Sidereal time in degree
	GMST0=24110.54841+(8640184.812866*T)+(0.093104*(T**2))-(T**3)*(0.0000062)
	


	GMST0=((GMST0))
	#print("#######GMST in Hour %s ",GMST0/3600,datetime.timedelta(0,GMST0))

	d,h,m,s=convert_sec_to_day_hmmss(GMST0)
	return  d,h,m,s,GMST0 



def angle_to_time_in_sec(angle):
#   Angle in degree
	tme=(angle*((24*3600)/360))
	return tme



def GMST_AT_UT(J,UT):
	days,hours,minutes,seconds,gmst0=GMST0(J)
	UT_hrs=int(UT[0:2])
	UT_min=int(UT[2:4])
	UT_sec=(UT_hrs*3600)+(UT_min)*60
	#Sidereal time runs 3min 57s faster
	delta=(1.00273790935)*((3*60)+57)
	UT_sec=UT_sec+delta
	GMST=gmst0+UT_sec
	#print("#######%S=",datetime.timedelta(0,GMST))
	d,h,m,s=convert_sec_to_day_hmmss(GMST)
	return d,h,m,s,GMST,gmst0

def LST(date_data,UT,LON):
	d,h,m,s,gmst,gmst0=GMST_AT_UT(date_julian_date(date_data),UT)
	lst=gmst+angle_to_time_in_sec(LON)
	#print("#######%s########",datetime.timedelta(0,lst))
	d,h,m,s=convert_sec_to_day_hmmss(lst)
	return d,h,m,s,lst,gmst,gmst0
	




