CREATE TABLE persona (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    estado_especial INTEGER,  -- Clave foránea
    manzana TEXT,
    estudia INTEGER DEFAULT 0,
    activo INTEGER DEFAULT 1,
    fecha_nacimiento INTEGER,
    FOREIGN KEY (estado_especial) REFERENCES estados_especiales(id)
)

CREATE TABLE estados_especiales (        
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)


INSERT INTO estados_especiales (nombre) VALUES
('Ninguno'),
('Madre soltera'),
('Discapacitado'),
('Enfermo');

CREATE TABLE pagos_agua (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    persona_id INTEGER,           -- Clave foránea que referencia a persona(id)
    tomas_agua INTEGER,           -- Número de tomas de agua
    año INTEGER,                  -- Año del pago (por ejemplo, 2023)
    fecha_pago TEXT,              -- Fecha del pago (formato YYYY-MM-DD)
    estado_pago TEXT, cantidad REAL, monto_total REAL,             -- Estado del pago (por ejemplo, "Pagado", "Pendiente")
    FOREIGN KEY (persona_id) REFERENCES persona(id)
        ON UPDATE CASCADE         -- Actualización en cascada
        ON DELETE CASCADE         -- Eliminación en cascada
)


CREATE TABLE sqlite_sequence(name,seq)  