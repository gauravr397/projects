import psutil

print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))

cpufreq = psutil.cpu_freq()
print(f"Max freq: {cpufreq.max:.2f}Mhz")
print(f"Min freq: {cpufreq.min:.2f}Mhz")
print(f"current frq: {cpufreq.current:.2f}Mhz")

print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core{i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")
