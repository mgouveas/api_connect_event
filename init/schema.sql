-- Criação da tabela de eventos
CREATE TABLE Eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
);

-- Criação da tabela de participantes
CREATE TABLE Participantes (
    id INTEGER PRIMERY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    link TEXT,
    evento_id INTEGER NOT NULL,
    FOREIGN KEY (evento_id) REFERENCES Eventos(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Criação da tebaa de Eventos_link
CREATE TABLE Eventos_link (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    evento_id INTEGER NOT NULL,
    participante_id INTEGER NOT NULL,
    link Text
    FOREIGN KEY (evento_id) REFERENCES Eventos(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (participante_id) REFERENCES Participantes(id) ON DELETE CASCADE ON UPDATE CASCADE
);