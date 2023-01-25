import pandas as pd
import numpy as np 
from datetime import datetime
import xlsxwriter
from datetime import date
import pytz
UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata')

df = pd.read_csv("demo.txt",delimiter=' ')
df.columns = ['Rtsp','Day','Time','Detectd']
# df['Detectd'] = int(df['Detectd'])
# print(type(df['Detectd'][0]))

# df.index.names = ["Time-stamp"]
df.to_csv("results.csv",index=None)
dff = pd.read_csv("results.csv")
dff = pd.DataFrame(dff)

def get_dif_time(df):
    ans = 0.0 
    for i in range(len(df.index)):
        print(int(df['Detection'][i]))
        if(i!=0 and int(df['Detection'][i]) == 14):
            start_time = df['Time_stamp'][i-1]
            end_time = df['Time_stamp'][i]
            t1 = datetime.strptime(start_time, "%M:%S:%f")
            t2 = datetime.strptime(end_time, "%M:%S:%f")
            delta = t2 - t1
            delta = delta.total_seconds()
            ans += delta
            
    return ans

workbook = xlsxwriter.Workbook("Bird_detection.xlsx")

dd = pd.read_csv("results.csv")
gb_df = df.groupby(['Rtsp'])
gb = df.groupby("Rtsp")
a = [gb.get_group(x) for x in gb.groups]
length_gb = len(a)
str_res = []

for k in range(length_gb):

    df = pd.DataFrame(a[k])
    df.to_csv("grp_by1.csv")
    df = pd.read_csv("grp_by1.csv")
    
    s1 = workbook.add_worksheet(str(df['Rtsp'][0][-4:]))
    s1.write(1, 0, 'Camera name')
    s1.write(1, 1, str(df['Rtsp'][0]))
    s1.set_column(0,0,14)
    s1.write(2, 0, 'Date')
    s1.write(2, 1, 'Time Slot')
    ind = 3
    for i in range(len(df.index)):
        if(df['Detectd'][i] == 14.0):
            s1.write(ind,0,str(df['Day'][i]))
            s1.write(ind,2,str(df['Time'][i]))
            s1.write(ind,3,"Detected")
            
            # Timeslot
            interval = str(df['Time'][i][:2])
            interval = int(interval)
            if(interval > 12):
                interval = interval%12
                s1.write(ind,1,str(interval)+" to "+str(interval+1)+" PM")
            else:
                s1.write(ind,1,str(interval)+" to "+str(interval+1)+" AM")
            
            ind += 1
    
    section = np.zeros(26, dtype=float)
    from datetime import datetime
    # now = datetime.now()
    now = datetime.now(IST)
    cur_minute = now.strftime("%M")
    ans = 0.0 
    for i in range(len(df.index)):
        if(i!=0 and df['Detectd'][i] == 14.0):
            start_time = df['Time'][i-1]
            end_time = df['Time'][i]
            
            t1 = datetime.strptime(start_time, "%M:%S:%f")
            t2 = datetime.strptime(end_time, "%M:%S:%f")
            
            curmin = t1.minute
            cursec = t1.second
            curm = int(curmin)
            curs = int(cursec)
            
            delta = t2 - t1
            delta = delta.total_seconds()
            ans += delta

            section[curm] = section[curm] + ans
            # section[curs] = section[curs] + ans #-section[curs-1]
            ans = 0 
            
    total_time = 0.0
    for i in range(25):
        total_time += section[i]
    section[25] = total_time
    section = list(section)
    str_res.append(section)
    # print(section)
    

# print(str_res)


# ss = list(a[0]['Rtsp'])
# print(ss[0])
rtsp_list = []
for i in range(len(str_res)):
    ss = list(a[i]['Rtsp'])
    rtsp_list.append(ss[0])
    

rtsp_list = []

for i in range(len(str_res)):
    ss = list(a[i]['Rtsp'])
    rtsp_list.append(ss[0])
    
ll = len(str_res)

s = workbook.add_worksheet("Detection_sheet") 

s.set_column(0,0, 23)
s.set_column(1,1, 40)
s.write(0, 0, 'IP Address')
s.write(0, 1, '(All)')
s.write(1, 0, 'Instance Type')
s.write(1, 1, '(All)')

s.write(3, 0, 'Count of Instance Type')
s.write(3, 2, 'Column Label')

for i in range(len(str_res)):
    s.write(7+i,1,rtsp_list[i])

s.write(5, 0, 'Date')
s.write(5, 1, 'Address')
s.write(4,27, "Total Time")
#Set date
for i in range(len(str_res)):
    today = date.today()
    today = str(today)
    # s.write(7+i,0,today)
    s.write(7+i,0,df['Day'][0])


for i in range(12):
    if(i==0):
        s.write(4,i+2,"{}AM".format(12))
    else:
        s.write(4,i+2,"{}AM".format(i))

for i in range(13):
    if(i==0):
        s.write(4,i+2+12,"{}PM".format(12))
    else:
        s.write(4,i+2+12,"{}PM".format(i))


# str_res
for i in range(26):
    for j in range(ll):
    # print(section[i])
    # s.write(7,i+2,'{}'.format(section[i]))
        s.write(7+j,i+2,'{}'.format(str_res[j][i]))


workbook.close()