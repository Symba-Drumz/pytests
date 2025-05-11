def add(num):
    return num + 3
print(add(2))

def is_even(num):
    return num % 2 == 0
print(is_even(2))

def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    return average
scores = [90, 80, 70, 60]
print("Average score:", calculate_average(scores))