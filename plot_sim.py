from simulate import run_simulation
from price import simulate_mid 
import matplotlib.pyplot as plt

if __name__ == "__main__":
    path = simulate_mid(100.0, 2.0, 0.01, 1000, 42)
    inv,cash, pnl = run_simulation(path, 0.05, 20, 10, 0.01, 7)

    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(8, 8))
    axes[0].plot(path[1:], label="Mid Price") 
    axes[0].set_ylabel("Mid Price")
    axes[1].plot(inv, label="Inventory", color='orange')
    axes[1].set_ylabel("Inventory")
    axes[2].plot(pnl, label="PnL", color='green')
    axes[2].set_ylabel("PnL") 
    axes[2].set_xlabel("Step")
    fig.tight_layout()
    plt.savefig("sim_run.png") 
    plt.show()  # Display the plot
