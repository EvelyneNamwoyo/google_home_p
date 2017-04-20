
class BinarySearch(list):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.arr=range(b,a*b+1,b)
        list.__init__(self,self.arr)
        self.length=len(self.arr)


    def search(self,val):
        count=0
        lobound=0
        hibound=len(self.arr)-1

        if val not in self.arr:
            return {'count':count, 'index':-1}
        else:

            while(lobound<=hibound):
                mid=(lobound+hibound)//2
                if self.arr[lobound]==val:
                    return {'count':count, 'index':lobound}

                elif self.arr[hibound]==val:
                    return {'count':count, 'index':hibound}

                elif self.arr[mid]==val:
                    return {'count':count, 'index':mid}

                elif self.arr[mid]<val:
                    lobound=mid+1
                    count+=1

                elif self.arr[mid]>val:
                    count+=1
                    hibound=mid-1

            return {'count':count,'index':mid}

a=BinarySearch(16,1)
print(a.search(5))
