def remove_duplicates(arr):
    
   
    if arr is None:
        print("")
    elif len(arr)==0:
        print("")
    else:
        ans=list(dict.fromkeys(arr))
        a=" "
        for i in range(0,len(ans)):
            a+=str(ans[i])
        print(a.join())

remove_duplicates([1,2,2,3,4])        