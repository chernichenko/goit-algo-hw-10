import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло
def monte_carlo_integration(func, a, b, num_samples=10000):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, func(b), num_samples)
    
    # Площа під кривою
    under_curve = y_random < func(x_random)
    area = (b - a) * func(b) * np.mean(under_curve)
    
    return area

# Обчислення інтеграла методом Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b)
print("Результат методом Монте-Карло:", monte_carlo_result)

# Перевірка результату за допомогою функції quad
result, error = spi.quad(f, a, b)
print("Інтеграл (функція quad):", result, "Абсолютна помилка:", error)

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()