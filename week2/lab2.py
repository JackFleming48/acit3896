'''
Rules:
1. Test more than once
2. Do not test 'Startup'
3. 

Mean needs to be in microseconds
'''
import time
import statistics

    # ls = []
    # before = time.perf_counter()
    # after = time.perf_counter()
    # result = (after - before) * 1_000_000
    # return result

master_ls = []

def insert_list_10():
    ls = [x for x in range(10)]
    before = time.perf_counter()
    ls.insert(0, 8)
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q1_ls = []

for x in range(100):
    q1_ls.append(insert_list_10())
    time.sleep(0.05)

print(f"The mean for question 1 is: {statistics.mean(q1_ls)}")


def insert_list_1000():
    ls = [x for x in range(1000)]
    before = time.perf_counter()
    ls.insert(0, 1)
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q2_ls = []
for x in range(100):
    q2_ls.append(insert_list_1000())
    time.sleep(0.05)

print(f"The mean for question 2 is: {statistics.mean(q2_ls)}")


def insert_list_1000000():
    ls = [x for x in range(1_000_000)]
    before = time.perf_counter()
    ls.insert(0, 1)
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q3_ls = []
for x in range(100):
    q3_ls.append(insert_list_1000000())
    time.sleep(0.05)

print(f"The mean for question 3 is: {statistics.mean(q3_ls)}")


def pop_list_10():
    ls = [x for x in range(10)]
    before = time.perf_counter()
    ls.pop(0)
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q4_ls = []

for x in range(100):
    q4_ls.append(pop_list_10())
    time.sleep(0.05)

print(f"The mean for question 4 is: {statistics.mean(q4_ls)}")



def pop_list_1000():
    ls = [x for x in range(1000)]
    before = time.perf_counter()
    ls.pop(0)
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q5_ls = []
for x in range(100):
    q5_ls.append(pop_list_1000())
    time.sleep(0.05)

print(f"The mean for question 5 is: {statistics.mean(q5_ls)}")


def pop_list_1000000():
    ls = [x for x in range(1_000_000)]
    before = time.perf_counter()
    ls.pop(0)
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q6_ls = []
for x in range(100):
    q6_ls.append(pop_list_1000000())
    time.sleep(0.05)

print(f"The mean for question 6 is: {statistics.mean(q6_ls)}")

def append_list_10():
    ls = [x for x in range(10)]
    before = time.perf_counter()
    ls.append(1)
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q7_ls =[]
for x in range(100):
    q7_ls.append(append_list_10())
    time.sleep(0.05)

print(f"The mean for question 7 is: {statistics.mean(q7_ls)}")

def append_list_1000():
    ls = [x for x in range(1000)]
    before = time.perf_counter()
    ls.append(1)
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q8_ls =[]
for x in range(100):
    q8_ls.append(append_list_1000())
    time.sleep(0.05)

print(f"The mean for question 8 is: {statistics.mean(q8_ls)}")

def append_list_1000000():
    ls = [x for x in range(1000000)]
    before = time.perf_counter()
    ls.append(1)
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q9_ls =[]
for x in range(100):
    q9_ls.append(append_list_1000000())
    time.sleep(0.5)

print(f"The mean for question 9 is: {statistics.mean(q9_ls)}")

def pop_ls_10():
    ls = [x for x in range(10)]
    before = time.perf_counter()
    ls.pop(-1)
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q10_ls = []

for x in range(100):
    q10_ls.append(pop_ls_10())
    time.sleep(0.05)

print(f"The mean for question 10 is: {statistics.mean(q10_ls)}")

def pop_ls_1000():
    ls = [x for x in range(1000)]
    before = time.perf_counter()
    ls.pop(-1)
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q11_ls = []
for x in range(100):
    q11_ls.append(pop_ls_1000())
    time.sleep(0.05)

print(f"The mean for question 11 is: {statistics.mean(q11_ls)}")


def pop_ls_1000000():
    ls = [x for x in range(1_000_000)]
    before = time.perf_counter()
    ls.pop(-1)
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q12_ls = []
for x in range(100):
    q12_ls.append(pop_ls_1000000())
    time.sleep(0.05)

print(f"The mean for question 12 is: {statistics.mean(q12_ls)}")

def in_list_10():
    ls = [x for x in range(10)]
    before = time.perf_counter()
    if 0.123 in ls:
        print()
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q13_ls = []
for x in range(100):
    q13_ls.append(in_list_10())
    time.sleep(0.05)

print(f"The mean for question 13 is: {statistics.mean(q13_ls)}")

def in_list_1000():
    ls = [x for x in range(1000)]
    before = time.perf_counter()
    if 0.123 in ls:
        print()
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q14_ls = []
for x in range(100):
    q14_ls.append(in_list_1000())
    time.sleep(0.05)

print(f"The mean for question 14 is: {statistics.mean(q14_ls)}")

def in_list_1000000():
    ls = [x for x in range(1000000)]
    before = time.perf_counter()
    if 0.123 in ls:
        print()
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q15_ls = []
for x in range(100):
    q15_ls.append(in_list_1000000())
    time.sleep(0.05)

print(f"The mean for question 15 is: {statistics.mean(q15_ls)}")

def in_dict_10():
    d = {x: x+1 for x in range (10)}
    before = time.perf_counter()
    if 0.123 in d:
        print()
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q16_ls = []
for x in range(100):
    q16_ls.append(in_dict_10())
    time.sleep(0.05)

print(f"The mean for question 16 is: {statistics.mean(q16_ls)}")

def in_dict_1000():
    d = {x: x+1 for x in range (1000)}
    before = time.perf_counter()
    if 0.123 in d:
        print()
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q17_ls = []
for x in range(100):
    q17_ls.append(in_dict_1000())
    time.sleep(0.05)

print(f"The mean for question 17 is: {statistics.mean(q17_ls)}")

def in_dict_1000000():
    d = {x: x+1 for x in range (1000000)}
    before = time.perf_counter()
    if 0.123 in d:
        print()
    after = time.perf_counter()
    result = (after - before) * 1_000_000
    return result

q18_ls = []
for x in range(100):
    q18_ls.append(in_dict_1000000())
    time.sleep(0.05)

print(f"The mean for question 18 is: {statistics.mean(q18_ls)}")

mean1 = statistics.mean(q1_ls)
mean2 = statistics.mean(q2_ls)
mean3 = statistics.mean(q3_ls)
mean4 = statistics.mean(q4_ls)
mean5 = statistics.mean(q5_ls)
mean6 = statistics.mean(q6_ls)
mean7 = statistics.mean(q7_ls)
mean8 = statistics.mean(q8_ls)
mean9 = statistics.mean(q9_ls)
mean10 = statistics.mean(q10_ls)
mean11 = statistics.mean(q11_ls)
mean12 = statistics.mean(q12_ls)
mean13 = statistics.mean(q13_ls)
mean14 = statistics.mean(q14_ls)
mean15 = statistics.mean(q15_ls)
mean16 = statistics.mean(q16_ls)
mean17 = statistics.mean(q17_ls)
mean18 = statistics.mean(q18_ls)
master_ls.append(f"Mean for q1 = {mean1}")
master_ls.append(f"Mean for q2 = {mean2}")
master_ls.append(f"Mean for q3 = {mean3}")
master_ls.append(f"Mean for q4 = {mean4}")
master_ls.append(f"Mean for q5 = {mean5}")
master_ls.append(f"Mean for q6 = {mean6}")
master_ls.append(f"Mean for q7 = {mean7}")
master_ls.append(f"Mean for q8 = {mean8}")
master_ls.append(f"Mean for q9 = {mean9}")
master_ls.append(f"Mean for q10 = {mean10}")
master_ls.append(f"Mean for q11 = {mean11}")
master_ls.append(f"Mean for q12 = {mean12}")
master_ls.append(f"Mean for q13 = {mean13}")
master_ls.append(f"Mean for q14 = {mean14}")
master_ls.append(f"Mean for q15 = {mean15}")
master_ls.append(f"Mean for q16 = {mean16}")
master_ls.append(f"Mean for q17 = {mean17}")
master_ls.append(f"Mean for q18 = {mean18}")

'''
The mean for question 1 is: 1.1029999586753547
The mean for question 2 is: 0.7799977902323008
The mean for question 3 is: 598.7100003403611
The mean for question 4 is: 0.9389992919750512
The mean for question 5 is: 1.035001769196242
The mean for question 6 is: 590.7620012294501
The mean for question 7 is: 0.4539979272522032
The mean for question 8 is: 0.3290004679001868
The mean for question 9 is: 0.4430001717992127
The mean for question 10 is: 0.8350005373358727
The mean for question 11 is: 0.7280003046616912
The mean for question 12 is: 1.2149987742304802
The mean for question 13 is: 2.3839989444240928
The mean for question 14 is: 22.571000445168465
The mean for question 15 is: 13011.415000655688
The mean for question 16 is: 3.4309999318793416
The mean for question 17 is: 3.428999916650355
The mean for question 18 is: 4.436001181602478

'''