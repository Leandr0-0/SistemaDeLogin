'''O sistema deve permitir que novos usuários sejam cadastrados e não deve permitir
que usuários já cadastrados se recadrastem. Usuários já existentes podem fazer login e
o sistema deve alertar caso o algum ou a senha não estejam corretos'''

# Permitir que novos usuários sejam cadastrados;
# Não deve permitir que usuários já cadastrados sejam recadastrados;
# Usuários cadastrados podem fazer login;
# Alerta caso o login ou a senha não estejam corretos;
# Permitindo que o usuário cadastrados façam login

resposta = input('[1] Cadastra novo usuário [2] Fazer login: ')

# Armazenado os usuários existentes:
usuarios = ['Leo', 'Luiz', 'Filipe']
senhas = ['BolinhaDeGolf', 'r2d2c3po', 'RuffGhanor']

if resposta == '1':
    # Recebendo um usuario:
    usuario_digitado = input('Digite seu usuário: ')
    if usuario_digitado in usuarios:
        print('Usuário existente!')
        
    else:
        # Recebendo uma senha:
        senha_digitada = input('Digite sua senha: ')

        # Caso não exista, cadastrar usuário e senha:
        usuarios.append(usuario_digitado)
        senhas.append(senha_digitada)

        # Confirmação de Adição de usuário:
        print(usuarios)


# Permitir que usuários já cadastrados façam login 
elif resposta == '2':

    # Pedir usuário
    usuario_digitado = input('Digite seu usuário: ')

    # Pedir senha
    senha_digitada = input('Digite sua senha: ')

    # Verificar se o usuário está na lista
    encontrado = False
    for indece, usuarios in enumerate(usuarios):
        if usuario_digitado == usuarios and senha_digitada == senhas[indece]:
            print('Login feito com sucesso!')
            encontrado = True
        elif encontrado == False:
            # O sistema deve alerta caso o login ou a senha não estejam corretos
            print('Usuário ou senha incorreto!')

else:
    print('Digite apenas 1 ou 2')
   
