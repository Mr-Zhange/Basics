import time

# time.process_time()

sum = 0

for i in range(100000000):
    sum += i

print(sum)
print(time.process_time())
