def linear_search(arr,target):
  for i in range (len(arr)):
    if arr[i]==target:
      return i # Return the index if target if found return -1 # Return -1 if target is not in the array
# Example usage 
arr=[10,5,7,15,20]
target=7
result =linear_search(arr,target)
if result!=-1:
  print (f"Element{target}found at index{result}")
else:
  print(f"Element{target}not found in the array.")