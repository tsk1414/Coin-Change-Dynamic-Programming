def calc(d_list, req_sum, i):
    #print(req_sum)
    if req_sum == 0:
        return 1
    if i < 0:
        return 0
    if req_sum < 0:
        return 0
    return calc(d_list, req_sum - d_list[i], i) + calc(d_list, req_sum, i - 1) 
        
        
req_sum = int(input("Enter required sum: "))
num = int(input("Enter number of coins: "))
vals = input("Enter denominations of coins: ").split()
d_list = []
for i in vals:
    d_list.append(int(i))
    
print(calc(d_list, req_sum, len(d_list)-1))
