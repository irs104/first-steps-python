import random
answers = ['Бесспорно', 'Мне кажется - да',	'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено', 'Вероятнее всего', 'Спроси позже',	'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

print('Привет Мир :) Я - магический шар, и я знаю ответ на любой твой вопрос')
name = input('Как тебя зовут? \n---> ')
print('\nПривет,', name.title(), end = '!')
while True:
    quest = input('\nЗадай свой вопрос и узри правду... \n---> ')
    if quest != '' and '?' in quest:
        print('\n', random.choice(answers))
    else:
        print('\nА на что отвечать? Не забывай знак "?"')
        continue
    again = input('\nХочешь узнать что-то еще?\n---> ')
    if again.lower() == 'да':
        continue
    elif again.lower() == 'нет':
        print('\nВозвращайся, если возникнут вопросы!')
        break
    else:
        print('\nПросто скажи "да" или "нет", тебя не понять...\n---> ')
        continue