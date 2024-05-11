-- Create users table with country enumeration
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,            -- Define primary key
    email VARCHAR(255) NOT NULL UNIQUE,          -- Define unique email column
    name VARCHAR(255),                            -- Define name column
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US' -- Define country enumeration
);
