'''O sistema deve permitir que novos usuários sejam cadastrados e não deve permitir
que usuários já cadastrados se recadrastem. Usuários já existentes podem fazer login e
o sistema deve alertar caos o loguns ou a senha não estejam corretos'''

# O sietema de login deve permitir que novos usuários sejam cadastrados;
# O sistema não deve permitir que usuários duplicados sejam recadastrados;
# Usuários cadastrados podem fazer login:
# O sistema deve alerta caso o login ou a senha não estejam corretos;
# Criar um banco de dados.

# Permitindo que o usuário cadastrados façam login

resposta = input('[1] Cadastra novo usuário [2] Fazer login: ')

# Armazenado os usuários e existentes:
usuarios = ['carol', 'amanda', 'jeff']
senhas = ['12345', 'abcde', '123abc']

if resposta =='1':
    # Recebendo um usuario:
    usuario_digitado = input('Digite seu usuário: ')

    # Recebendo uma senha:
    senha_digitada = input('Digite sua senha: ')

    # Caso não exista, cadastrar usuário e senha:
    usuarios.append(usuario_digitado)
    senhas.append(senha_digitada)

    # Confirmar que funcionou
    print(usuarios)

# Permitir que usuários já cadastrados façam login 
elif resposta == '2':
    # Permitir que usuários já cadastrados possam fazer login

    # Pedir usuário
    usuario_digitado = input('Digite seu usuário: ')
    # Pedir senha
    senha_digitada = input('digite sua senha: ')
    # Verificar se o usuário está na lista
    if usuario_digitado in usuarios:
        print('Encontrado!')
    # Verificar se a senha fornecida pelo usuário e a mesma da lista