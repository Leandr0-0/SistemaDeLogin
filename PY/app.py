'''O sistema deve permitir que novos usuários sejam cadastrados e não deve permitir
que usuários já cadastrados se recadrastem. Usuários já existentes podem fazer login e
o sistema deve alertar caos o loguns ou a senha não estejam corretos'''

# O sietema de login deve permitir que novos usuários sejam cadastrados;
# O sistema não deve permitir que usuários duplicados sejam recadastrados;
# Usuários cadastrados podem fazer login:
# O sistema deve alerta caso o login ou a senha não estejam corretos;

# O sistema deve alerta caso o login ou a senha não estejam corretos
# Permitindo que o usuário cadastrados façam login
resposta = input('[1] Cadastra novo usuário [2] Fazer login: ')

# Armazenado os usuários e existentes:
usuarios = ['carol', 'amanda', 'jeff']
senhas = ['12345', 'abcde', '123abc']


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


# Permitir que usuários já cadastrados façam login 
elif resposta == '2':

    # Pedir usuário
    usuario_digitado = input('Digite seu usuário: ')

    # Pedir senha
    senha_digitada = input('Digite sua senha: ')

    # Verificar se o usuário está na lista
    encontrado = False
    for indece, usuario in enumerate(usuarios):
        if usuario_digitado == usuario and senha_digitada == senhas[indece]:
            print('Login feito com sucesso!')
            encontrado = True
        elif encontrado == False:
            # O sistema deve alerta caso o login ou a senha não estejam corretos
            print('Usuário ou senha incorreto!')

else:
    print('Digite apenas 1 ou 2')
        
