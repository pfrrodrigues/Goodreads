-- Guarda as informações de usuários(Leitor ou Escritor) do sistema
CREATE TABLE Leitor (
    email VARCHAR(100) PRIMARY KEY,
    nome VARCHAR(50),
    senha VARCHAR(256),
    sexo CHAR(1),
    nascimento DATE,
    Leitor_TIPO INT,
    fk_Pais_codPais SERIAL
);

-- Guarda as informações de livros contidos no catálogo do sistema
CREATE TABLE Livro (
    ISBN CHAR(10) PRIMARY KEY,
    titulo VARCHAR(100),
    descr TEXT,
    nmrPag INTEGER,
    fk_formato_formato_PK serial,
    anoPublic DATE,
    imagem VARCHAR(200)
);

-- Guarda as informações de eventos criados por usuários do sistema
CREATE TABLE Evento (
    codEvento SERIAL,
    hora TIME,
    data DATE,
    descricao TEXT,
    Evento_TIPO INT,
    fk_Leitor_email VARCHAR(100),
    fk_Leitor_email_ VARCHAR(100),
    fk_Endereco_codEnd SERIAL,
    PRIMARY KEY (codEvento)
);

-- Guarda informações de grupos do sistema
CREATE TABLE Grupo (
    codGrupo SERIAL,
    nome VARCHAR(100),
    fk_Leitor_email VARCHAR(100),
    PRIMARY KEY (codGrupo)
);

-- Guarda informações de países contido no catálogo do sistema
CREATE TABLE Pais (
    codPais SERIAL,
    nome VARCHAR(100),
    PRIMARY KEY (codPais)
);

-- Guarda informações de gêneros de livros
CREATE TABLE Genero (
    codGenero SERIAL,
    nome VARCHAR(100),
    PRIMARY KEY(codGenero)
);

-- Guarda informações de tags relacionadas a grupos
CREATE TABLE Tag_Grupo (
    codTagg SERIAL,
    tagg VARCHAR(100),
    PRIMARY KEY(codTagg)
);

-- Guarda informação das listas criadas por usuários no sistema
CREATE TABLE Lista (
    codLista SERIAL,
    nome VARCHAR(100),
    fk_Leitor_email VARCHAR(100),
    PRIMARY KEY(codLista)
);

-- Gaurda informações a lista de tags relacionadas as listas dos usuários
CREATE TABLE Tag_Lista (
    codTagl SERIAL,
    tagl VARCHAR(100),
    PRIMARY KEY(codTagl)
);

-- Guarda a informação de quais usuários participam de quais grupos
CREATE TABLE Mensagem_PARTICIPA (
    fk_Leitor_email VARCHAR(100),
    fk_Grupo_codGrupo serial
);

-- Guarda informações a respeito de um post feito por um usuário
CREATE TABLE Post (
    codPost SERIAL,
    PRIMARY KEY (codPost)
);

-- Guarda informações a respeito de endereços de eventos
CREATE TABLE Endereco (
    cidade VARCHAR(100),
    rua VARCHAR(100),
    bairro VARCHAR(100),
    nmrEstabelecimento INTEGER,
    codEnd SERIAL,
    fk_Pais_codPais serial,
    PRIMARY KEY (codEnd)
);

-- Guarda informações sobre formato de livros
CREATE TABLE formato (
    formato_PK SERIAL,
    formato VARCHAR(20),
    PRIMARY KEY(formato_PK)
);

-- Guarda informações a respeito de amigos de usuários
CREATE TABLE AMIZADE (
    FK_Leitor_email VARCHAR(100),
    FK_Leitor_email_ VARCHAR(100)
);

-- Guarda informações a respeito de quais usuários marcaram determinados livros
CREATE TABLE LEITURA (
    FK_Leitor_email VARCHAR(100),
    FK_Livro_ISBN CHAR(10),
    tipo CHAR(1),
    classificacao CHAR(1)
);

-- Guarda informações a respeito de quais leitores escreveram quais livros
CREATE TABLE ESCRITA (
    FK_Leitor_email VARCHAR(100),
    FK_Livro_ISBN CHAR(10)
);

-- Guarda informações de quais usuários participam de quais eventoss
CREATE TABLE PARTICIPACAO (
    FK_Leitor_email VARCHAR(100),
    FK_Evento_codEvento serial
);

-- Guarda informações a respeito de quais livros possuem quais gêneros
CREATE TABLE POSSE_GENERO (
    FK_Livro_ISBN CHAR(10),
    FK_Genero_codGenero serial
);

-- Guarda informações a respeito de livros que uma lista contém
CREATE TABLE CONTEM (
    FK_Lista_codLista serial,
    FK_Livro_ISBN CHAR(10)
);

-- Guarda informações a respeito de quais grupos possuem determinadas tags
CREATE TABLE POSSE_TAGG (
    FK_Grupo_codGrupo serial,
    FK_Tag_Grupo_codTagg serial
);

-- Guarda informações a respeito de quais listas possuem determinadas tags
CREATE TABLE POSSE_TAGL (
    FK_Lista_codLista serial,
    FK_Tag_Lista_codTagl serial
);

CREATE TABLE POSTAGEM (
    FK_Post_codPost serial
);

ALTER TABLE Leitor ADD CONSTRAINT FK_Leitor_2
FOREIGN KEY (fk_Pais_codPais)
REFERENCES Pais (codPais)
ON DELETE CASCADE;

ALTER TABLE Livro ADD CONSTRAINT FK_Livro_2
FOREIGN KEY (fk_formato_formato_PK)
REFERENCES formato (formato_PK)
ON DELETE CASCADE;

ALTER TABLE Evento ADD CONSTRAINT FK_Evento_3
FOREIGN KEY (fk_Endereco_codEnd)
REFERENCES Endereco (codEnd)
ON DELETE RESTRICT;

ALTER TABLE Grupo ADD CONSTRAINT FK_Grupo_2
FOREIGN KEY (fk_Leitor_email)
REFERENCES Leitor (email)
ON DELETE CASCADE;

ALTER TABLE Lista ADD CONSTRAINT FK_Lista_2
FOREIGN KEY (fk_Leitor_email)
REFERENCES Leitor (email)
ON DELETE CASCADE;

ALTER TABLE Mensagem_PARTICIPA ADD CONSTRAINT FK_Mensagem_PARTICIPA_1
FOREIGN KEY (fk_Leitor_email)
REFERENCES Leitor (email);

ALTER TABLE Mensagem_PARTICIPA ADD CONSTRAINT FK_Mensagem_PARTICIPA_2
FOREIGN KEY (fk_Grupo_codGrupo)
REFERENCES Grupo (codGrupo);

ALTER TABLE Endereco ADD CONSTRAINT FK_Endereco_2
FOREIGN KEY (fk_Pais_codPais)
REFERENCES Pais (codPais)
ON DELETE CASCADE;

ALTER TABLE AMIZADE ADD CONSTRAINT FK_AMIZADE_1
FOREIGN KEY (FK_Leitor_email)
REFERENCES Leitor (email)
ON DELETE CASCADE;

ALTER TABLE AMIZADE ADD CONSTRAINT FK_AMIZADE_2
FOREIGN KEY (FK_Leitor_email_)
REFERENCES Leitor (email)
ON DELETE CASCADE;

ALTER TABLE LEITURA ADD CONSTRAINT FK_LEITURA_1
FOREIGN KEY (FK_Leitor_email)
REFERENCES Leitor (email)
ON DELETE SET NULL;

ALTER TABLE LEITURA ADD CONSTRAINT FK_LEITURA_2
FOREIGN KEY (FK_Livro_ISBN)
REFERENCES Livro (ISBN)
ON DELETE SET NULL;

ALTER TABLE ESCRITA ADD CONSTRAINT FK_ESCRITA_1
FOREIGN KEY (FK_Leitor_email)
REFERENCES Leitor (email)
ON DELETE RESTRICT;

ALTER TABLE ESCRITA ADD CONSTRAINT FK_ESCRITA_2
FOREIGN KEY (FK_Livro_ISBN)
REFERENCES Livro (ISBN)
ON DELETE RESTRICT;

ALTER TABLE PARTICIPACAO ADD CONSTRAINT FK_PARTICIPACAO_1
FOREIGN KEY (FK_Leitor_email)
REFERENCES Leitor (email)
ON DELETE RESTRICT;

ALTER TABLE PARTICIPACAO ADD CONSTRAINT FK_PARTICIPACAO_2
FOREIGN KEY (FK_Evento_codEvento)
REFERENCES Evento (codEvento)
ON DELETE SET NULL;

ALTER TABLE POSSE_GENERO ADD CONSTRAINT FK_POSSE_GENERO_1
FOREIGN KEY (FK_Livro_ISBN)
REFERENCES Livro (ISBN)
ON DELETE RESTRICT;

ALTER TABLE POSSE_GENERO ADD CONSTRAINT FK_POSSE_GENERO_2
FOREIGN KEY (FK_Genero_codGenero)
REFERENCES Genero (codGenero)
ON DELETE SET NULL;

ALTER TABLE CONTEM ADD CONSTRAINT FK_CONTEM_1
FOREIGN KEY (FK_Lista_codLista)
REFERENCES Lista (codLista)
ON DELETE SET NULL;

ALTER TABLE CONTEM ADD CONSTRAINT FK_CONTEM_2
FOREIGN KEY (FK_Livro_ISBN)
REFERENCES Livro (ISBN)
ON DELETE SET NULL;

ALTER TABLE POSSE_TAGG ADD CONSTRAINT FK_POSSE_TAGG_1
FOREIGN KEY (FK_Grupo_codGrupo)
REFERENCES Grupo (codGrupo)
ON DELETE RESTRICT;

ALTER TABLE POSSE_TAGG ADD CONSTRAINT FK_POSSE_TAGG_2
FOREIGN KEY (FK_Tag_Grupo_codTagg)
REFERENCES Tag_Grupo (codTagg)
ON DELETE SET NULL;

ALTER TABLE POSSE_TAGL ADD CONSTRAINT FK_POSSE_TAGL_1
FOREIGN KEY (FK_Lista_codLista)
REFERENCES Lista (codLista)
ON DELETE RESTRICT;

ALTER TABLE POSSE_TAGL ADD CONSTRAINT FK_POSSE_TAGL_2
FOREIGN KEY (FK_Tag_Lista_codTagl)
REFERENCES Tag_Lista (codTagl)
ON DELETE SET NULL;

ALTER TABLE POSTAGEM ADD CONSTRAINT FK_POSTAGEM_1
FOREIGN KEY (FK_Post_codPost)
REFERENCES Post (codPost)
ON DELETE SET NULL;
