# ExtraTask:
# Для заданной строки, sсостоящей из нескольких слов, разделенных некоторым количеством пробелов, 
# вернуть длину последнего слова в строке.
# Слово — это максимальная подстрока, состоящая только из непробельных символов.
# Deadline: 26.04.2022 18:00


# длина последнего слова в строке

class Leng:
    def leng(self, a):
        b = len(a[-1])
        c = a[-1]
        print(a)
        print(f'\nlast word \'{c}\' length {b} letters\n')
leng = Leng()
leng.leng(('go do birthday rabbit cat create translate google').split())