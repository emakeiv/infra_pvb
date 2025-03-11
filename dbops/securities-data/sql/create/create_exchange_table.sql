CREATE TABLE IF NOT EXISTS exchange (
    id INTEGER           GENERATED ALWAYS AS IDENTITY,
    abbrev VARCHAR(20)   NOT NULL UNIQUE,
    name VARCHAR(255)    NOT NULL,
    currency VARCHAR(10) NOT NULL DEFAULT 'USD',
    timezone VARCHAR(50) NOT NULL DEFAULT 'UTC', 
    created TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    updated TIMESTAMPTZ  NOT NULL DEFAULT NOW(),

    CONSTRAINT exchange_pkey PRIMARY KEY (id)

);

CREATE INDEX idx_exchange_abbrev ON exchange (abbrev);
