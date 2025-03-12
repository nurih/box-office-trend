CREATE TABLE
  movie (
    title VARCHAR(255) NOT NULL CONSTRAINT pk_movie PRIMARY KEY
  );

CREATE TABLE
  theater (
    name VARCHAR(255) NOT NULL CONSTRAINT pk_theater PRIMARY KEY
  );

CREATE TABLE
  sale (
    theater VARCHAR(255) NOT NULL,
    movie VARCHAR(266) NOT NULL,
    day DATE NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    CONSTRAINT pk_sale PRIMARY KEY (movie, theater, day),
    CONSTRAINT fk_theater FOREIGN KEY (theater) REFERENCES theater (name),
    CONSTRAINT fk_movie FOREIGN KEY (movie) REFERENCES movie (title)
  );

INSERT INTO
  movie (title)
VALUES
  ('Shrek'),
  ('Alien'),
  ('Up');

INSERT INTO
  theater (name)
VALUES
  ('Laemle 1'),
  ('Laemle 2'),
  ('Arclight 1');

INSERT INTO
  sale (theater, movie, day, amount)
VALUES
  ('Laemle 1', 'Up', '2025-01-01', 111.00),
  ('Laemle 1', 'Up', '2025-01-02', 112.00),
  ('Laemle 2', 'Shrek', '2025-01-01', 221.00),
  ('Laemle 2', 'Shrek', '2025-01-02', 222.00),
  ('Laemle 2', 'Shrek', '2025-01-03', 223.00),
  ('Arclight 1', 'Alien', '2025-01-01', 331.00),
  ('Laemle 1', 'Alien', '2025-01-02', 332.00);