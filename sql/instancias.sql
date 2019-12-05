INSERT INTO pais(nome)
VALUES ('Brazil'), ('United States'), ('England');

SELECT * FROM pais;

INSERT INTO leitor(email, nome, senha, sexo, nascimento, Leitor_TIPO, fk_Pais_codPais)
VALUES 
('pfrodrigues@inf.ufrgs.br', 'Pablo Rodrigues', '123456NuncaVaoAdivinhar', 'M', '1998-06-05', 0, 'e4de6545-4d2c-4bbf-a30e-4c2e2958dd97'),
('avccamargo@inf.ufrgs.br', 'Arthur Camargo', '123456', 'M', '1998-02-24', 0, 'e4de6545-4d2c-4bbf-a30e-4c2e2958dd97');  

INSERT INTO livro(isbn, titulo, descr, nmrPag, anoPublic, imagem)
VALUES('0545010225', 'harry potter', 'harry potter duh...', 120, '1998-02-01', '/usr/Imagens/HarryPotter/harry.png');


-- CREATE TABLE Livro (
--     ISBN CHAR(10) PRIMARY KEY,
--     titulo VARCHAR(100),
--     descr TEXT,
--     nmrPag INTEGER,
--     fk_formato_formato_PK UUID,
--     anoPublic DATE,
--     imagem VARCHAR(100)
-- );

-- CREATE TABLE Evento (
--     codEvento UUID DEFAULT uuid_generate_v4 (),
--     hora TIME,
--     data DATE,
--     descricao TEXT,
--     Evento_TIPO INT,
--     fk_Leitor_email VARCHAR(100),
--     fk_Leitor_email_ VARCHAR(100),
--     fk_Endereco_codEnd UUID,
-- 	PRIMARY KEY (codEvento)
-- );

-- CREATE TABLE Grupo (
--     codGrupo UUID DEFAULT uuid_generate_v4 (),
--     nome VARCHAR(100),
--     fk_Leitor_email VARCHAR(100),
-- 	PRIMARY KEY (codGrupo)
-- );

-- CREATE TABLE Pais (
--     codPais UUID DEFAULT uuid_generate_v4 (),
--     nome VARCHAR(100),
-- 	PRIMARY KEY (codPais)
-- );

-- CREATE TABLE Genero (
--     codGenero UUID DEFAULT uuid_generate_v4 (),
--     nome VARCHAR(100),
-- 	PRIMARY KEY(codGenero)
-- );

-- CREATE TABLE Tag_Grupo (
--     codTagg UUID DEFAULT uuid_generate_v4 (),
--     tagg VARCHAR(100),
-- 	PRIMARY KEY(codTagg)
-- );

-- CREATE TABLE Lista (
--     codLista UUID DEFAULT uuid_generate_v4 (),
--     nome VARCHAR(100),
--     fk_Leitor_email VARCHAR(100),
-- 	PRIMARY KEY(codLista)
-- );

-- CREATE TABLE Tag_Lista (
--     codTagl UUID DEFAULT uuid_generate_v4 (),
--     tagl VARCHAR(100),
-- 	PRIMARY KEY(codTagl)
-- );

-- CREATE TABLE Mensagem_PARTICIPA (
--     fk_Leitor_email VARCHAR(100),
--     fk_Grupo_codGrupo UUID
-- );

-- CREATE TABLE Post (
--     codPost UUID DEFAULT uuid_generate_v4 (),
-- 	PRIMARY KEY (codPost)
-- );

-- CREATE TABLE Endereco (
--     cidade VARCHAR(100),
--     rua VARCHAR(100),
--     bairro VARCHAR(100),
--     nmrEstabelecimento INTEGER,
--     codEnd UUID DEFAULT uuid_generate_v4 (),
--     fk_Pais_codPais UUID,
-- 	PRIMARY KEY (codEnd)
-- );

-- CREATE TABLE formato (
--     formato_PK UUID DEFAULT uuid_generate_v4 (),
--     formato VARCHAR(20),
-- 	PRIMARY KEY(formato_PK)
-- );

-- CREATE TABLE AMIZADE (
--     FK_Leitor_email VARCHAR(100),
--     FK_Leitor_email_ VARCHAR(100)
-- );

-- CREATE TABLE LEITURA (
--     FK_Leitor_email VARCHAR(100),
--     FK_Livro_ISBN CHAR(10),
--     tipo CHAR(1),
--     classificacao CHAR(1)
-- );

-- CREATE TABLE ESCRITA (
--     FK_Leitor_email VARCHAR(100),
--     FK_Livro_ISBN CHAR(10)
-- );

-- CREATE TABLE PARTICIPACAO (
--     FK_Leitor_email VARCHAR(100),
--     FK_Evento_codEvento UUID
-- );

-- CREATE TABLE POSSE_GENERO (
--     FK_Livro_ISBN CHAR(10),
--     FK_Genero_codGenero UUID
-- );

-- CREATE TABLE CONTEM (
--     FK_Lista_codLista UUID,
--     FK_Livro_ISBN CHAR(10)
-- );

-- CREATE TABLE POSSE_TAGG (
--     FK_Grupo_codGrupo UUID,
--     FK_Tag_Grupo_codTagg UUID
-- );

-- CREATE TABLE POSSE_TAGL (
--     FK_Lista_codLista UUID,
--     FK_Tag_Lista_codTagl UUID
-- );

-- CREATE TABLE POSTAGEM (
--     FK_Post_codPost UUID
-- );

