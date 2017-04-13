from subprocess import check_output
import re
import sys

def network_test():
    r = check_output(["speedtest-cli", "--simple"]).split("\n")
    l = [None] * 3
    l[0] = r[1].split(":")[1][1:]
    l[1] = r[2].split(":")[1][1:]
    l[2] = r[0].split(":")[1][1:]
    print(l)
    return l

def main():
    avg_down = 0
    avg_up = 0
    avg_latency = 0
    n = int(sys.argv[1])
    print(n)
    print(range(n))
    for index in range(n):
        run = network_test()
        nums = re.findall(r'([\d.]+)', str(run))
        avg_down += float(nums[0])
        avg_up += float(nums[1])
        avg_latency += float(nums[2])
    avg_up /= n
    avg_down /= n
    avg_latency /= n
    print "Download: ", str(avg_down), " Upload: ", str(avg_up), " Latency: ", str(avg_latency)

if __name__ == "__main__":
    main()
