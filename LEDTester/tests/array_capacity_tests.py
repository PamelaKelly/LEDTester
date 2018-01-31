import time

def array_size_limit_test(size):
    try:
        start_time = time.time()
        arr = []
        for i in range(size):
            arr.append((i, i))
        print("Length of array: ", len(arr))
        print(arr[0])
        runtime = start_time - time.time()
        print(runtime)
    except Exception as e: 
        print("Error: Could not complete action due to a ", type(e), " error")
    
array_size_limit_test(1000)
array_size_limit_test(10000)
array_size_limit_test(15000)
array_size_limit_test(50000)
array_size_limit_test(100000)
array_size_limit_test(1000000)
array_size_limit_test(100000000)

def dict_size_limit_test(size):
    try:
        start_time = time.time()
        dict1 = {}
        for i in range(size):
            key = (i, i)
            dict1[key] = False
        print("Length of dictionary: ", len(dict1))
        print(dict1[(0, 0)])
        runtime = start_time - time.time()
        print(runtime)
    except Exception as e: 
        print("Error: Could not complete action due to a ", type(e), " error")

dict_size_limit_test(1000)
dict_size_limit_test(10000)
dict_size_limit_test(15000)
dict_size_limit_test(50000)
dict_size_limit_test(100000)
dict_size_limit_test(1000000)
dict_size_limit_test(100000000)
