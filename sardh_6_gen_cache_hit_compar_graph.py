import matplotlib.pyplot as plt

# Read from sardh_5_output_phit_parda.txt
with open("sardh_5_output_phit_parda.txt", "r") as f:
    ref_value = f.readline().strip()
    parda_hit_rate = float(ref_value)

# Read from sardh_5_output_phit_model.txt
with open("sardh_5_output_phit_model.txt", "r") as f:
    pred_value = f.readline().strip()
    model_hit_rate = float(pred_value)

labels = ["PARDA", "MODEL"]
values = [parda_hit_rate, model_hit_rate]
colors = ['blue', 'red']

plt.figure(figsize=(6, 5))
bars = plt.bar(labels, values, color=colors)

# Set y-limits close to the actual values to make bars taller
plt.ylim(min(values) - 1, max(values) + 1)
plt.ylabel('Cache Hit Rates (%)')
plt.title('Cache Hit Rate Comparison')

# Add text above bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.1, f'{height:.2f}%', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
