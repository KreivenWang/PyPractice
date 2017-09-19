val = '-0.022123,0.32141,1,1.3214,1.0'
arr = val.split(',')

toFloat1 = list(map(lambda x: float(x)*2, arr))
print('float1:')
print(toFloat1)

toFloat2 = [float(item)*2 for item in arr]
print('float2:')
print(toFloat2)

