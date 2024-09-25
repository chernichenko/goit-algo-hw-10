from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, value

# Створення проблеми оптимізації
problem = LpProblem("Maximize_Production", LpMaximize)

# Визначення змінних
lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')
juice = LpVariable("Juice", lowBound=0, cat='Integer')

# Визначення цільової функції
problem += lemonade + juice, "Total_Production"

# Додавання обмежень
problem += 2 * lemonade + 1 * juice <= 100, "Water_Constraint"
problem += 1 * lemonade <= 50, "Sugar_Constraint"
problem += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
problem += 2 * juice <= 40, "Fruit_Puree_Constraint"

# Розв'язання проблеми
problem.solve()

# Виведення результатів
print("Статус:", LpStatus[problem.status])
print("Виробництво Лимонаду:", lemonade.varValue)
print("Виробництво Фруктового соку:", juice.varValue)
print("Загальна кількість продукції:", value(problem.objective))