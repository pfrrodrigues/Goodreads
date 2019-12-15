 -- Consultas no banco de dados :
-- Minímo:
-- 2 devem usar GROUP BY e uma deve ter HAVING junto ✓, ✓
-- 2 devem ter subconsultas (sem malandrar) ✓
-- 1 deve usar o NOT EXIST
-- 2 devem utilizar a visão que criarmos ✓, ✓

-- Seleciona isbn, titulo, imagem, autor, e nota de um livro
select livro.isbn, livro.titulo, livro.imagem, e.nome, leitura.tipo as marcacao, leitura.classificacao as nota
from leitor l
join leitura on (l.email=fk_leitor_email)
join livro on (fk_livro_isbn=isbn)
join escrita on (livro.isbn=escrita.fk_livro_isbn)
join leitor e on (escrita.fk_leitor_email=e.email)
-- se dermos o parametro da isbn
-- where livro.isbn = %s;

--  Consulta de Notas média dos livros de cada autor
SELECT escrita.fk_leitor_email, livro.titulo, AVG(CAST(classificacao AS INT))
FROM leitor JOIN escrita
ON(leitor.email = escrita.fk_leitor_email)
JOIN leitura
ON(escrita.fk_livro_ISBN = leitura.fk_livro_ISBN)
JOIN livro
ON(escrita.fk_livro_ISBN = ISBN)
GROUP BY escrita.fk_leitor_email, livro.titulo
HAVING COUNT(CAST( classificacao AS INT)) >= 1;

-- Saber quantas pessoas participam de eventos de um autor
SELECT leitor.nome, evento.descricao,  COUNT(DISTINCT fk_leitor_email_)
FROM evento JOIN leitor
ON (evento.fk_leitor_email = leitor.email)
JOIN participacao
ON (participacao.fk_leitor_email = evento.fk_leitor_email_)
GROUP BY leitor.nome, evento.descricao

 -- Saber o livro mais lido de cada autor 
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


-- retorna o top 10  escritores mais lidos
select leitor.nome, count(classificacao::int) as nmr_leituras
from ((leitor join escrita on (email=FK_Leitor_email))
join livro on(FK_Livro_ISBN=isbn)) join leitura on(isbn=leitura.FK_Livro_ISBN)
where leitura.tipo = 'L'
group by leitor.nome
order by nmr_leituras desc limit 10;

-- retorna as tags de uma dada lista
SELECT tagl FROM lista
JOIN posse_tagl ON (lista.codlista = posse_tagl.fk_lista_codlista)
JOIN tag_lista ON (posse_tagl.fk_tag_lista_codtagl)
-- WHERE fk_leitor_email = %s AND lista.nome =
-- Para ter os parametros do leitor e de suas listas

-- )

-- VIEWS
CREATE VIEW leitor_livros AS
SELECT leitor.nome, livro.titulo, livro.imagem, leitura.classificacao, leitura.tipo, autor.nome autor
FROM leitor
JOIN leitura ON (leitor.email = leitura.fk_leitor_email)
JOIN livro ON (leitura.fk_livro_isbn = livro.isbn)
JOIN escrita ON (leitura.fk_livro_isbn = escrita.fk_livro_isbn)
JOIN leitor autor ON (escrita.fk_leitor_email = autor.email);
-- Parametro
-- WHERE leitor.email = $$
-- Visao de leitores e seus livros

-- Queries usando essa view
SELECT leitor_livros.nome, AVG(leitor_livros.classificacao::int)
FROM leitor_livros
GROUP BY leitor_livros.nome;
-- Se quisermos setar um minimo de classificacoes
-- HAVING COUNT(leitor_livros.classificacao::int) > 10;



-- DELETIONS

DELETE FROM lista
WHERE lista.codlista = ?
-- WHERE lista.codlista = %s
--dado um codlista

DELETE FROM contem
WHERE fk_lista_codlista = ? 
-- Deleta uma lista de uma relacao de contem


DELETE FROM lista
WHERE lista.codlista = ?
-- Deleta uma lista

DELETE FROM tag_lista
WHERE NOT EXISTS(SELECT * FROM posse_tagl
    WHERE fk_tag_lista_codtagl = codtagl)
-- Deleta uma tag que nao esta sendo usada

-- ALTER TABLES



-- FUNCTIONS
create function book_util(
    isbn char
)
returns table(isbn char, titulo varchar, imagem varchar, nome varchar, tipo char, nota char) as $$
select livro.isbn, livro.titulo, livro.imagem, e.nome, leitura.tipo as marcacao, leitura.classificacao as nota
from (((leitor l join leitura on (l.email=fk_leitor_email)) join livro on (fk_livro_isbn=isbn))
    join escrita on (livro.isbn=escrita.fk_livro_isbn)) join leitor e on (escrita.fk_leitor_email=e.email)
where livro.isbn = isbn;
$$ language sql;

-- retorna os livros de um autor
create function search_author_books(
  author varchar
)
returns table(nome varchar) as $$
select livro.titulo from (leitor join escrita on(email=FK_Leitor_email)) join livro on(FK_Livro_ISBN=isbn)
where leitor.nome = author;
$$ language sql;

-- retorna livros de um determinado genero
create function search_for_genre(
  genre varchar
)
returns table(titulo varchar) as $$
  select livro.titulo
    from (livro join posse_genero on(isbn=FK_Livro_ISBN)) join genero on(FK_Genero_codGenero=codGenero)
    where genero.nome = genre;
$$ language sql;

-- retorna os lançamentos do mês
create view lancamento_editorial
	as select livro.titulo, leitor.nome, anoPublic
	from (livro join escrita on(isbn=FK_Livro_ISBN))
		join leitor on(FK_Leitor_email=email)
		where extract(month from anoPublic) = extract(month from current_date)
		and extract (year from anoPublic) = extract(year from current_date);

 -- retorna os 10 escritores mais lidos nos últimos tempos
select leitor.nome, count(classificacao::int) as nmr_leituras
  from ((leitor join escrita on (email=FK_Leitor_email))
    join livro on(FK_Livro_ISBN=isbn)) join leitura on(isbn=leitura.FK_Livro_ISBN)
    where leitura.tipo = 'L'
    group by leitor.nome
    order by nmr_leituras desc limit 10;

-- retorna os livros marcados por um leitor
-- chamada: select marked(email);
create function marked(
  user_email varchar
)
returns table(isbn char, titulo varchar, imagem varchar, nome varchar, tipo char, nota char) as $$
  select livro.isbn, livro.titulo, livro.imagem, e.nome, leitura.tipo as marcacao, leitura.classificacao as nota
    from (((leitor l join leitura on (l.email=fk_leitor_email)) join livro on (fk_livro_isbn=isbn))
    join escrita on (livro.isbn=escrita.fk_livro_isbn)) join leitor e on (escrita.fk_leitor_email=e.email)
    where l.email = user_email;
$$ language sql;


-- retorna a media de um determinado livro
create function avg_rating(
  isbn char
)
returns table(media float) as $$
  select avg(classificacao::float)
  from leitura
  where tipo='L' and fk_livro_isbn=isbn;
  $$ language sql;


-- mostra todas as informacoes de um livro
create function info_book(
  book_isbn char
)
returns table(isbn char, titulo varchar, ano date, descr varchar, img varchar, pag integer,
formato varchar, autor varchar, genero varchar) as $$
  select livro.isbn, livro.titulo, livro.anoPublic, livro.descr, livro.imagem, livro.nmrPag,
         formato.formato, leitor.nome, genero.nome
  from (((((livro join escrita on (livro.isbn=escrita.fk_livro_isbn))
        join leitor on (escrita.fk_leitor_email=leitor.email))
        join formato on (livro.fk_formato_formato_PK=formato.formato_PK))
        join posse_genero on (livro.isbn=posse_genero.FK_Livro_ISBN))
        join genero on (posse_genero.FK_Genero_codGenero=genero.codGenero))
  where livro.isbn = book_isbn;
  $$ language sql;

