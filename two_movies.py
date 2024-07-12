#number of test cases
t = int(input())

#number of ratings
r_c = int(input())
for i in range(1, t+1):
    # sum up ratings and calculate the maximum value between the two movies
    r_mv1 = sum(int(x) for x in input().split())
    r_mv2 = sum(int(x) for x in input().split())
    print(max(r_mv1, r_mv2))