import datetime as dt
laiks = dt.datetime.now().hour

if 0 <= laiks < 12:         
    print('labrit')
elif 12 <= laiks < 18:
    print('labdien')  
else:
    print('labvakar')