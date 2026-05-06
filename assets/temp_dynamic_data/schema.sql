CREATE TABLE IF NOT EXISTS Universes (
    universe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    universe_name TEXT NOT NULL,
    preview_image TEXT NULL, --base64
    order_position INTEGER CHECK (order_position > 0)
);

CREATE TABLE IF NOT EXISTS Characters (
    character_id INTEGER PRIMARY KEY AUTOINCREMENT,
    character_name TEXT NOT NULL,
    universe_id INTEGER,
    default_style INTEGER,
    default_text_transform INTEGER,
    preview_image TEXT NULL, --base64
    order_position INTEGER CHECK (order_position > 0),
    FOREIGN KEY (universe_id) REFERENCES Universes (universe_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Expressions (
    expression_id INTEGER PRIMARY KEY AUTOINCREMENT,
    expression_name TEXT NOT NULL,
    character_id INTEGER,
    preview_image TEXT NOT NULL, --base64
    order_position INTEGER CHECK (order_position > 0),
    FOREIGN KEY (character_id) REFERENCES Characters (character_id)
        ON DELETE CASCADE
);