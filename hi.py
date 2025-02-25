def fruit(arr):
    count = 0
    for i in range(len(arr)):  #iterate through array
        print(arr[i])
        count +=1
        print(f"you have {count} types of fruits") #print how many types of fruits  


fruits = ["apple", "banana", "watermelon", "papaya", "durian", "strawberry", "raspberry"]

fruit(fruits)
