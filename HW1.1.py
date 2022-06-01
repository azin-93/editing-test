import operator

costumer = int(input("Enter number of costumers: "))
orders = []
for k in range(costumer):
    n = int(input("Enter number of elements : "))

max_min = []
average = 0
jobs_order = []

# Below line read inputs from user using map() function
t = list(map(int, input("\nEnter the time of each order : ").strip().split()))[:n]
l = list(map(int, input("\nEnter the loss of each order : ").strip().split()))[:n]
for i in range(n):
    average = l[i]/t[i]
    max_min.append(average)
enumerate_object = enumerate(max_min)
sorted_pairs = sorted(enumerate_object, key=operator.itemgetter(1), reverse=True)
sorted_indices = [index for index, element in sorted_pairs]
print(sorted_indices)
for j in sorted_indices:
    j+=1
    jobs_order.append(j)
print(jobs_order)
