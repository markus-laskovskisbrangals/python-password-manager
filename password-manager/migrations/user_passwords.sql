CREATE TABLE IF NOT EXISTS user_passwords (
    id NOT NULL, AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    created_at DATE
)