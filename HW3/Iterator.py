# Итератор, который возвращает числа, начиная с 1, и увеличивает их на единицу

class MyNumbers:

# Метод, возвращающий сам обьект итератора    
    def __iter__(self):
        self.a = 1
        return self

# Метод, возвращающий следующий следующий элемент последовательности

    def __next__(self):
        if self.a <= 15: # ограничение, чтобы итерация не продолжалась вечно
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
for i in myiter:
    print(i)