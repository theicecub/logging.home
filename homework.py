#2
import logging
import time

def hello():
    print("Hello!")

def multiplying():
    print(5 * 19)

def time_calculator(func):
    start_time = time.time()
    func()
    end_time=time.time()
    execution = end_time - start_time
    print(f"It taked {execution} seconds to output this function")

time_calculator(hello)
time_calculator(multiplying)