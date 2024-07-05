from time import time

start_time = time() #start time

for x in range(1000):
    print(x)
end_time = time() #end time
print(f" the start time of the algorithm is: {start_time}")
print(f" the end time of the algorithm is: {end_time}")
print(f" the total time taken by the algorithm is: {end_time - start_time}")
