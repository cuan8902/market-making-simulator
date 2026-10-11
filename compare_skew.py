import matplotlib.pyplot as plt
from price import simulate_mid
from simulate import run_simulation
path = simulate_mid(100.0, 2.0, 0.01, 1000, 42)
inv0, cash0, pnl0 = run_simulation(path, 0.05, 20, 10, 0.01, 7, 0.00)
inv1, cash1, pnl1 = run_simulation(path, 0.05, 20, 10, 0.01, 7, 0.01)
fig, axes = plt.subplots(2, 1, figsize=(10,7), sharex=True)
axes[0].plot(inv0, label="No Skew", color='blue')
axes[0].plot(inv1, label="Skew = 0.01", color='orange')
axes[0].set_ylabel("Inventory")
axes[1].set_ylabel("P&L")
axes[1].plot(pnl0, label="No Skew", color='blue')
axes[1].plot(pnl1, label="Skew = 0.01", color='orange')
axes[1].set_xlabel("Step")
axes[0].set_title("Inventory and P&L: no skew vs skew")
axes[0].legend()
axes[1].legend()
fig.tight_layout()
plt.savefig("sim_compare.png")  # Save the plot as a PNG file
plt.show()
