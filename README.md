### Documento Descritivo do Trabalho

 Introdução
A empresa modelada é uma empresa de TI fictícia chamada "Tech Solutions", que oferece serviços de desenvolvimento de software, manutenção e consultoria técnica. O sistema gerencia dois tipos de informação: usuários e serviços. Os tipos de usuário incluem:
- **Gerente:** Tem todas as permissões para gerenciar usuários e serviços.
- **Desenvolvedor:** Pode gerenciar apenas serviços.
- **Cliente:** Pode visualizar serviços, mas não pode gerenciar usuários nem serviços.

 Implementação
Para cada elemento do sistema (usuário e serviço), são descritas a estrutura de dados escolhida, o arquivo de registro e a lista de funcionalidades.

 Usuários
1. **Estrutura de Dados:** A informação dos usuários é carregada em uma lista de dicionários, onde cada dicionário contém os campos 'nome', 'senha' e 'permissao'.
2. **Arquivo de Registro:** O arquivo `usuarios.csv` contém as informações dos usuários, com cada linha representando um usuário no formato `nome,senha,permissao`.
3. **Funcionalidades (CRUD):**
   - **Create:** Função `criar_usuario()` permite adicionar novos usuários.
   - **Read:** Função `listar_usuarios()` permite listar todos os usuários.
   - **Update:** Função `atualizar_usuario()` permite atualizar informações de um usuário existente.
   - **Delete:** Função `deletar_usuario()` permite remover um usuário.

 Serviços
1. **Estrutura de Dados:** A informação dos serviços é carregada em uma lista de dicionários, onde cada dicionário contém os campos 'codigo', 'nome', 'descricao' e 'preco'.
2. **Arquivo de Registro:** O arquivo `servicos.csv` contém as informações dos serviços, com cada linha representando um serviço no formato `codigo,nome,descricao,preco`.
3. **Funcionalidades (CRUD):**
   - **Create:** Função `criar_servico()` permite adicionar novos serviços.
   - **Read:** Função `listar_servicos()` permite listar todos os serviços.
   - **Update:** Função `atualizar_servico()` permite atualizar informações de um serviço existente.
   - **Delete:** Função `deletar_servico()` permite remover um serviço.
   - **Buscar:** Função `buscar_servico()` permite buscar um serviço específico por código.
   - **Ordenar por Nome:** Função `ordenar_servicos_por_nome()` permite listar os serviços ordenados por nome.
   - **Ordenar por Preço:** Função `ordenar_servicos_por_preco()` permite listar os serviços ordenados por preço.

 Conclusão
Durante o desenvolvimento do sistema, encontramos algumas dificuldades, como garantir a segurança e a eficiência no login dos usuários e a manipulação de arquivos CSV para armazenar dados de forma persistente. Escolhas bem-sucedidas incluem o uso de dicionários para estruturar dados de forma clara e o uso de funções separadas para cada operação CRUD, garantindo modularidade e facilidade de manutenção do código.

No futuro, poderíamos adicionar funcionalidades como recuperação de senha, criptografia de senhas, e uma interface gráfica para melhorar a experiência do usuário. Além disso, a validação mais robusta de entrada de dados e a gestão de permissões mais granular poderiam ser implementadas para melhorar a segurança e a flexibilidade do sistema.
