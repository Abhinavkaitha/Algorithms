import datetime

d= datetime

print(d.date(2016,7,24))

print(d.date.today())

print(d.date.today().weekday()) # Monday= 0

print(d.date.today().isoweekday()) # Monday= 1

tdelta = datetime.timedelta(days=7)

print(d.date.today()+tdelta) # 7 days from now

print(d.date.today()-tdelta) # 7 days ago

till_bday=d.date(2019,5,1)-d.date.today()

print(till_bday) # Difference between two dates

print(till_bday.total_seconds()) # Difference between two dates in seconds

t=datetime.time(9,30,45,10000)

print(t)
print(t.hour)

dt = datetime.datetime(2016,7,26,12,30,45,10000)
print(dt)

print(dt.date())
print(dt.time())
print(dt.year)

tdelta1 = datetime.timedelta(days=7,hours=12)

print(dt+tdelta1)

dt_today = datetime.datetime.today() # If we excecute both today and now at the same time, they will be same.
# The difference is today gives the local time stamp without timezone. now gives us the option to enter time zone
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today.isoformat())

print(dt_today.strftime("%B %d, %Y")) # month, two digit date, 4 year

#########  Problem

dt_str = ["1-January-2010","1-March-2010","1-April-2010","02-November-2010","1-May-1995","1-July-2010","1-June-2010","1-August-2010","1-September-2010","1-November-2010","1-october-2010","1-December-2010"]

dt_1 = [datetime.datetime.strptime(i,"%d-%B-%Y") for i in dt_str]
dt_1.sort()
ans = [datetime.datetime.strftime(i,"%d-%B-%Y") for i in dt_1]

print(ans)

# strftime - Datetime to String
# strptime - String to Datetime


######### Problem

work_hours = 24

pattern = "08??840"

day_hours = 4


sum_hr=0
days_to_assign=0

for i in pattern:
    if i!="?":
        sum_hr+=int(i)
    else:
        days_to_assign+=1

left = work_hours - sum_hr

valid_permutations=[]
for i in range(day_hours+1):
    for j in range(day_hours+1):
        if i+j == left:
            valid_permutations.append((i,j))

#valid_permutations=[]

#for i in permutations:
#    if sum(i) == left:
#        valid_permutations.append(i)

original = pattern

ans = []

for i in valid_permutations:
    pattern=pattern.replace("?",str(i[0]),1)
    pattern=pattern.replace("?",str(i[1]))
    ans.append(pattern)
    pattern = original
ans.sort()
print(ans)

################  Partitions

def printArray(p,n):
    for i in range(0,n):
        print(p[i],end=" ")
    print()
def uniquePartitions(n):
    p = [0]*n
    k = 0
    p[k] = n
    while True:
        printArray(p,k+1)
        rem_val =0
        while k>=0 and p[k] ==1:
            rem_val+=p[k]
            k-=1
        if k<0:
            print()
            return
        p[k]-=1
        rem_val+=1

        while rem_val>p[k]:
            p[k+1] = p[k]
            rem_val = rem_val-p[k]
            k+=1
        p[k+1]=rem_val
        k+=1
uniquePartitions(4)

