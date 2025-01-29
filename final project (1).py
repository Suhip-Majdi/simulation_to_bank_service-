import numpy as np
import matplotlib.pyplot as plt


customers = list(range(1000))
arrival_time = np.zeros(len(customers))
interarrival_time = np.random.exponential(1, len(customers))
# server1
service_time1 = np.zeros(len(customers))
i = 0
while i < len(customers):
    x = np.random.poisson()
    if x > 0:
        service_time1[i] = x
        i += 1
time_s_begin1 = np.zeros(len(customers))
time_s_end1 = np.zeros(len(customers))
# server2
service_time2 = np.zeros(len(customers))
i = 0
while i < len(customers):
    x = np.random.poisson()
    if x > 0:
        service_time2[i] = x
        i += 1
time_s_begin2 = np.zeros(len(customers))
time_s_end2 = np.zeros(len(customers))
waitingInQueue = np.zeros(len(customers))


arrival_time[0] = 0
interarrival_time[0] = 0
time_s_begin1[0] = 0
time_s_end1[0] = service_time1[0]
waitingInQueue[0] = 0
service_time2[0] = 0
for i in range(1, len(customers)):
    arrival_time[i] = interarrival_time[i] + arrival_time[i - 1]
    # condition
    if arrival_time[i] < max(time_s_end1) and arrival_time[i]>max(time_s_end2):
        service_time1[i] = 0
        time_s_begin2[i] = max(arrival_time[i], max(time_s_end2))
        time_s_end2[i] = time_s_begin2[i] + service_time2[i]
        waitingInQueue[i] = time_s_begin2[i] - arrival_time[i]
    else:
        service_time2[i] = 0
        time_s_begin1[i] = max(arrival_time[i], max(time_s_end1))
        time_s_end1[i] = time_s_begin1[i] + service_time1[i]
        waitingInQueue[i] = time_s_begin1[i] - arrival_time[i]
# visulization
var = max(max(time_s_end1), max(time_s_end2))
percentage_busy1 = sum(service_time1)/var
percentage_busy2 = sum(service_time2)/var
print(percentage_busy1)
print(percentage_busy2)
labels = ['server 1', 'server2 2']
sizes = [percentage_busy1, percentage_busy2]
colors = ['lightblue', 'lightgreen']


plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  
plt.title('Percentage Busy for Systems')
plt.show()
plt.figure(figsize=(100, 50))
plt.plot(customers, waitingInQueue, marker='o', linestyle='-', color='b')
plt.title('Waiting Time in Queue for Each Customer')
plt.xlabel('Customer')
plt.ylabel('Waiting Time')
plt.grid(True)
plt.show()

