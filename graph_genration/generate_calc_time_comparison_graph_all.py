import matplotlib.pyplot as plt

reference = {
    'PARDA': 6.522,
    'No Trace Gen': 0.0335,
    'Gen Trace Model': 59.58307504653931
}

keys = list(reference.keys())
values = list(reference.values())
x = range(len(keys))

bar_width = 0.35  # Narrow bar width to reduce space between bars

plt.figure(figsize=(10, 6))  # Slightly smaller width
bars = plt.bar(x, values, width=bar_width, color=['blue', 'orange', 'green'])

plt.xticks(x, keys, fontsize=10)
plt.ylabel('Calculation Time in Seconds')
plt.title('Calculaiton time comparison in producing Reuse Profile')

# Add labels above bars
max_height = max(values)
plt.ylim(0, max_height + 2)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, f'{height:.2f} sec', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()