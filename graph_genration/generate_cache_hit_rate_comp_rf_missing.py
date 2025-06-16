import matplotlib.pyplot as plt

# Data
labels = ["PARDA", "MODEL Adjusting MMR", "MODEL Without MMR"]
values = [92.45, 84.93, 92.45]
colors = ["blue", "orange", "green"]

# Plotting
plt.figure(figsize=(6, 5))
bars = plt.bar(labels, values, color=colors)

# Adding percentage labels on top of each bar
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width() / 2, value + 0.3, f'{value:.2f}%', ha='center', va='bottom', fontsize=10)

# Titles and labels
plt.title("Cache Hit Rate Comparison with Missing Memory References(MMR)")
plt.ylabel("Cache Hit Rates (%)")
plt.ylim(84, 94)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()