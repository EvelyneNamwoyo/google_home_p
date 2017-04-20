class BinarySearch(list):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        arr= [x*2 for x in range(1,b+1)]
        lenght=len(arr)


    def search(self,val):
        count=0
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)/2
            if li[mid]==val:
                return mid
            elif li[mid]<val:
                low=mid+1
            elif li[mid]>val:
                high=mid+1
            count+=1
        return {count:li[mid]}

a=BinarySearch(6,2)
print(a.search(7))
# x = [x*2 for x in range(1,6+1)] 
# print(x)