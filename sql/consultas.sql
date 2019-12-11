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
 -- 9) Quantas postagens um leitor fez em cada data

 -- OBS: aqui estao ideias que @ArthurCamargo pensou que seriam uteis
--  e que sao relativamente mais complexas, qualquer reclamacao fique a
--  vontade para alterar, modificar e excluir

-- 1)
SELECT escrita.fk_leitor_email, AVG(CAST(classificacao AS INT))
FROM leitor  JOIN escrita 
ON(leitor.email = escrita.fk_leitor_email)
JOIN leitura
ON(escrita.fk_leitor_email = leitura.fk_leitor_email)
GROUP BY escrita.fk_leitor_email, email
HAVING  COUNT(CAST( classificacao AS INT)) >= 1;

-- 2)
--

-- 3)
--
