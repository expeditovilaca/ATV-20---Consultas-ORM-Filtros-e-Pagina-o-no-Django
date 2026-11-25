#  🎮 NexusGames — Catálogo de Jogos

Aplicação web desenvolvida em **Python** e **Django** para a disciplina de **Programação para Internet**, com o objetivo de consolidar o uso de **Models**, relacionamentos (`ForeignKey`), consultas **ORM**, filtros dinâmicos via `GET` e paginação com preservação de parâmetros.

---

## 👥 Integrantes da Dupla

* **Expedito Vilaça Gualberto Duarte** 
* **Layleska Kauane Vieira da Silva**

---

## 🎯 Tema Escolhido

**Catálogo de Jogos** — Sistema de consulta de acervo digital composto por três entidades relacionadas:
* **Jogo**: nome, ano de lançamento, gênero, URL da capa e chaves estrangeiras para desenvolvedora e plataforma.
* **Desenvolvedora**: nome e país de origem.
* **Plataforma**: nome da plataforma (ex.: PC, PlayStation 5, Nintendo Switch, Xbox Series X).

---

## 🔍 Descrição dos Filtros e Paginação Implementados

As consultas são processadas por uma *Function-Based View* (`lista_jogos`) utilizando exclusivamente o **ORM do Django** (`select_related` e encadeamento de `.filter()`) antes da paginação:

1. **Pesquisa Textual (`q`):**
   * Realiza busca parcial e insensível a maiúsculas/minúsculas pelo nome do jogo utilizando `nome__icontains`.
2. **Filtro por Desenvolvedora (`desenvolvedora`):**
   * Campo `<select>` dinâmico preenchido com as desenvolvedoras cadastradas no banco, filtrando os registros via `desenvolvedora_id`.
3. **Filtro por Plataforma (`plataforma`):**
   * Campo `<select>` dinâmico preenchido com as plataformas cadastradas no banco, filtrando os registros via `plataforma_id`.
4. **Combinação Dinâmica:**
   * Todos os filtros utilizam o método `GET` e podem ser aplicados de forma isolada ou combinados simultaneamente.
5. **Paginação e Preservação de Estado (`Paginator`):**
   * Exibe **5 jogos por página** com navegação entre *Anterior* e *Próxima*, além de indicar a página atual e o total de páginas.
   * Os links de paginação repassam os parâmetros ativos (`&q=...&desenvolvedora=...&plataforma=...`) na URL, garantindo que os filtros selecionados não sejam perdidos ao trocar de página.

---

## 📸 Demonstração do Sistema

> **Instrução para a dupla:** Tire um print da tela mostrando a listagem de jogos com pelo menos um filtro/pesquisa aplicado e a barra de paginação visível, salve a imagem na raiz do projeto como `screenshot.png` e faça o commit junto com este `README.md`.

![Listagem do Catálogo de Jogos com Filtros e Paginação](screenshot.png)

---

## ⚙️ Como Executar o Projeto Localmente

```bash
# 1. Clone o repositório
git clone <URL_DO_SEU_REPOSITORIO_GITHUB>
cd catalogo_jogos

# 2. Crie e ative o ambiente virtual
python -m
