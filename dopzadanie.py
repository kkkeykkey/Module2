import random


def gtn():
    num_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win = random.choice(num_)
    return win


win = gtn()

print('Привет! Давай сыграем в игру! Я уже загадал число от 1 до 10, а ты должен его отгадать! Ну что, поехали!:)')
first = int(input('Я знаю, это невозможно, но попробуй угадать с первой попытки:'))
if first == win:
    print('Я не верю, да тебе срочно нужно на битву экстрасенсов 0.0')

else:
    print('Ай, ты был так близок! Если, конечно, не учитывать, что чисел всего десять))')
    second = int(input('Это уже твоя вторая попытка, всего их три,'
                       ' поэтому подключи ВСЕ свои экстрасенсорные способности, чтобы выиграть:'))
    if second == win:
        print('Как же ты хорош, а может тебе стоит провериться на супер-дупер чтение мыслей?'
              ' Этому городу уже давно нужен новый герой!')
    else:
        print('Ладно, я дам тебе подсказку:')
        if win == 1:
            print('Ты всегда для мамы на этом месте ;)')
        if win == 2:
            print('Ты не хочешь получить эту оценку за важную контрольную Т.Т')
        if win == 3:
            print('о, о, эта подсказка для фанатов Гарри Поттера: Сколько голов у милой собачки по кличке "Пушок"?')
        if win == 4:
            print('Их было ..., ... пацана')
        if win == 5:
            print('Посмотри на свою руку, сколько там пальчиков???')
        if win == 6:
            print('Если это число написать три раза подряд, то все бабули во дворе будут называть тебя богохульником))')
        if win == 7:
            print('Сколько цветов в радуге? Да, да, тот самый цвет мы тоже считаем))')
        if win == 8:
            print('Знак бесконечнааааааааааааааасть ©Земфира')
        if win == 9:
            print('Кошкам повезло, ведь иммено столько у них жизней)')
        if win == 10:
            print('Чирик)))')
        third = int(input('Итак, твой ответ:'))
        if third == win:
            print('WE ARE THE CHAMPIONS!!!!')
        else:
            print('Давай попробуем еще раз? Мое число было:', win)

