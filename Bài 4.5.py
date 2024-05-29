def f_X(x, a, b):
    if x >= a and x <= b:
        return 1/(b-a)
    else:
        return 0

def f_Y(y, a, b):
    if y >= a and y <= b:
        return 1/(b-a)
    else:
        return 0

def f_Z(z, a, b):
    result = 0
    for x in range(a, z+1):
        result += f_X(x, a, b) * f_Y(z-x, a ,b)
    
    return result

def F_Z(z,a,b):
    if z < 2*a:
        return 0
    elif z > 2*b:
        return 1
    elif z >= (a+b) and z <= (2*b): 
         temp= ((z-2*b)**2)/(2*(b-a)**2)
         res=1-temp
         print(res)

# Ta thay đổi giá trị của a và b nếu cần.
a = -3
b = 3

print("Hàm phân phối của Z là:")
for i in range(10): # In ra giá trị từ Z=0 đến Z=9 để kiểm tra hàm phân phối.
     print(f"F_Z({i}) =", F_Z(i,a,b))