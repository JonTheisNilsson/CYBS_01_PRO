from collections import Counter

def list_slicing():

    full_name  = "Svampebob Firkant"

    for i in full_name.split():
        print(i)

    

def set_test():
    x = [1,2,3,4,42]

    print(x[2:-1])

    test_set = set()
    test_set.add(3)
    test_set.add(5)
    test_set.add(7)
    test_set.add(3)
    test_set.add(42)

    if 5 in test_set:
        print(5)

    if 42 in test_set:
        print("YUO have been hacle!!!!")
    else:
        print("sun is up")


ips = [1,2,23,3,4,5,3,2,2,4,56,7,8,4,2,56,56,56,56,56,]

def ip_count(ips:list) -> dict:
    ips_count = dict()

    for ip in ips:
        ips_count[ip] = ips_count.get(ip, 0) + 1

    print(ips_count)
    return ips_count


'''
for i in set(ips):
    print(f"{i} is {ips.count(i)}")
'''


print(Counter(ips).most_common())




