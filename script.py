we=[[0.2,0.4,0.6,0.8],[0.9,0.7,0.5,0.3],[0.4,0.1,0.2,0.3]]
ip=[[0,0,1,1],[1,0,0,0],[0,1,1,0],[0,0,0,1]]
lr=0.5
for ipno,ip in enumerate(ip):
    ele=0
    elev=float("inf")
    # find min weight
    print()
    print(f"*For Input {ipno+1}*")
    for wno,w in enumerate(we):
        c=0
        print(f"D{wno+1}",end="=")
        for i,j in zip(w,ip):
            c+=(i-j)**2
            print(f"({i}-{j})^2+",end="")
        print("=",c)
        if c<elev:
            ele=wno
            elev=c
    print(f"D{ele+1} is the winning cluster")
       
    # update cluster with min weight
    print("Updating weights")
    temp=[]
    for counter,(i,j) in enumerate(zip(we[ele],ip)):
       
        temp.append(i+(lr*(j-i)))
        print(f"w{counter+1}{ele+1}={i}+{lr}*({j}-{i})={temp[-1]}")
   

    we[ele]=temp
    print("Updated Weight Matrix")
    print(we)


 
        
        
