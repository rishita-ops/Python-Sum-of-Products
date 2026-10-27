"""
a(n+1)=1/(1+(1/a(n))))
a1=1
(a1*a2)+(a2*a3)+........(a(n-1)*an)=??
"""
n=int(input("Enter n : "))
ca=1.0
ts=0.0

for i in range(1,n):
    na=1/(1+(1/ca))
    ts+=(ca*na)

    ca=na

print(f"The sum is : {ts}")