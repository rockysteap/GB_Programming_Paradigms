from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, W, V, likes, has_common_interest, mutual_interest_group, shared_multiple_interests')

# Расширенный список интересов
+ likes('Алексей', 'Футбол')
+ likes('Игорь', 'Футбол')
+ likes('Светлана', 'Теннис')
+ likes('Мария', 'Теннис')
+ likes('Олег', 'Футбол')
+ likes('Анна', 'Бег')
+ likes('Сергей', 'Теннис')
+ likes('Ольга', 'Бег')
+ likes('Иван', 'Плавание')
+ likes('Иван', 'Теннис')
+ likes('Ольга', 'Футбол')
+ likes('Анна', 'Плавание')
+ likes('Мария', 'Бег')
# + likes('Анна', 'Футбол')


# Определяем, кто имеет общие интересы
has_common_interest(X, Y) <= likes(X, Z) & likes(Y, Z) & (X != Y)

# Группа с общими интересами
mutual_interest_group(X, Y, Z) <= likes(X, W) & likes(Y, W) & likes(Z, W) & (X != Y) & (Y != Z) & (X != Z)

# Люди с множественными общими интересами
shared_multiple_interests(X, Y, Z, W) <= likes(X, V) & likes(Y, V) & likes(X, Z) & likes(Y, Z) & (V != Z) & (X != Y)

# Запросы
# print("С кем у Алексея общий интерес:", has_common_interest('Алексей', X))
# print("Группа с общим интересом в теннисе:", mutual_interest_group(X, Y, 'Теннис'))
print("Люди с множественными общими интересами (например, Футбол и Бег):", shared_multiple_interests(X, Y, 'Футбол', 'Бег'))