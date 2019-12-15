-- Etapa 2:
-- Item 2)Manipulação da Base de Dados: Consultas, Visões, Gatilhos e Procedimentos

-- Item2.a) Definir uma visão útil a seu universo de discurso, envolvendo no mínimo 3 tabelas.

-- FINALIDADE: mostra todos os grupos do sistema
-- EXEMPLO DE CHAMADA: SELECT * FROM show_groups;
CREATE VIEW show_groups
  AS SELECT grupo.codGrupo as codigo grupo.nome AS grupo, grupo.fk_leitor_email AS criador, tag_grupo.tagg AS tag
      FROM (grupo JOIN posse_tagg ON (grupo.codgrupo = posse_tagg.FK_Grupo_codGrupo))
	    JOIN tag_grupo on(posse_tagg.FK_Tag_Grupo_codTagg = tag_grupo.codtagg);

/* Item2.b) Definir um conjunto de 10 consultas úteis e variadas sobre seu Sistema de Informação,
   sendo que cada uma delas deve envolver no mínimo 3 tabelas. Os requisitos quantitativos são:*/

/* a. No mínimo duas delas devem necessitar serem respondidas com a cláusula group by (isto é,
a resposta deve combinar atributos e totalizações sobre grupos ). Uma delas deve incluir também a cláusula Having. */
--  Consulta de Notas média dos livros de cada autor

-- FINALIDADE: consulta de Notas média dos livros de cada autor
SELECT escrita.fk_leitor_email, livro.titulo, AVG(CAST(classificacao AS INT))
FROM leitor JOIN escrita
ON(leitor.email = escrita.fk_leitor_email)
JOIN leitura
ON(escrita.fk_livro_ISBN = leitura.fk_livro_ISBN)
JOIN livro
ON(escrita.fk_livro_ISBN = ISBN)
GROUP BY escrita.fk_leitor_email, livro.titulo
HAVING COUNT(CAST( classificacao AS INT)) >= 1;

-- FINALIDADE: retorna os 10 escritores mais lidos nos últimos tempos
-- EXEMPLO DE CHAMADA: SELECT * FROM show_most_read;
CREATE VIEW show_most_read AS
SELECT leitor.nome, count(classificacao::INT) AS nmr_leituras
  FROM ((leitor JOIN escrita ON (email=FK_Leitor_email))
    JOIN livro ON(FK_Livro_ISBN=isbn)) JOIN leitura ON(isbn=leitura.FK_Livro_ISBN)
    WHERE leitura.tipo = 'L'
    GROUP BY leitor.nome
    ORDER BY nmr_leituras DESC LIMIT 10;



/* b. No mínimo duas delas devem necessitar serem respondidas com subconsulta (isto é, não existe formulação
    equivalente simplesmente usando joins); */

-- FINALIDADE: saber o livro mais lido de cada autor
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
    GROUP BY le);


-- FINALIDADE: saber qual genero mais lido de um leitor (pode ser mais de 1)
-- Substituir ? por email do leitor procurado
SELECT  leitor.email, genero.nome, COUNT(livro.isbn)
FROM leitor
JOIN leitura ON (leitor.email = leitura.fk_leitor_email)
JOIN livro ON (livro.isbn = leitura.fk_livro_isbn)
JOIN posse_genero ON (livro.isbn = posse_genero.fk_livro_isbn)
JOIN genero ON(genero.codgenero = posse_genero.fk_genero_codgenero)
GROUP BY leitor.email, genero.nome
HAVING (leitor.email, COUNT (leitura.fk_livro_isbn)) IN
(SELECT le, MAX(cntisbn)
    FROM (SELECT leitor.email le, genero.nome gen, COUNT(leitura.fk_livro_isbn) cntisbn
        FROM leitor
        JOIN leitura ON (leitor.email = leitura.fk_leitor_email)
        JOIN livro ON (livro.isbn = leitura.fk_livro_isbn)
        JOIN posse_genero ON (livro.isbn = posse_genero.fk_livro_isbn)
        JOIN genero ON(genero.codgenero = posse_genero.fk_genero_codgenero)
        GROUP BY leitor.email, genero.nome
        HAVING leitor.email = ?)cnt
    GROUP BY le);



/* c. No mínimo uma delas (diferente das consultas acima) deve necessitar do operador NOT EXISTS para
responder questões do tipo TODOS ou NENHUM que <referencia> (isto é, não existe formulaçãoo
equivalente usando simplemente joins ou subconsultas com (NOT) IN ou operadores relacionais) */

-- FINALIDADE: Deleta uma tag que nao esta sendo usada
-- EXEMPLO DE CHAMADA:
DELETE FROM tag_lista
  WHERE NOT EXISTS(SELECT * FROM posse_tagl
  WHERE fk_tag_lista_codtagl = codtagl);



/* d. No mínimos duas delas devem utilizar a visão definida no item anterior. */

-- FINALIDADE: mostra todos os grupos criados pelo usuário
-- EXEMPLO DE CHAMADA: SELECT * FROM show_created_groups(<email usuario>);
CREATE OR REPLACE FUNCTION show_created_groups(
  email varchar
)
RETURNS TABLE(codigo INT, grupo VARCHAR, criador VARCHAR, tag VARCHAR) AS $$
SELECT *
  FROM show_groups allgroups
  WHERE allgroups.criador = email;
$$ LANGUAGE SQL;


-- FINALIDADE: <FUNÇÃO AUXILIAR> mostra os codigos dos grupos em que um determinado usuario participa
CREATE OR REPLACE FUNCTION participate (
  email VARCHAR
)
RETURNS TABLE(codigo VARCHAR) AS $$
  SELECT fk_Grupo_codGrupo
  FROM Mensagem_PARTICIPA
  WHERE fk_Leitor_email = email;
$$ LANGUAGE SQL;


-- FINALIDADE: mostra todos os grupos em que o usuario participa
-- EXEMPLO DE CHAMADA: SELECT * FROM show_my_groups(<email usuario>);
CREATE OR REPLACE FUNCTION show_my_groups(
  email VARCHAR
)
RETURNS TABLE(codigo INT, grupo VARCHAR, tag VARCHAR) AS $$
  SELECT allgroups.codigo, allgroups.grupo, allgroups.tag
  FROM (show_groups allgroups JOIN  participate(email) p ON (allgroups.codigo=p.codigo));
$$ LANGUAGE SQL;
