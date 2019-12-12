 -- Consultas no banco de dados :
-- Minímo:
-- 2 devem usar GROUP BY e uma deve ter HAVING junto
-- 2 devem ter subconsultas (sem malandrar)
-- 1 deve usar o NOT EXIST
-- 2 devem utilizar a visão que criarmos

-- IDEIAS:

 -- 1) Consulta de Notas média dos livros de cada autor
 -- 2) Saber quantas pessoas participam de eventos de um autor
 -- 3) Saber o genero favorito de cada leitor (genero mais lido)
 -- 4) Mostrar os livros que possuem o mesmo genero de um outro livro
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


 -- 3) Saber o genero favorito de cada leitor (genero mais lido) INCOMPLETO(NAO EH TAO TRIVIAL ASSIM)
SELECT lenome, genCnt
FROM leitor JOIN leitura ON(leitor.email = leitura.fk_leitor_email)
JOIN posse_genero ON(posse_genero.fk_livro_ISBN = leitura.fk_livro_ISBN)
JOIN genero ON(genero.codgenero = posse_genero.fk_genero_codgenero)
GROUP BY genero.
HAVING MAX(SELECT codgenero FROM )


-- 5) Pesquisar qual o livro mais lido de cada leitor
select leitor.nome, count(classificacao::int) as nmr_leituras
from ((leitor join escrita on (email=FK_Leitor_email))
join livro on(FK_Livro_ISBN=isbn)) join leitura on(isbn=leitura.FK_Livro_ISBN)
where leitura.tipo = 'L'
group by leitor.nome

-- 9)retorna o escritor mais lido
select leitor.nome, count(classificacao::int) as nmr_leituras
from ((leitor join escrita on (email=FK_Leitor_email))
    join livro on(FK_Livro_ISBN=isbn)) join leitura on(isbn=leitura.FK_Livro_ISBN)
where leitura.tipo = 'L'
group by leitor.nome
order by nmr_leituras desc limit 10;


-- FUNCTIONS

-- retorna livros de um determinado genero
CREATE FUNCTION search_for_genre(
    genre VARCHAR
)
returns table(titulo VARCHAR) AS $$
SELECT livro.titulo
FROM (livro JOIN posse_genero ON(isbn=FK_Livro_ISBN)) JOIN genero ON(FK_Genero_codGenero=codGenero)
WHERE genero.nome = genre;rder by nmr_leituras desc limit 10;- 5)
