CREATE TABLE source (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE document (
    id SERIAL PRIMARY KEY,
    embedding VECTOR(1536),
    potential_questions VECTOR(1536) NULL,
    source_id INTEGER REFERENCES source(id) ON DELETE CASCADE,
    start_line INTEGER NULL,
    end_line INTEGER NULL,
    content TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);