import numpy as np
import matplotlib.pyplot as plt


def statistics(m, n):
    mat = np.random.normal(loc=0, scale=1, size=(m, n))
    mean_row = np.mean(mat, axis=0)
    mean_col = np.mean(mat, axis=1)
    var_row = np.var(mat, axis=0)
    var_col = np.var(mat, axis=1)
    print(f"Мат. ожидание строк {mean_row}")
    print(f"Мат. ожидание столбцов {mean_col}")
    print(f"Дисперсия строк {var_row}")
    print(f"Дисперсия столбцов {var_col}")

    fig = plt.figure(figsize=(10, 10))
    axes = []

    for i in range(1, m + n + 1):
        axes.append(fig.add_subplot(m, n, i))

    for i in range(n):
        axes[i].hist(mat[:, i], bins=15)
        axes[i].set_title(f'Гистограмма столбца {i + 1}')
        axes[i].set_xlabel('Значения')
        axes[i].set_ylabel('Частота')

    for i in range(m):
        axes[n + i].hist(mat[i])
        axes[n + i].set_title(f'Гистограмма строки {i + 1}')
        axes[n + i].set_xlabel('Значения')
        axes[n + i].set_ylabel('Частота')

    plt.subplots_adjust(bottom=0.1, top=0.9, hspace=1, wspace=0.3)
    plt.show()


print(statistics(4, 2))
