#Checking the input value 'N' don't lie in Non-prime numbers
def prime_number(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return(0)
        return (1)

#Enter the input N for finding the prime numbers
N=int(input("Please enter N value:"))
i=2
array_list=[]
while(1):
    if(prime_number(i)):
        array_list.append(i)
        if(len(array_list)==N):
            break
    i+=1
print("First "+str(N)+" Prime numbers are:",end="")
print(*array_list)