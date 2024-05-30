n = int(input('Первая вставка:'))
result = []
if n > 20 or n < 3:
    print('Не канон :(')
else:
    for i in range(1, 10):
        if i == n:
            continue
        else:
            for num in range(1, 20):
                if num == i:
                    continue
                else:
                    while n % (i + num) == 0:
                        result.append(i)
                        result.append(num)
                        break
print(''.join(map(str, result)))
