from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, W, likes, has_common_interest, mutual_interest_group')

# Расширяем список интересов
+ likes('Алексей', 'Футбол')
+ likes('Игорь', 'Футбол')
+ likes('Светлана', 'Теннис')
+ likes('Мария', 'Теннис')
+ likes('Олег', 'Футбол')
+ likes('Анна', 'Бег')
+ likes('Сергей', 'Теннис')
+ likes('Ольга', 'Бег')
+ likes('Иван', 'Плавание')

# Определяем, кто имеет общие интересы
has_common_interest(X, Y) <= likes(X, Z) & likes(Y, Z) & (X != Y)

# Группа с общими интересами
mutual_interest_group(X, Y, Z) <= likes(X, W) & likes(Y, W) & likes(Z, W) & (X != Y) & (Y != Z) & (X != Z)

# Запросы
# print("С кем у Алексея общий интерес в футболе:", has_common_interest('Алексей', X))
# print("С кем у Светланы общий интерес в теннисе:", has_common_interest('Светлана', X))
print("Группа с общим интересом в теннисе:", mutual_interest_group(X, Y, 'Игорь'))