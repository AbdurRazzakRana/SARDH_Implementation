import matplotlib.pyplot as plt

# Dictionaries
reference = {
    'Cache_s: 32 KB': 89.77,
    'Cache_s: 256 KB': 89.96,
    'Cache_s: 1024 KB': 90.05
}
predicted_1 = {
    'Cache_s: 32 KB': 89.77,
    'Cache_s: 256 KB': 89.96,
    'Cache_s: 1024 KB': 89.98
}
predicted_2 = {
    'Cache_s: 32 KB': 89.77,
    'Cache_s: 256 KB': 89.96,
    'Cache_s: 1024 KB': 90.05
}

# Extract keys and values
keys = list(reference.keys())
ref_values = [reference[k] for k in keys]
pred1_values = [predicted_1[k] for k in keys]
pred2_values = [predicted_2[k] for k in keys]

x = range(len(keys))
bar_width = 0.25

plt.figure(figsize=(10, 6))

# Plot bars with offset
ref_bars = plt.bar([i - bar_width for i in x], ref_values, width=bar_width, label='PARDA')
pred1_bars = plt.bar(x, pred1_values, width=bar_width, label='No Array Trace Gen')
pred2_bars = plt.bar([i + bar_width for i in x], pred2_values, width=bar_width, label='Gen Array Trace')

plt.ylim(0, 110)
plt.xlabel('Cache Configurations (Assoc: 8, Line Size: 64 in all setups)')
plt.ylabel('Cache Hit Rates (%)')
plt.title('Cache Hit Rate: PARDA vs Our Models')
plt.xticks(x, keys, ha='center')
plt.legend()
plt.tight_layout()

# Add percentage text above bars
for bars in [ref_bars, pred1_bars, pred2_bars]:
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, f'{height:.2f}%', ha='center', va='bottom', fontsize=9)

plt.show()