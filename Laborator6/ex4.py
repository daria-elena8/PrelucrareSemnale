import numpy as np
import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

train_data = {}

# Citire date din Train.csv
with open("Train.csv") as train_csv:
    train_reader = csv.DictReader(train_csv, delimiter=',')
    for row in train_reader:
        train_data[int(row['ID'])] = {'datetime': datetime.strptime(row['Datetime'], "%d-%m-%Y %H:%M"),
                                      'count': int(row['Count'])}

# Selectarea datelor pentru 3 zile
start_date = train_data[0]['datetime']
end_date = start_date + timedelta(days=3)

x = [train_data[i]['count'] for i in train_data if start_date <= train_data[i]['datetime'] < end_date]

window_sizes = [5, 9, 13, 17]
smoothed_signals = {}

for w in window_sizes:
    smoothed_signals[w] = np.convolve(x, np.ones(w), 'valid') / w

fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(x)

for w, smooth_x in smoothed_signals.items():
    ax.plot(smooth_x, label=f'w = {w}')

ax.legend()

fig.savefig("semnal_netezit.pdf")
plt.show()
