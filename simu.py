import numpy as np

customers = list(range(20))
arrival_time = np.zeros(len(customers))
interarrival_time = np.random.exponential(1,len(customers))
service_time=np.zeros(len(customers))
i=0
while i<len(customers):
    x=np.random.poisson()
    if x>0:
        service_time[i]=x
        i+=1
time_s_begin = np.zeros(len(customers))
time_s_end = np.zeros(len(customers))
waitingInQueue = np.zeros(len(customers))
timeInSystem = np.zeros(len(customers))
idleTime = np.zeros(len(customers))

arrival_time[0] = 0
interarrival_time[0]=0
time_s_begin[0] = 0
idleTime[0] = 0

for i in range(0, len(customers)):
    if i!=0:
        arrival_time[i] = interarrival_time[i] + arrival_time[i - 1]
        time_s_begin[i] = max(arrival_time[i], time_s_end[i - 1])
    time_s_end[i] = time_s_begin[i] + service_time[i]
    waitingInQueue[i] = time_s_begin[i] - arrival_time[i]
    timeInSystem[i] = time_s_end[i] - arrival_time[i]
    if i!=0:
        idleTime[i] = time_s_begin[i] - time_s_end[i - 1]
