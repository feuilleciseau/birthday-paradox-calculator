import matplotlib.pyplot as plt


def calculate_shared_birthday_probability(group_size: int) -> float:
    """
    Calculates the probability that at least two people in a group of 'n' share the same birthday (Birthday Paradox).
    Args:
        group_size (int): The number of people in the group. Should be a positive integer.
    Returns:
        float: The probability (between 0 and 1) that at least two people share the same birthday.
    """
    if group_size < 2:
        return 0.0

    unique_prob = 1.0
    for i in range(group_size):
        unique_prob *= (365 - i)/365

    return 1 - unique_prob

def calculate_group_size_from_probability(target_prob: float) -> int:
    """
    Calculates the minimum number of people required in a group for the probability 
    that at least two of them share the same birthday to reach or exceed a given value.

    Args:
        target_prob (float): The desired probability (between 0 and 1).

    Returns:
        int: The minimum number of people needed to reach at least the given probability.
    """
    if target_prob == 0:
        return 1

    groupe_size = 2
    while calculate_shared_birthday_probability(groupe_size) < target_prob:
        groupe_size += 1

    return groupe_size

def show_graph():
    """
    Displays a graph illustrating the Birthday Paradox.

    The graph shows the probability (in percentage) that at least two people 
    in a group share the same birthday, as the group size increases from 1 to 100.

    X-axis: Number of people in the group (1 to 100)  
    Y-axis: Probability that at least two people share a birthday (%)
    """
    group_sizes = list(range(1, 101))  # De 1 à 100 personnes
    probabilities = [calculate_shared_birthday_probability(n) * 100 for n in group_sizes]  # En pourcentage

    plt.figure(figsize=(10, 6))
    plt.plot(group_sizes, probabilities, marker='o', linestyle='-', color='blue')
    plt.axhline(y=50, color='red', linestyle='--', label='50% de probabilité')
    plt.title("Birthday paradox")
    plt.xlabel("Number of people in the group")
    plt.ylabel("Probability that at least 2 people share a birthday (%)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
