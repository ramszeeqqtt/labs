import random
print("#1 простая программа с циклом while")
j = 7
while j > 0:
    print(j, end=" ")
    j=j-1

print(end="\n")
print("#2 простая программа с циклом for")
i = 0
N = 10
P = [0]*10
for i in range(N):
    P[i] = i + 1
    print(P[i], end=" ") 
print(end="\n")
print("#3используя функцию range()")

print(list(range(10,15))) #range(start, stop)
print(end="\n")

print(list(range(2, 10, 2)))#range(start, stop, step)
print("#4используйте функции randint() randrange() random() enumerate()  в своей программе")
print("#1. Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.") 
A = random.randint(1,5)
B = random.randint(5,10)
print("A =",A ,"B = ",B)
if A != B:
    while A <= B:
        print(A, end=" ")
        A = A+1
print(end="\n")
print("#2. Даны два целых числа C и D. Выведите все числа от C до D включительно, в порядке возрастания,")
print("# если C < D, или в порядке убывания в противном случае")
C = random.randint(1,10)
D = random.randint(1,10)
print("C =",C ,"D = ",D)
if D <= C:
    while D <= C:
        print(D, end=" ")
        D = D+1
elif C <= D:
    while C <= D:
        print(C, end=" ")
        C = C+1
print(end="\n")
print("#3. Даны два целых числа E и F,E>F. Выведите все нечётные числа от A до B включительно, в порядке убывания.")
print("# В этой задаче можно обойтись без инструкции if.")
E = random.randint(1,10)
F = random.randint(10,20)
print("E =",E ,"F = ",F)
for i in range(F, E-1, -2):
    print(i, end=" ")
print("#4. Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.")
print("Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). Программа должна вывести номер потерянной карточки.")
print("Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.")

def find_lc(n, cards):
    return (n * (n + 1) // 2) - sum(cards)

n = int(input())
cards = [int(input()) for i in range(n - 1)]
print(find_lc(n, cards))



