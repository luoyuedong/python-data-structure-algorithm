#普通方法
def get_median(data):
    data = sorted(data)
    size = len(data)
    if size%2 == 0:
        median = (data[size//2]+data[size//2-1])/2
        data[0] = median
    if size%2 == 1:
        median = data[(size-1)//2]
        data[0] = median
    return data[0]

def get_median2(data):
    data.sort()
    half = len(data)//2
    print(data[~half],~half,half)
    return (data[half]+data[~half])/2
data = [3,5,6,1,2,4]
print(get_median2(data))