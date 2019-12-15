/* Item2.c) Definir um procedimento armazenado (stored procedure) que deve ser disparado por um gatilho ao
atualizar uma tabela (e.g. inserção, atualização ou remoção de tuplas). Você deve pesquisar a linguagem do SGBD
escolhido para definir este procedimento, e programar este procedimento nesta linguagem. Será considerada a
utilidade do procedimento proposto. Procedimentos triviais não serão valorizados. */

/* FINALIDADE: seta a classificacao para NULL quando o estado de marcacao
   for alterado de LIDO(L) para ATUALMENTE LENDO(A) OU DESEJO LER(D), pois
   não é permitido a um usuário dar uma classificacao para um livro que não leu */
-- TRIGGER FUNCTION
CREATE OR REPLACE FUNCTION set_classification()
RETURNS trigger AS $$
BEGIN
  IF OLD.tipo = 'L' THEN
     UPDATE leitura SET classificacao = NULL
     WHERE tipo = 'A' OR tipo = 'D';
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- TRIGGER
CREATE TRIGGER change_classification
  AFTER UPDATE
  ON leitura
  FOR EACH ROW
  EXECUTE PROCEDURE set_classification();
