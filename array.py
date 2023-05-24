arr = ["HI", "Hello", 3]

print(f"first item: {arr[0]}")

print(f"length: {len(arr)}")

arr.append("BYE")
print(f"append: {arr}")

arr.pop()
print(f"popped: {arr}")


arr.pop(2)
print(f"popped: {arr}")

arr.remove("BYE")
print(f"removed: {arr}")