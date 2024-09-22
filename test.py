from main import main
print("Location of main function:", main.__code__.co_filename)
from mid import main as mid_main

sample_data = [
    {
        "name": "John",
        "age": 30,
        "city": "New York",
        "country": "USA",
        "email": "john@mail.com",
    },
    {
        "name": "Jane",
        "age": 25,
        "city": "San Francisco",
        "country": "USA",
        "email": "jane@mail.com",
    },
]

# increase the number of sample_data by x
x = 1_000_000

sample_data = sample_data * x

print("sample_data length:", len(sample_data))

# compare the performance of the two functions
import time

start = time.perf_counter_ns()
res = mid_main(sample_data)
end = time.perf_counter_ns()

print(f"mid.py: {end - start} ns", "res:", res)

start = time.perf_counter_ns()
res = main(sample_data)
end = time.perf_counter_ns()

print(f"main.py: {end - start} ns", "res:", res)
