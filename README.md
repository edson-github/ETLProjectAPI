# Projeto ETL com Python

Este projeto é uma implementação de um pipeline ETL (Extract, Transform, Load) utilizando Python. O objetivo é extrair dados de uma API, transformá-los conforme necessário e carregá-los em um banco de dados ou outro sistema de armazenamento.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Requests**: Biblioteca para realizar requisições HTTP.
- **Pandas**: Biblioteca para manipulação e análise de dados (opcional, mas recomendada para transformações).
- **SQLAlchemy**: Biblioteca para interagir com bancos de dados (opcional, mas recomendada para a etapa de carregamento).

## Estrutura do Projeto

```

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/etl_project.git
   cd etl_project
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:

   Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

   ```
   OPENAI_API_KEY=sua_chave_api_aqui
   ```

   Este arquivo será usado para armazenar chaves de API e outras informações sensíveis que não devem ser compartilhadas no controle de versão.

## Uso

1. Configure as variáveis de ambiente necessárias (por exemplo, chaves de API, URLs de banco de dados, etc.).

2. Execute o script ETL:

   ```bash
   python etl.py
   ```



## Contribuição

Sinta-se à vontade para abrir issues e enviar pull requests. Para mudanças importantes, por favor, abra uma issue primeiro para discutir o que você gostaria de mudar.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
