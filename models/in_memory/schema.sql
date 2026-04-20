CREATE TABLE IF NOT EXISTS BorderStyles (
    border_id INTEGER PRIMARY KEY AUTOINCREMENT,
    border_name TEXT,
    image TEXT --base64
);

CREATE TABLE IF NOT EXISTS Colors (
    color_id INTEGER PRIMARY KEY AUTOINCREMENT,
    color_name TEXT,
    r INTEGER CHECK (r >= 0 AND r <= 255),
    g INTEGER CHECK (r >= 0 AND r <= 255),
    b INTEGER CHECK (r >= 0 AND r <= 255)
);

CREATE TABLE IF NOT EXISTS Fonts (
    font_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    font_name  TEXT,
    font_value TEXT --base64
);

CREATE TABLE IF NOT EXISTS Transforms (
    transform_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    transform_name TEXT CHECK (transform_name IN ('no changes', 'UPPERCASE', 'lowercase', 'Capitalize'))
)