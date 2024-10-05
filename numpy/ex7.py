import numpy as np

time_series = np.random.rand(50)

mean_value = np.mean(time_series)
var_value = np.var(time_series)
deviation = np.std(time_series)

print(f"Математическое ожидание: {mean_value}")
print(f"Дисперсия: {var_value}")
print(f"Стандартное отклонение: {deviation}")

local_max = []
local_min = []

for i in range(1, len(time_series) - 1):
    if time_series[i] > time_series[i - 1] and time_series[i] > time_series[i + 1]:
        local_max.append(i)
    elif time_series[i] < time_series[i - 1] and time_series[i] < time_series[i + 1]:
        local_min.append(i)

print("\nЛокальные максимумы:", time_series[local_max])
print("\nЛокальные минимумы:", time_series[local_min])

p = 10
moving_average = np.convolve(time_series, np.ones(p) / p, mode='valid')
print("\nСкользящее среднее:", moving_average)
