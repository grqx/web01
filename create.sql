CREATE TABLE Makers (
    maker_id INTEGER UNIQUE NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY(maker_id AUTOINCREMENT)
);

CREATE TABLE Bikes (
    bike_id INTEGER UNIQUE NOT NULL,
    maker_id INTEGER NOT NULL,
    model TEXT NOT NULL,
    top_speed INTEGER NOT NULL,  /* MPH */
    cost INTEGER NOT NULL,  /* USD */
    description TEXT,
    PRIMARY KEY(bike_id AUTOINCREMENT),
    FOREIGN KEY(maker_id) REFERENCES Makers(maker_id)
);

.read insert.sql
