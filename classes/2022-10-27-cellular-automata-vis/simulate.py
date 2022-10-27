"""
1. What is the simplest simulation we can come up with?
  - "Elementary Cellular Automata"
  - Sometimes show up as simple epidemiological models
2. Introduce three types of visualizations
  - 2D data ("images")
  - Line plots
  - Networks
3. Use this as a way to jump into health visualizations
  - Open access data
"""

import numpy as np
from numpy.random import default_rng
import networkx as nx
import matplotlib.pyplot as plt


def step(state: list, rule: dict) -> list:
    s = [state[-1]] + state + [state[0]]
    new_state = state.copy()

    for i, (x, y, z) in enumerate(zip(s, s[1:], s[2:])):
        new_state[i] = rule[(x, y, z)]

    return new_state


def simulate(initial_state: list, rule: dict, iters: int = 10) -> np.ndarray:

    state_space = np.zeros((iters, len(initial_state)))

    state = initial_state
    state_space[0] = initial_state

    for i in range(1, iters):
        state = step(state, rule)
        state_space[i] = state

    return state_space


def simulate_ratio(initial_state: list, rule: dict, iters: int = 10) -> None:

    state_space = np.zeros((iters, len(initial_state)))

    state = initial_state
    state_space[0] = initial_state

    for i in range(1, iters):
        state = step(state, rule)
        state_space[i] = state

    plt.plot(state_space.sum(axis=1) / state_space.shape[1])
    plt.show()


def plot2d(data: np.ndarray) -> None:
    fig, ax = plt.subplots()
    ax.imshow(data, cmap="gray", aspect="equal")
    plt.axis("off")
    plt.show()


def make_rule(number: int) -> dict:
    assert 0 <= number <= 255
    states = [
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1),
    ]
    return {s: int(t) for s, t in zip(states, format(255 - number, "08b"))}


def hash_state(state: list) -> int:
    return sum((2**i) * j for i, j in enumerate(state))


def simulate_network(initial_state: list, rule: dict, iters: int = 10) -> None:

    G = nx.DiGraph()
    state = initial_state

    for _ in range(iters):
        i: int = hash_state(state)
        state = step(state, rule)
        j: int = hash_state(state)

        G.add_edge(i, j)

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":

    rng = default_rng()

    # Sample a random start state using a binomial distribution
    initial_state: list = rng.binomial(1, 0.5, size=10).tolist()

    # Show an image of the running rule 90 for 20 iterations
    plot2d(simulate(initial_state, make_rule(90), iters=20))

    # Show the ratio between on/off states over 100 iterations
    simulate_ratio(initial_state, make_rule(90), iters=100)

    # There appeared to be some periodic behavior, what does the network look like?
    simulate_network(initial_state, make_rule(105), iters=500)
