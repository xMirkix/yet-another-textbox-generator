INSERT INTO Colors (color_name, r, g, b, a)
VALUES ('White', 255, 255, 255, 255),
       ('Red', 255, 0, 0, 255),
       ('Orange', 255, 128, 0, 255),
       ('Yellow', 255, 255, 0, 255),
       ('Lime', 128, 255, 0, 255),
       ('Green', 0, 255, 0, 255),
       ('Spring green', 0, 255, 128, 255),
       ('Cyan', 0, 255, 255, 255),
       ('Blue', 0, 128, 255, 255),
       ('Sea blue', 0, 0, 255, 255),
       ('Purple', 128, 0, 255, 255),
       ('Pink', 255, 0, 255, 255),
       ('Hot pink', 255, 0, 128, 255),
       ('Gray', 128, 128, 128, 255),
       ('Black', 0, 0, 0, 255),
       ('Transparent', 0, 0, 0, 0);

INSERT INTO Transforms (transform_name)
VALUES ('no changes'),
       ('UPPERCASE'),
       ('lowercase'),
       ('Capitalize');

INSERT INTO BorderStyles (border_name, preview_file_name, source_image_file_name)
VALUES ('Original Box','undertale_preview', 'Original Box'),
       ('Deltarune','deltarune_preview', 'Deltarune');

INSERT INTO Fonts (font_name, font_system_name)
VALUES ('Determination Mono', 'DeterminationMonoWeb.ttf'),
       ('Comic Sans', 'UndertaleSans.ttf'),
       ('Papyrus', 'UndertalePapyrus.ttf'),
       ('Wingdings', 'wingding');