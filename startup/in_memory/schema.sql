CREATE TABLE IF NOT EXISTS BorderStyles (
    border_id INTEGER PRIMARY KEY AUTOINCREMENT,
    border_name TEXT NOT NULL,
    preview_file_name TEXT NOT NULL,
    source_image_file_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Colors (
    color_id INTEGER PRIMARY KEY AUTOINCREMENT,
    color_name TEXT NOT NULL,
    r INTEGER CHECK (r >= 0 AND r <= 255) NOT NULL,
    g INTEGER CHECK (r >= 0 AND r <= 255) NOT NULL,
    b INTEGER CHECK (r >= 0 AND r <= 255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Fonts (
    font_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    font_name  TEXT NOT NULL UNIQUE,
    font_system_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Transforms (
    transform_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    transform_name TEXT NOT NULL CHECK (transform_name IN ('no changes', 'UPPERCASE', 'lowercase', 'Capitalize'))
)