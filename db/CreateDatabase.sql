USE gaabrieldb;

CREATE TABLE carros (
    id INTEGER NOT NULL auto_increment,
    marca VARCHAR(100),
    modelo VARCHAR(100),
    ano INTEGER,
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;
