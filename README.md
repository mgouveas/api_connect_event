# Connect

Bem-vindo ao **Connect**! Este projeto tem como objetivo gerenciar eventos, participantes e links personalizados". Este repositório foi criado para facilitar a colaboração e o onboarding de novos desenvolvedores.

## Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Testes](#testes)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Contato](#contato)

---

## Visão Geral

O **Connect** é uma API desenvolvida em Python com o objetivo de facilitar o gerenciamento de eventos e participantes, além de permitir a geração de links personalizados para cada evento. A aplicação foi pensada para ser simples de integrar a outros sistemas e fácil de utilizar, tanto para desenvolvedores quanto para usuários finais.

Com o Connect, é possível cadastrar eventos, adicionar participantes, gerar e rastrear links exclusivos para divulgação e acompanhar o engajamento dos participantes por meio de rankings. O projeto é modular, utiliza boas práticas de desenvolvimento e está aberto para contribuições da comunidade.

Ideal para equipes que desejam organizar eventos, monitorar a participação e engajamento de usuários, ou integrar funcionalidades de eventos em suas próprias

## Funcionalidades

- Cadastro de eventos
- Cadastro de participantes
- Geração de links personalizados para eventos
- Ranking de participantes por link

## Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- Cerberus
- pytest
- SQLite

## Como Executar o Projeto

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/mgouveas/api_connect_event.git
   cd connect
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados:**
   - O projeto utiliza SQLite. O arquivo `schema.db` será criado automaticamente.
   - Para criar as tabelas manualmente, utilize o script em `init/schema.sql`.

5. **Execute a aplicação:**
   ```sh
   python main.py
   ```
   O servidor estará disponível em [http://localhost:3000](http://localhost:3000).

## Estrutura do Projeto

```
connect/
├── main.py
├── requirements.txt
├── schema.db
├── init/
│   └── schema.sql
├── src/
│   ├── controllers/
│   ├── http_types/
│   ├── main/
│   ├── model/
│   └── validators/
└── ...
```

- `src/controllers`: Lógica de negócio dos módulos.
- `src/http_types`: Tipos de requisição e resposta HTTP.
- `src/main`: Rotas e servidor Flask.
- `src/model`: Entidades, repositórios e configurações do banco.
- `src/validators`: Validações de entrada.
- `init`: Scripts de inicialização do banco de dados.

## Testes

O projeto utiliza **pytest** para testes automatizados.

Para rodar todos os testes:

```sh
pytest
```

Os testes estão localizados em `src/model/repositories` com o sufixo `_test.py`.

## Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork este repositório.
2. Crie uma branch para sua feature ou correção (`git checkout -b minha-feature`).
3. Commit suas alterações (`git commit -m 'Minha nova feature'`).
4. Push para o branch (`git push origin minha-feature`).
5. Abra um Pull Request.

Consulte o arquivo CONTRIBUTING.md para mais detalhes.  

## Licença

MIT

## Contato

- Responsável: [a ser adicionado]
- E-mail: [a ser adicionado]
- Outras formas de contato: [a ser adicionado]

---

Sinta-se à vontade para abrir issues e sugerir melhorias. Boas contribuições!
