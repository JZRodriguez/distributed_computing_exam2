from exam import get_time
import subprocess, re, sys
import matplotlib.pyplot as plt


filler, start, end, jump, ip = [0] + [int(a) for a in sys.argv[1:-1]] + [sys.argv[-1]]



megabytes = [1]
run = [get_time(ip, 1)]
print(f'{megabytes[0]} MBs in {run[0]} seconds')
for i in range (start, end+1, jump) :
    run.append(get_time(ip, i))
    megabytes.append(i)
    print(f'{i} MBs in {run[-1]} seconds')

plt.plot(megabytes, run)
plt.savefig("latency_graph.png")
