import matplotlib.pyplot as plt
import numpy as np
import random

n = 5000

def roll():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    return x + y

def simulation(n):
    results = []
    for _ in range(n):
        results.append(roll())
    return results

def visualize():
    results = simulation(n)
    counts = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
    values = []
    for i in range(13):
        counter = 0
        for j in range(len(results)):
            if results[j] == i:
                counter+=1
        values.append(counter)
    values.pop(0)
    y_pos = np.arange(len(counts))
    plt.bar(y_pos, values)
    plt.xticks(y_pos, counts)
    plt.show()

if __name__ == "__main__":
    visualize()
