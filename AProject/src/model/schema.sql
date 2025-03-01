-- schema.sql

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS translations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    translation TEXT NOT NULL,
    translation_user INTEGER NOT NULL,  -- Define the column first
    FOREIGN KEY (translation_user) REFERENCES users(id) ON DELETE CASCADE  -- Correct reference to users table
);
