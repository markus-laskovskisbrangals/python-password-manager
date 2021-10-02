CREATE TABLE IF NOT EXISTS user_passwords (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    created_at varchar(30) NOT NULL,
    PRIMARY KEY(id)
)