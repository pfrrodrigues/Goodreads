 -- Consultas no banco de dados :
-- Minímo:
-- 2 devem usar GROUP BY e uma deve ter HAVING junto
-- 2 devem ter subconsultas (sem malandrar)
-- 1 deve usar o NOT EXIST
-- 2 devem utilizar a visão que criarmos

-- IDEIAS:

 -- 1) Consulta de Notas média dos livros de cada autor
 -- 2) Saber quantas pessoas participam de eventos de um autor
 -- 3) Saber o livro mais lido de cada leitor
 -- 4) 
 -- 5) Pesquisar qual o livro mais lido de cada leitor
 -- 6) Pesquisar quais os livros mais lidos de um grupo
 -- 7) Saber qual a lista mais visitada
 -- 8) Descobrir quais livros sao os mais desejados
--  9)O escritor mais lido

 -- OBS: aqui estao ideias que @ArthurCamargo pensou que seriam uteis
--  e que sao relativamente mais complexas, qualquer reclamacao fique a
--  vontade para alterar, modificar e excluir

-- 1) Consulta de Notas média dos livros de cada autor
SELECT escrita.fk_leitor_email, livro.titulo, AVG(CAST(classificacao AS INT))
FROM leitor JOIN escrita
ON(leitor.email = escrita.fk_leitor_email)
JOIN leitura
ON(escrita.fk_livro_ISBN = leitura.fk_livro_ISBN)
JOIN livro
ON(escrita.fk_livro_ISBN = ISBN)
GROUP BY escrita.fk_leitor_email, livro.titulo
HAVING COUNT(CAST( classificacao AS INT)) >= 1;

-- 2) Saber quantas pessoas participam de eventos de um autor
SELECT leitor.nome, evento.descricao,  COUNT(DISTINCT fk_leitor_email_)
FROM evento JOIN leitor
ON (evento.fk_leitor_email = leitor.email)
JOIN participacao
ON (participacao.fk_leitor_email = evento.fk_leitor_email_)
GROUP BY leitor.nome, evento.descricao

-- 3) Saber o genero mais lido de cada leitor


 -- 5) Saber o livro mais lido de cada autor 
SELECT leitor.nome, livro.titulo, COUNT(livro.isbn)
FROM leitor
JOIN escrita ON (fk_leitor_email = email)
JOIN livro ON(escrita.fk_livro_isbn = isbn)
JOIN leitura ON (isbn = leitura.fk_livro_isbn)
GROUP BY leitor.email, livro.isbn
HAVING (leitor.email , COUNT(leitura.fk_livro_isbn)) IN
    (SELECT le, MAX(cntisbn)
    FROM (SELECT leitor.email le, COUNT (leitura.fk_livro_isbn) cntisbn
        FROM leitor
        JOIN escrita ON (fk_leitor_email = email)
        JOIN livro ON(escrita.fk_livro_isbn = isbn)
        JOIN leitura ON (isbn = leitura.fk_livro_isbn)
        GROUP BY leitor.email,livro.isbn) cnt
    GROUP BY le)


-- 5) Pesquisar qual o livro mais lido de cada leitor ?????
-- isso parece muito errado
select leitor.nome, count(classificacao::int) as nmr_leituras
from ((leitor join escrita on (email=FK_Leitor_email))
join livro on(FK_Livro_ISBN=isbn)) join leitura on(isbn=leitura.FK_Livro_ISBN)
where leitura.tipo = 'L'
group by leitor.nome

-- 9)retorna o top 10  escritores mais lidos
select leitor.nome, count(classificacao::int) as nmr_leituras
from ((leitor join escrita on (email=FK_Leitor_email))
join livro on(FK_Livro_ISBN=isbn)) join leitura on(isbn=leitura.FK_Livro_ISBN)
where leitura.tipo = 'L'
group by leitor.nome
order by nmr_leituras desc limit 10;


-- VIEWS
CREATE VIEW leitor_livros AS
SELECT leitor.nome, livro.titulo, livro.imagem, leitura.classificacao, leitura.tipo, autor.nome autor
FROM leitor
JOIN leitura ON (leitor.email = leitura.fk_leitor_email)
JOIN livro ON (leitura.fk_livro_isbn = livro.isbn)
JOIN escrita ON (leitura.fk_livro_isbn = escrita.fk_livro_isbn)
JOIN leitor autor ON (escrita.fk_leitor_email = autor.email);
-- Visao de leitores e seus livros

-- Queries usando essa view
SELECT leitor_livros.nome, AVG(leitor_livros.classificacao::int)
FROM leitor_livros
GROUP BY leitor_livros.nome;
-- Se quisermos setar um minimo de classificacoes
-- HAVING COUNT(leitor_livros.classificacao::int) > 10;





-- FUNCTIONS

-- retorna livros de um determinado genero
CREATE FUNCTION search_for_genre(
    genre VARCHAR
)
returns table(titulo VARCHAR) AS $$
SELECT livro.titulo
FROM (livro JOIN posse_genero ON(isbn=FK_Livro_ISBN)) JOIN genero ON(FK_Genero_codGenero=codGenero)
WHERE genero.nome = genre;rder by nmr_leituras desc limit 10;- 5)
