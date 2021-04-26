def calc(req_sum, d_list):
    cols = req_sum + 1
    rows = len(d_list)
    
    arr = [[0 for i in range(cols)] for j in range(rows)] 
    #hard code 1 for every row 0 col
    for x in range(len(d_list)):
        arr[x][0] = 1
    
    i = 0
    for r_iter in range(rows):
        for c_iter in range(cols):
            #skip 0
            if c_iter == 0:
                continue
                    
            if r_iter == 0:
                
                if d_list[i] <= c_iter:
                    
                    temp = c_iter - d_list[i]
                    arr[r_iter][c_iter] += arr[r_iter][temp] 
                    
            else:
                if d_list[i] > c_iter:
                    arr[r_iter][c_iter] += arr[r_iter - 1][c_iter] 
                else:
                    temp = c_iter - d_list[i]
                    value = arr[r_iter][temp] + arr[r_iter - 1][c_iter]
                    arr[r_iter][c_iter] += value
                
        i += 1
    print(arr[rows-1][cols-1])
#main
if __name__ == "__main__":        
    req_sum = int(input())
    numCoins = int(input())
    vals = input().split()
    d_list = []
    for i in vals:
        d_list.append(int(i))
        
    calc(req_sum, d_list)
