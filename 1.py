my_text = list(' Напишите программу, удаляющую из текста все слова, содержащие ""абв"" '.split())
print(list(filter(lambda i: 'абв' not in i, my_text)))