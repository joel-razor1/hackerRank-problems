x = int(input())
y = int(input())
z = int(input())
n = int(input())
main_list=[]
coordinates=[]
coordinates_pack=[]

def compute(a,b,c,d):
    for i in range(0,a+1):
        for j in range(0,b+1):
            for k in range(0,c+1):
                if((i+j+k)!=d):
                    coordinates.append([i,j,k])
                    
    print(coordinates)


compute(x,y,z,n)