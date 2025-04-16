CREATE TABLE persona (
    id TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    estado_especial INTEGER,
    manzana TEXT,
    estudia INTEGER DEFAULT 0,
    activo INTEGER DEFAULT 0,
    fecha_nacimiento INTEGER,
    FOREIGN KEY (estado_especial) REFERENCES estados_especiales(id)
);

CREATE TABLE pagos_agua (
    id TEXT PRIMARY KEY,
    persona_id TEXT,
    tomas_agua INTEGER CHECK (tomas_agua >= 0),
    año INTEGER CHECK (año >= 2000),
    fecha_pago TEXT,  -- Almacenamos fechas como TEXT en SQLite
    estado_pago TEXT,
    cantidad REAL CHECK (cantidad >= 0),
    tarifa_pendiente REAL CHECK (tarifa_pendiente >= 0),
    FOREIGN KEY (persona_id) REFERENCES persona(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE estados_especiales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);

INSERT INTO estados_especiales (nombre) VALUES
('Ninguno'),
('Madre soltera'),
('Discapacitado'),
('Enfermo');

--Se agregaron 2 registros mas para que la bd acepte mas casos 
INSERT INTO estados_especiales(nombre) VALUES ("usuario especial"), ("comercial/industrial");