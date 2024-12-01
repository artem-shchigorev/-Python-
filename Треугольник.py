a, b, c = int(input()), int(input()), int(input())
if c > a + b or a > c + b or b > c + a:
    print('Треугольника с такими сторонами не существует')
elif a == b and a == c:
    print('Треугольник равносторонний')
elif a != b and a != c and c != b:
    print('Треугольник разносторонний')
else:
    print('Треугольник равнобедренный')