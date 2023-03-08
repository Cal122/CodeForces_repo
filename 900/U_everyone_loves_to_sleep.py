#PROBLEM - Check how long there is between the time of going to sleep to waking up, if the alarm is before the sleep time, go to the next alarm, if there is no other alarm then return 0 0

t = int(input())


for i in range(0, t):

    n,h,m = map(int, str(input()).split())
    
    for i in range(0, n):
        alarm_h, alarm_m = map(int, str(input()).split())
        h_diff = alarm_h - h
        m_diff = alarm_m - m
        if m_diff < 0:
            h_diff -= 1
            m_diff += 60
        print(h_diff)
        print(m_diff)


if h == alarm_h and m == alarm_m:
    continue