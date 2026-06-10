INSERT INTO Colors (color_name, r, g, b)
VALUES ('White', 255, 255, 255),
       ('Red', 255, 0, 0),
       ('Orange', 255, 128, 0),
       ('Yellow', 255, 255, 0),
       ('Lime', 128, 255, 0),
       ('Green', 0, 255, 0),
       ('Spring green', 0, 255, 128),
       ('Cyan', 0, 255, 255),
       ('Blue', 0, 128, 255),
       ('Sea blue', 0, 0, 255),
       ('Purple', 128, 0, 255),
       ('Pink', 255, 0, 255),
       ('Hot pink', 255, 0, 128),
       ('Gray', 128, 128, 128),
       ('Black', 0, 0, 0);

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