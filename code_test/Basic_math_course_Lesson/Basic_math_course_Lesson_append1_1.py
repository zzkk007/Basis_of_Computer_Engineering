import time


def lession_append():
    even_cnt = 0
    odd_cnt = 0

    start = time.strftime("%H:%S",time.localtime())

    for i in range(100000000):

        if i & 1 == 0:
        # if i % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1

    end = time.strftime("%H:%S", time.localtime())

    print(start)
    print(end)
    print("even number[%d], odd number[%d]" % (even_cnt, odd_cnt))


if __name__ == "__main__":
    lession_append()
