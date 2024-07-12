# accept input, split it and cast it as int
n, k = input().split()
n, k = int(n), int(k)
sec = 0
gb = 0

# Till the number of GB uploaded is not equal to n 
for i in range(1, n+1):
    # add increment time and GB by 1
    sec += 1
    gb += 1
    # if GH is equal to n, then  break
    # else, incrememt by wait time - 1
    if gb == n:
        break
    else:
        sec += k-1
print({sec})


