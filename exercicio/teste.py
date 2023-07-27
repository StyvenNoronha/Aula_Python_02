caminho = 'C:\\Users\\styven\\Desktop\\python\\aula'

for i in range(50):
    with open(caminho + '\\aula0' + str(i) + '.txt', 'w') as arquivo:
        
        print('arquivo criado')
