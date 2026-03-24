import time

ls_ten = [x for x in range(10)]
ls_thou = [x for x in range(10_000)]
ls_mill = [x for x in range(1_000_000)]

def add_beginning_10():
    ls_ten = [x for x in range(10)]
    before = time.perf_counter()
    ls_ten.insert(0, 100)
    after = time.perf_counter()
    result = after - before
    return result 

