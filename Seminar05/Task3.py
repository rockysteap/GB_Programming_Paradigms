from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, works_in, colleague')

+ works_in('Алексей', 'IT')
+ works_in('Игорь', 'IT')
+ works_in('Мария', 'Бухгалтерия')

# Коллеги работают в одном отделе
colleague(X, Y) <= works_in(X, Z) & works_in(Y, Z) & (X != Y)

# Запрос: кто может быть коллегой Алексея?
print(colleague('Алексей', X))
