# Напишите программу, удаляющую из текста все слова, содержащие "абв".

line = 'абвке оонркр вокре опабв абв'
print(f'Исходный текст: {line}')
words = line.split(' ')
new_list = []
new_list = [word for word in words if 'абв' not in word]
answer = ' '.join(new_list)
print(f'Итоговый текст: {answer}')


