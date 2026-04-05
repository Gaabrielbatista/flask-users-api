USE gaabrieldb;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL auto_increment,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    idade INTEGER NULL,
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;
