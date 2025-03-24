import matplotlib.pyplot as plt

reference = {
    'Cache_s: 32 KB': 89.77,
    'Cache_s: 256 KB': 89.96,
    'Cache_s: 1024 KB': 90.05
}
predicted = {
    'Cache_s: 32 KB': 89.77,
    'Cache_s: 256 KB': 89.96,
    'Cache_s: 1024 KB': 90.05
}

keys = list(predicted.keys())
ref_values = [reference.get(k, 0) for k in keys]
pred_values = [predicted[k] for k in keys]

x = range(len(keys))
bar_width = 0.4

plt.figure(figsize=(10, 6))
ref_bars = plt.bar([i - bar_width/2 for i in x], ref_values, width=bar_width, label='PARDA')
pred_bars = plt.bar([i + bar_width/2 for i in x], pred_values, width=bar_width, label='Our Model')

plt.ylim(0, 110)
plt.xlabel('Cache Configurations ( Assoc: 8, Line Size: 64 in all setups)')
plt.ylabel('Cache Hit Rates (%)')
plt.title('Cache Hit Rate PARDA vs our model')
plt.xticks(x, keys, ha='center')
plt.legend()
plt.tight_layout()

# Add percentage text above bars
for bar in ref_bars + pred_bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.05, f'{height:.2f}%', ha='center', va='bottom', fontsize=9)

plt.show()
