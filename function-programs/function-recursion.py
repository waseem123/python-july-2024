def printnumber(num):
    if num>0:
        print(num)
        printnumber(num-1)
    
printnumber(5)

# num
# 5           5
# 4           4
# 3           3
# 2           2
# 1           1
# 0---------------------------