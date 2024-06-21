import csv
import os
import math

# Função para criar arquivos iniciais se não existirem
def criar_arquivos_iniciais():
    if not os.path.exists('usuarios.csv'):
        with open('usuarios.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Adicionando usuários de exemplo
            writer.writerow(['admin', 'admin123', 'gerente'])
            writer.writerow(['dev', 'dev123', 'desenvolvedor'])
            writer.writerow(['cliente1', 'cliente123', 'cliente'])
    
    if not os.path.exists('servicos.csv'):
        with open('servicos.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Adicionando serviços de exemplo
            writer.writerow(['001', 'Desenvolvimento Web', 'Criação de websites', '1500.00'])
            writer.writerow(['002', 'Manutenção de Software', 'Correção de bugs e melhorias', '500.00'])
            writer.writerow(['003', 'Consultoria Técnica', 'Consultoria em TI', '300.00'])

# Função para carregar usuários do arquivo
def carregar_usuarios():
    usuarios = []
    if os.path.exists('usuarios.csv'):
        with open('usuarios.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                usuarios.append({
                    'nome': row[0],
                    'senha': row[1],
                    'permissao': row[2]
                })
    return usuarios

# Função para carregar serviços do arquivo
def carregar_servicos():
    servicos = []
    if os.path.exists('servicos.csv'):
        with open('servicos.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                servicos.append({
                    'codigo': row[0],
                    'nome': row[1],
                    'descricao': row[2],
                    'preco': float(row[3])
                })
    return servicos

# Funções CRUD para usuários

def criar_usuario(usuarios):
    nome = input("Nome do usuário: ")
    senha = input("Senha do usuário: ")
    permissao = input("Permissão do usuário (gerente/desenvolvedor/cliente): ")
    usuarios.append({'nome': nome, 'senha': senha, 'permissao': permissao})
    salvar_usuarios(usuarios)
    print("Usuário criado com sucesso.")

def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for usuario in usuarios:
            writer.writerow([usuario['nome'], usuario['senha'], usuario['permissao']])

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Permissão: {usuario['permissao']}")

def atualizar_usuario(usuarios):
    nome = input("Nome do usuário a ser atualizado: ")
    for usuario in usuarios:
        if usuario['nome'] == nome:
            nova_senha = input("Nova senha: ")
            nova_permissao = input("Nova permissão: ")
            usuario['senha'] = nova_senha
            usuario['permissao'] = nova_permissao
            salvar_usuarios(usuarios)
            print("Usuário atualizado com sucesso.")
            return
    print("Usuário não encontrado.")

def deletar_usuario(usuarios):
    nome = input("Nome do usuário a ser deletado: ")
    for usuario in usuarios:
        if usuario['nome'] == nome:
            usuarios.remove(usuario)
            salvar_usuarios(usuarios)
            print("Usuário deletado com sucesso.")
            return
    print("Usuário não encontrado.")

# Funções CRUD para serviços

def criar_servico(servicos):
    codigo = input("Código do serviço: ")
    nome = input("Nome do serviço: ")
    descricao = input("Descrição do serviço: ")
    preco = float(input("Preço do serviço: "))
    servicos.append({'codigo': codigo, 'nome': nome, 'descricao': descricao, 'preco': preco})
    salvar_servicos(servicos)
    print("Serviço criado com sucesso.")

def salvar_servicos(servicos):
    with open('servicos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for servico in servicos:
            writer.writerow([servico['codigo'], servico['nome'], servico['descricao'], servico['preco']])

def listar_servicos(servicos):
    for servico in servicos:
        print(f"Código: {servico['codigo']}, Nome: {servico['nome']}, Descrição: {servico['descricao']}, Preço: {servico['preco']}")

def atualizar_servico(servicos):
    codigo = input("Código do serviço a ser atualizado: ")
    for servico in servicos:
        if servico['codigo'] == codigo:
            novo_nome = input("Novo nome: ")
            nova_descricao = input("Nova descrição: ")
            novo_preco = float(input("Novo preço: "))
            servico['nome'] = novo_nome
            servico['descricao'] = nova_descricao
            servico['preco'] = novo_preco
            salvar_servicos(servicos)
            print("Serviço atualizado com sucesso.")
            return
    print("Serviço não encontrado.")

def deletar_servico(servicos):
    codigo = input("Código do serviço a ser deletado: ")
    for servico in servicos:
        if servico['codigo'] == codigo:
            servicos.remove(servico)
            salvar_servicos(servicos)
            print("Serviço deletado com sucesso.")
            return
    print("Serviço não encontrado.")

# Função de login
def login(usuarios):
    while True:
        print("\n1 - Login")
        print("2 - Criar novo usuário")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome de usuário: ")
            senha = input("Senha: ")
            for usuario in usuarios:
                if usuario['nome'] == nome and usuario['senha'] == senha:
                    print(f"Bem-vindo, {usuario['nome']}! Permissão: {usuario['permissao']}")
                    return usuario
            print("Nome de usuário ou senha incorretos.")
        
        elif opcao == "2":
            criar_usuario(usuarios)
        
        else:
            print("Opção inválida.")

# Função para ordenar e buscar serviços
def buscar_servico(servicos, codigo):
    for servico in servicos:
        if servico['codigo'] == codigo:
            return servico
    return None

def ordenar_servicos_por_nome(servicos):
    return sorted(servicos, key=lambda x: x['nome'])

def ordenar_servicos_por_preco(servicos):
    return sorted(servicos, key=lambda x: x['preco'])

# Função principal
def main():
    criar_arquivos_iniciais()
    usuarios = carregar_usuarios()
    servicos = carregar_servicos()
    
    # Executa o login
    usuario_atual = login(usuarios)
    
    while True:
        print("\n1 - Gerenciar usuários")
        print("2 - Gerenciar serviços")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            if usuario_atual['permissao'] == 'gerente':
                print("\n1 - Criar usuário")
                print("2 - Listar usuários")
                print("3 - Atualizar usuário")
                print("4 - Deletar usuário")
                print("5 - Voltar")
                
                opcao_usuario = input("Escolha uma opção: ")
                
                if opcao_usuario == "1":
                    criar_usuario(usuarios)
                elif opcao_usuario == "2":
                    listar_usuarios(usuarios)
                elif opcao_usuario == "3":
                    atualizar_usuario(usuarios)
                elif opcao_usuario == "4":
                    deletar_usuario(usuarios)
                elif opcao_usuario == "5":
                    continue
                else:
                    print("Opção inválida.")
            else:
                print("Acesso negado. Você não tem permissão para gerenciar usuários.")
        
        elif opcao == "2":
            print("\n1 - Criar serviço")
            print("2 - Listar serviços")
            print("3 - Atualizar serviço")
            print("4 - Deletar serviço")
            print("5 - Buscar serviço")
            print("6 - Ordenar serviços por nome")
            print("7 - Ordenar serviços por preço")
            print("8 - Voltar")
            
            opcao_servico = input("Escolha uma opção: ")
            
            if opcao_servico == "1":
                criar_servico(servicos)
            elif opcao_servico == "2":
                listar_servicos(servicos)
            elif opcao_servico == "3":
                atualizar_servico(servicos)
            elif opcao_servico == "4":
                deletar_servico(servicos)
            elif opcao_servico == "5":
                codigo = input("Digite o código do serviço: ")
                servico = buscar_servico(servicos, codigo)
                if servico:
                    print(f"Código: {servico['codigo']}, Nome: {servico['nome']}, Descrição: {servico['descricao']}, Preço: {servico['preco']}")
                else:
                    print("Serviço não encontrado.")
            elif opcao_servico == "6":
                servicos_ordenados = ordenar_servicos_por_nome(servicos)
                for servico in servicos_ordenados:
                    print(f"Código: {servico['codigo']}, Nome: {servico['nome']}, Descrição: {servico['descricao']}, Preço: {servico['preco']}")
            elif opcao_servico == "7":
                servicos_ordenados = ordenar_servicos_por_preco(servicos)
                for servico in servicos_ordenados:
                    print(f"Código: {servico['codigo']}, Nome: {servico['nome']}, Descrição: {servico['descricao']}, Preço: {servico['preco']}")
            elif opcao_servico == "8":
                continue
            else:
                print("Opção inválida.")
        
        elif opcao == "3":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
