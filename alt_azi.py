from sdt import LST,convert_sec_to_day_hmmss
#date_data=input("Enter DATE DDMMYYYY= ")
#time_data=input("Enter Time in HH:MM")
import time
from math import sin,cos,pi,asin
import matplotlib.pyplot as plt
LON=+78.961
LAT=32.776
RA="18 00 00" 
DEC="-23 00 00"
date_data="21032023"
UTOFF=+5.3
#UT="2000"

def ra_to_deg(RA):
	ra=RA.split(" ")
	rah=int(ra[0])
	ram=int(ra[1])
	ras=float(ra[2])
	v=(rah*15)+(ram/4)+(ras*(15/3600))
	return v

def dec_to_deg(DEC):
	dec=DEC.split(" ")
	decd=int(dec[0])
	decm=int(dec[1])
	decs=float(dec[2])
	v=decd+(decm/60)+(decs/3600)
	return v

def sec_deg(sec):
	return sec*(15/3600)

def get_altitude_deg(RA,DEC,LAT,LON,date_data,UT):
	d,h,m,s,lst,gmst,gmst0=LST(date_data, UT, LON)
	ra=ra_to_deg(RA)
	#lst_deg=sec_deg(lst)
	hagle= ((h*15)+(m/4)+(s*(15/3600)))-ra

	dec=dec_to_deg(DEC)
	#print("###########===",hagle,)
	eqn=(cos(((pi/180)*hagle))*(cos((pi/180)*dec))*cos(((pi/180)*LAT)))+(sin((pi/180)*dec)*sin((pi/180)*LAT))

	return (180/pi)*asin(eqn),lst



y=[]
ut=[]
lt=[]
lth=[]
ls_=[]
for i in range(0,24*3600,15*60):
	d,h,m,s=convert_sec_to_day_hmmss(i)
	#print(d,h,m,s)
	UT="{:02}".format(h)+"{:02}".format(m)
	alt,lst=get_altitude_deg(RA, DEC, LAT, LON, date_data, UT)
	UT="{:02}".format(h)+":"+"{:02}".format(m)
	local_time=((h*3600+(m*60))+UTOFF*3600)
	ld,lh,lm,ls=convert_sec_to_day_hmmss(local_time)
	LT="{:02}".format(lh)+":"+"{:02}".format(lm)
	lsd,lsh,lsm,lss=convert_sec_to_day_hmmss(lst)
	LST_="{:02}".format(lsh)+":"+"{:02}".format(lsm)
	if alt>0:
		y.append(alt)
		lt.append(LT)
		lth.append(lh+lm/60)
		ut.append((UT))
		ls_.append(LST_)




ax=plt.gca()
ax.grid(True, which='minor')


#ax2.set_xlabel("Modified x-axis")
ax.set_xticks(range(len(ut)))
ax.set_xticklabels(ut,rotation=90)
ax.set_xlabel("UT")
ax.minorticks_on()
ax.plot(range(len(ut)),y ,'.')

ax2 = ax.twiny()
ax2.set_xlim(ax.get_xlim())
ax2.set_xticks(range(len(ls_)))
ax2.set_xticklabels(ls_,rotation=90)


plt.grid(which='major')
plt.ylabel("Altitude in degree")
plt.show()
