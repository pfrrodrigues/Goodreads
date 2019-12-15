-- Instancias de Formato
INSERT INTO formato(formato) VALUES('Livro de Bolso');
INSERT INTO formato(formato) VALUES('Capa Dura');
INSERT INTO formato(formato) VALUES('Capa Comum');
INSERT INTO formato(formato) VALUES('Audio CD');
INSERT INTO formato(formato) VALUES('Ebook');
INSERT INTO formato(formato) VALUES('Audiolivro');
INSERT INTO formato(formato) VALUES('Edição Econômica');


-- Instancias de Pais
INSERT INTO Pais(nome) VALUES ('Afeganistão');
INSERT INTO Pais(nome) VALUES ('África do Sul');
INSERT INTO Pais(nome) VALUES ('Albânia');
INSERT INTO Pais(nome) VALUES ('Alemanha');
INSERT INTO Pais(nome) VALUES ('Angola');
INSERT INTO Pais(nome) VALUES ('Arábia Saudita');
INSERT INTO Pais(nome) VALUES ('Australia');
INSERT INTO Pais(nome) VALUES ('Bélgica');
INSERT INTO Pais(nome) VALUES ('Bolívia');
INSERT INTO Pais(nome) VALUES ('Brasil');
INSERT INTO Pais(nome) VALUES ('Bulgária');
INSERT INTO Pais(nome) VALUES ('Camarões');
INSERT INTO Pais(nome) VALUES ('Canadá');
INSERT INTO Pais(nome) VALUES ('Chile');
INSERT INTO Pais(nome) VALUES ('China');
INSERT INTO Pais(nome) VALUES ('Colômbia');
INSERT INTO Pais(nome) VALUES ('Coreia do Norte');
INSERT INTO Pais(nome) VALUES ('Coreia do Sul');
INSERT INTO Pais(nome) VALUES ('Costa Rica');
INSERT INTO Pais(nome) VALUES ('Cuba');
INSERT INTO Pais(nome) VALUES ('Dinamarca');
INSERT INTO Pais(nome) VALUES ('Equador');
INSERT INTO Pais(nome) VALUES ('Espanha');
INSERT INTO Pais(nome) VALUES ('Estados Unidos');
INSERT INTO Pais(nome) VALUES ('França');
INSERT INTO Pais(nome) VALUES ('Gana');
INSERT INTO Pais(nome) VALUES ('Grecia');
INSERT INTO Pais(nome) VALUES ('Haiti');
INSERT INTO Pais(nome) VALUES ('India');
INSERT INTO Pais(nome) VALUES ('Iraque');
INSERT INTO Pais(nome) VALUES ('Irlanda');
INSERT INTO Pais(nome) VALUES ('Itália');
INSERT INTO Pais(nome) VALUES ('Japão');
INSERT INTO Pais(nome) VALUES ('México');
INSERT INTO Pais(nome) VALUES ('Nigéria');
INSERT INTO Pais(nome) VALUES ('Noruega');
INSERT INTO Pais(nome) VALUES ('Paquistão');
INSERT INTO Pais(nome) VALUES ('Paraguai');
INSERT INTO Pais(nome) VALUES ('Peru');
INSERT INTO Pais(nome) VALUES ('Portugal');
INSERT INTO Pais(nome) VALUES ('Reino Unido');
INSERT INTO Pais(nome) VALUES ('Russia');
INSERT INTO Pais(nome) VALUES ('Senegal');
INSERT INTO Pais(nome) VALUES ('Servia');
INSERT INTO Pais(nome) VALUES ('Suiça');
INSERT INTO Pais(nome) VALUES ('Ucrânia');
INSERT INTO Pais(nome) VALUES ('Uruguai');
INSERT INTO Pais(nome) VALUES ('Venezuela');


-- Instancias de genero
INSERT INTO Genero(nome) VALUES('Fantasia');
INSERT INTO Genero(nome) VALUES('Romance');
INSERT INTO Genero(nome) VALUES('Ficção Científica');
INSERT INTO Genero(nome) VALUES('Thriller Psicológico');
INSERT INTO Genero(nome) VALUES('Classicos');
INSERT INTO Genero(nome) VALUES('Ficção Histórica');
INSERT INTO Genero(nome) VALUES('Terror');
INSERT INTO Genero(nome) VALUES('Mistério');
INSERT INTO Genero(nome) VALUES('Biografia');
INSERT INTO Genero(nome) VALUES('Jornalismo');
INSERT INTO Genero(nome) VALUES('Poesia');
INSERT INTO Genero(nome) VALUES('Autobiografia');
INSERT INTO Genero(nome) VALUES('Humor');
INSERT INTO Genero(nome) VALUES('Ficção Jovem Adulto');
INSERT INTO Genero(nome) VALUES('Dicionário');
INSERT INTO Genero(nome) VALUES('Livro Texto');
INSERT INTO Genero(nome) VALUES('Ciência e Matemática');
INSERT INTO Genero(nome) VALUES('Auto-Ajuda');
INSERT INTO Genero(nome) VALUES('Religião e Espiritualidade');
INSERT INTO Genero(nome) VALUES('Computadores e Tecnologia');


-- Instâncias de Escritores
-- tipo 0: Escritor
-- tipo 1: Leitor
INSERT INTO Leitor VALUES('carlsagan@goodreads.com', 'Carl Sagan', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'M', '2019-12-12', 0,24);
INSERT INTO Leitor VALUES('cixinliu@goodreads.com', 'Cixin Liu', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'M', '1963-06-23', 0,15);
INSERT INTO Leitor VALUES('shawking@goodreads.com', 'Stephen Hawking', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'M', '2019-12-12', 0,41);
INSERT INTO Leitor VALUES('agathachristie@goodreads.com', 'Agatha Christie', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'F', '2019-12-12', 0,41);
INSERT INTO Leitor VALUES('jkrowling@goodreads.com', 'J. K. Rowling', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'F', '1965-07-31', 0,41);
INSERT INTO Leitor VALUES('hlee@goodreads.com', 'Harper Lee', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'F', '2019-12-12', 0,24);
INSERT INTO Leitor VALUES('matwood@goodreads.com', 'Margaret Atwood', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'F', '1939-09-18', 0,13);
INSERT INTO Leitor VALUES('sof@goodreads.com', 'Sófocles', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'M', '2019-12-12', 0,27);
INSERT INTO Leitor VALUES('janea@goodreads.com', 'Jane Austen', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'F', '2019-12-12', 0,41);
INSERT INTO Leitor VALUES('mshelley@goodreads.com', 'Mary Shelley', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'F', '2019-12-12', 0,41);
INSERT INTO Leitor VALUES('steph@goodreads.com', 'Stephenie Meyer', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'F', '1973-12-24', 0,24);
INSERT INTO Leitor VALUES('orwell@goodreads.com', 'George Orwell', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'M', '2019-12-12', 0,41);
INSERT INTO Leitor VALUES('patrickroth@goodreads.com', 'Patrick Rothfuss', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'M', '1973-06-06', 0,24);
INSERT INTO Leitor VALUES('massis@goodreads.com', 'Machado de Assis', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'M', '2019-12-12', 0,10);
INSERT INTO Leitor VALUES('emilybronte@goodreads.com', ' Emily Bronte', '$pbkdf2-sha256$29000$yLn3nvNe6x1jrBUipHSu9Q$9dsFr3c6DT5YWuydlrCE4grgafbe75TJoMzCMrCPjI4',
'F', '2019-12-12', 0,41);
INSERT INTO Leitor VALUES('pfrrodrigues@goodreads.com', 'Pablo Rodrigues', '$pbkdf2-sha256$29000$DkEoBQBA6J3znnMOwRhjDA$9GYhpxye5g2BxvIxW2IsPrL6EzRdSN.hEAb3K4G8LUc',
'M', '1998-06-23', 1, 10);
INSERT INTO Leitor VALUES('avccamargo@goodreads.com', 'Arthur Camargo', '$pbkdf2-sha256$29000$DkEoBQBA6J3znnMOwRhjDA$9GYhpxye5g2BxvIxW2IsPrL6EzRdSN.hEAb3K4G8LUc',
'M', '2019-12-12', 1, 10);
INSERT INTO Leitor VALUES('alice@goodreads.com', 'Alice Sloan', '$pbkdf2-sha256$29000$DkEoBQBA6J3znnMOwRhjDA$9GYhpxye5g2BxvIxW2IsPrL6EzRdSN.hEAb3K4G8LUc',
'F', '2019-12-12', 1, 24);
INSERT INTO Leitor VALUES('rgalante@goodreads.com', 'Renata Galante', '$pbkdf2-sha256$29000$DkEoBQBA6J3znnMOwRhjDA$9GYhpxye5g2BxvIxW2IsPrL6EzRdSN.hEAb3K4G8LUc',
'F', '2019-12-12', 1, 10);
INSERT INTO Leitor VALUES('dongdong@goodreads.com', 'Yang Dong', '$pbkdf2-sha256$29000$DkEoBQBA6J3znnMOwRhjDA$9GYhpxye5g2BxvIxW2IsPrL6EzRdSN.hEAb3K4G8LUc',
'F', '1998-06-23', 1, 15);

-- Instâncias de Livro
INSERT INTO Livro VALUES('8535911944', 'Bilhões e bilhões', 'Último livro escrito por Carl Sagan - e publicado postumamente por Ann Druyan, sua mulher e colaboradora, Bilhões e bilhões traz dezenove artigos dedicados a temas variados. Une-os o fio da racionalidade no exame das coisas do mundo',
288, 3, '2008-03-25', 'https://images-na.ssl-images-amazon.com/images/I/51z7Wgm5vEL._SX342_BO1,204,203,200_.jpg');

INSERT INTO Livro VALUES('8556510205', 'O Problema dos Três Corpos', 'China, final dos anos 1960. Enquanto o país inteiro está sendo devastado pela violência da Revolução Cultural, um pequeno grupo de astrofísicos, militares e engenheiros começa um projeto ultrassecreto envolvendo ondas sonoras e seres extraterrestres.',
320, 3, '2016-09-13', 'https://images-na.ssl-images-amazon.com/images/I/51mVEpYbblL.jpg');

INSERT INTO Livro VALUES('8556510507', 'A Floresta Sombria', 'Depois de "O problema dos três corpos", a humanidade se prepara para a iminente invasão alienígena.',
472, 3, '2017-10-30','https://images-na.ssl-images-amazon.com/images/I/51Fy13z7v1L.jpg');

INSERT INTO Livro VALUES('8580576466', 'Uma Breve História do Tempo','Uma das mentes mais geniais do mundo moderno, Stephen Hawking guia o leitor na busca por respostas a algumas das maiores dúvidas da humanidade: Qual a origem do universo? Ele é infinito?...',
256, 5, '2015-01-22', 'https://images-na.ssl-images-amazon.com/images/I/51aG2%2BoutOL.jpg');

INSERT INTO Livro VALUES('8580415012', 'Os Crimes ABC', 'Há um serial killer à solta, matando suas vítimas em ordem alfabética. A única pista que a polícia tem é um macabro cartão de visitas que o assassino deixa em cada cena do crime...',
150, 5, '2008-11-12', 'https://images-na.ssl-images-amazon.com/images/I/91aLWHmg8QL.jpg');

INSERT INTO Livro VALUES('8532530796','Harry Potter e a Câmara Secreta', 'Depois de férias aborrecidas na casa dos tios trouxas, está na hora de Harry Potter voltar a estudar. Coisas acontecem, no entanto, para dificultar o regresso de Harry...',
224, 2, '2017-08-19', 'https://images-na.ssl-images-amazon.com/images/I/71NsVQ5MlwL.jpg');

INSERT INTO Livro VALUES('8532530842','Harry Potter e as relíquias da morte', 'Harry Potter e as relíquias da morte, de J.K. Rowling, é o sétimo e último livro da série. Voldemorte está cada vez mais forte e Harry Potter precisa encontrar e aniquilar as Horcruxes para enfraquecer o lorde e poder enfrentálo.',
512, 2, '2017-08-19', 'https://d1pkzhm5uq4mnt.cloudfront.net/imagens/capas/_f9b329bdfe71cb03efa4f0a2a6ebfee60dbe8d03.jpg');

INSERT INTO Livro VALUES('8532520669', 'O Conto da Aia', 'O romance distópico O conto da aia, de Margaret Atwood, se passa num futuro muito próximo e tem como cenário uma república onde não existem mais jornais, revistas, livros nem filmes...',
368, 3, '2017-06-07', 'https://images-na.ssl-images-amazon.com/images/I/91AHNAr638L.jpg');

INSERT INTO Livro VALUES('8503009498', 'O Sol é para Todos', 'Um livro emblemático sobre racismo e injustiça e um dos maiores clássicos da literatura mundial.Um livro emblemático sobre racismo e injustiça: a história de um advogado...',
350, 3, '2006-10-10', 'https://images-na.ssl-images-amazon.com/images/I/51SDFG0BD8L._SR600,315_SCLZZZZZZZ_.jpg');

INSERT INTO Livro VALUES('8537817368', 'Édipo Rei', 'Insultado por um homem embriagado que o chamou de filho adotivo, Édipo, herdeiro do trono de Corinto, se dirige a Delfos em busca de respostas sobre sua origem.',
128, 5, '2018-04-12', 'https://images-na.ssl-images-amazon.com/images/I/51lTtg2%2Bv6L._SX298_BO1,204,203,200_.jpg');

INSERT INTO Livro VALUES('8578553071', 'Orgulho e Preconceito', 'Em “Orgulho e Preconceito”, Elizabeth Bennet, segunda de 5 filhas de um proprietário rural na cidade fictícia de Meryton, lida com os problemas relacionados à educação, cultura, moral e casamento na sociedade aristocrática do início do século XIX',
399, 2, '2017-04-11', 'https://www.casasbahia-imagens.com.br/livros/LivrodeLiteraturaEstrangeira/Romance/174186/5899044/Orgulho-e-Preconceito-Jane-Austen-174186.jpg');

INSERT INTO Livro VALUES('8594540183', 'Frankenstein', 'A criatura de Frankenstein é considerada o primeiro mito dos tempos modernos.Para compor sua bem-sucedida experiência literária, Shelley costurou influências diversas, que vão do livro do Gênesis a Paraíso Perdido, da Grécia Antiga ao Iluminismo. ',
304, 7, '2017-02-06', 'https://http2.mlstatic.com/livro-frankenstein-darkside-capa-dura-lacrado-D_NQ_NP_716364-MLB31683742516_082019-F.jpg');

INSERT INTO Livro VALUES('8598078301', 'Crepúsculo', 'Crepúsculo poderia ser uma história comum, não fosse um elemento irresistível: o objeto da paixão da protagonista é um vampiro. Assim, soma-se à paixão um perigo sobrenatural temperado com muito suspense, e o resultado é uma leitura de tirar o fôlego...',
480, 3, '2008-12-12', 'http://statics.livrariacultura.net.br/products/capas_lg/195/11018195.jpg');

INSERT INTO Livro VALUES('8535914846', '1984', 'Winston, herói de 1984, último romance de George Orwell, vive aprisionado na engrenagem totalitária de uma sociedade completamente dominada pelo Estado, onde tudo é feito coletivamente, mas cada qual vive sozinho...',
416, 3, '2009-12-17', 'https://images-na.ssl-images-amazon.com/images/I/41E9Z5XaHcL.jpg');

INSERT INTO Livro VALUES('853781752X', 'O Morro dos Ventos Uivantes', 'No centro dos acontecimentos dessa história de obsessão e dor, perversidade e vingança, estão a obstinada figura de Catherine Earnshaw e o rude e enérgico Heathcliff...',
480, 7, '2018-10-10', 'https://images-na.ssl-images-amazon.com/images/I/51UdKJDe2TL.jpg');

INSERT INTO Livro VALUES('8599296493', 'O Nome do Vento', ' Da infância numa trupe de artistas itinerantes, passando pelos anos vividos numa cidade hostil e pelo esforço para ingressar na escola de magia, O nome do vento acompanha a trajetória de Kote...',
656, 3, '2009-12-13', 'https://lojasaraiva.vteximg.com.br/arquivos/ids/9194257-287-426/1006695900.jpg?v=637103721392230000');

INSERT INTO Livro VALUES('6580210087', 'O Alienista', 'Com quantos doidos se faz uma cidadezinha? É o que está prestes a investigar o ilustre Dr. Simão Bacamarte, renomado médico com estudos no exterior, que funda na vila de Itaguaí a Casa Verde, instituto onde pretende estudar e tratar todos...',
304, 2, '2019-10-01', 'https://images-na.ssl-images-amazon.com/images/I/41v3HwWeX4L._SX322_BO1,204,203,200_.jpg');

INSERT INTO Livro VALUES('0000000000', 'Teste', '',
304, 2, '2019-12-01', 'https://images-na.ssl-images-amazon.com/images/I/41v3HwWeX4L._SX322_BO1,204,203,200_.jpg');


-- Instâncias de Escrita
INSERT INTO ESCRITA VALUES('carlsagan@goodreads.com', '8535911944');
INSERT INTO ESCRITA VALUES('carlsagan@goodreads.com', '0000000000');
INSERT INTO ESCRITA VALUES('cixinliu@goodreads.com', '8556510205');
INSERT INTO ESCRITA VALUES('cixinliu@goodreads.com', '8556510507');
INSERT INTO ESCRITA VALUES('shawking@goodreads.com', '8580576466');
INSERT INTO ESCRITA VALUES('agathachristie@goodreads.com', '8580415012');
INSERT INTO ESCRITA VALUES('jkrowling@goodreads.com', '8532530796');
INSERT INTO ESCRITA VALUES('jkrowling@goodreads.com', '8532530842');
INSERT INTO ESCRITA VALUES('hlee@goodreads.com', '8503009498');
INSERT INTO ESCRITA VALUES('matwood@goodreads.com', '8532520669');
INSERT INTO ESCRITA VALUES('sof@goodreads.com', '8537817368');
INSERT INTO ESCRITA VALUES('janea@goodreads.com', '8578553071');
INSERT INTO ESCRITA VALUES('mshelley@goodreads.com', '8594540183');
INSERT INTO ESCRITA VALUES('steph@goodreads.com', '8598078301');
INSERT INTO ESCRITA VALUES('orwell@goodreads.com', '8535914846');
INSERT INTO ESCRITA VALUES('patrickroth@goodreads.com', '8599296493');
INSERT INTO ESCRITA VALUES('massis@goodreads.com', '6580210087');
INSERT INTO ESCRITA VALUES('emilybronte@goodreads.com', '853781752X');

--  Instancias de POSSE_GENERO
INSERT INTO POSSE_GENERO VALUES('8535911944',17);
INSERT INTO POSSE_GENERO VALUES('8556510205',3);
INSERT INTO POSSE_GENERO VALUES('8556510205',3);
INSERT INTO POSSE_GENERO VALUES('8580576466',17);
INSERT INTO POSSE_GENERO VALUES('8580415012',5);
INSERT INTO POSSE_GENERO VALUES('8580415012',8);
INSERT INTO POSSE_GENERO VALUES('8532530796',1);
INSERT INTO POSSE_GENERO VALUES('8532530796',14);
INSERT INTO POSSE_GENERO VALUES('8532530842',1);
INSERT INTO POSSE_GENERO VALUES('8532530842',14);
INSERT INTO POSSE_GENERO VALUES('8503009498',2);
INSERT INTO POSSE_GENERO VALUES('8503009498',6);
INSERT INTO POSSE_GENERO VALUES('8532520669',6);
INSERT INTO POSSE_GENERO VALUES('8532520669',2);
INSERT INTO POSSE_GENERO VALUES('8537817368',5);
INSERT INTO POSSE_GENERO VALUES('8578553071',2);
INSERT INTO POSSE_GENERO VALUES('8578553071',5);
INSERT INTO POSSE_GENERO VALUES('8594540183',7);
INSERT INTO POSSE_GENERO VALUES('8594540183',4);
INSERT INTO POSSE_GENERO VALUES('8594540183',3);
INSERT INTO POSSE_GENERO VALUES('8598078301',2);
INSERT INTO POSSE_GENERO VALUES('8535914846',5);
INSERT INTO POSSE_GENERO VALUES('8535914846',3);
INSERT INTO POSSE_GENERO VALUES('8599296493',1);
INSERT INTO POSSE_GENERO VALUES('6580210087',5);
INSERT INTO POSSE_GENERO VALUES('853781752X',5);
INSERT INTO POSSE_GENERO VALUES('853781752X',2);


-- Instancias de LEITURA
-- TIPO: LIDO(L)
INSERT INTO LEITURA VALUES ('pfrrodrigues@goodreads.com', '8594540183', 'L', '5');
INSERT INTO LEITURA VALUES ('avccamargo@goodreads.com', '8594540183', 'L', '3');
INSERT INTO LEITURA VALUES ('pfrrodrigues@goodreads.com', '8532530842', 'L', '4');

-- TIPO: DESEJO LER(D)
INSERT INTO LEITURA(fk_Leitor_email, FK_Livro_ISBN, tipo) VALUES('pfrrodrigues@goodreads.com', '8535911944', 'D');
INSERT INTO LEITURA(fk_Leitor_email, FK_Livro_ISBN, tipo) VALUES ('pfrrodrigues@goodreads.com', '8556510205', 'D');
INSERT INTO LEITURA(fk_Leitor_email, FK_Livro_ISBN, tipo) VALUES('avccamargo@goodreads.com', '8556510205', 'D');
INSERT INTO LEITURA(fk_Leitor_email, FK_Livro_ISBN, tipo) VALUES('avccamargo@goodreads.com', '8535911944', 'D');

-- TIPO: ATUALMENTE LENDO(A)
INSERT INTO LEITURA(fk_Leitor_email, FK_Livro_ISBN, tipo) VALUES('avccamargo@goodreads.com', '8580576466', 'A');
INSERT INTO LEITURA(fk_Leitor_email, FK_Livro_ISBN, tipo) VALUES('pfrrodrigues@goodreads.com', '8580576466', 'A');
