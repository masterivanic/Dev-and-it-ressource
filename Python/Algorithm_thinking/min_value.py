
def find_min_value(xs):
    min_index = 0
    for i in range(len(xs)):
        if xs[i] < xs[min_index]:
            min_index = i
    return xs[min_index]


# xs = ['a', 'f', 'q' , 'b']
# min_value = find_min_value(xs)
# print(f"The minimum value is {min_value}")


def selection_sort(xs):
    for i in range(len(xs) -1):
        min_index = i
        for j in range(i + 1, len(xs)):
            if xs[j] < xs[min_index]:
                min_index  = j

        xs[i], xs[min_index] = xs[min_index], xs[i]

xs = [3, 2, 1 , 5, 4]
print(xs)
selection_sort(xs=xs)
print(xs)
print(all(xs[i] < xs[i+1] for i in range(len(xs) -1))) # nice python to check if list is sorted
