def hill_climbing():
    current = 0
    def objective(x):
        return -(x - 5) ** 2 + 25
    while True:
        neighbors = [current - 1, current + 1]
        best_neighbor = max(neighbors, key=objective)
        if objective(best_neighbor) <= objective(current):
            break
        current = best_neighbor
    return current, objective(current)
state, value = hill_climbing()
print("Optimal State:", state)
print("Maximum Value:", value)
