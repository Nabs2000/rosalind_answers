
def rabbits_and_recurrence_relations(file):
    with open(file, 'r') as f:
        n, k = f.readline().split(" ")
        n, k = int(n), int(k)
        print('n:', n)
        print('k:', k)
    months = [0] * (n + 1)
    months[1] = 1
    for i in range(2, n + 1):
        # Recurrence relation: F_{i} = F_{i-1} + 4F_{i-2}
        months[i] = months[i - 1] + (k * months[i - 2])
    return months[n]