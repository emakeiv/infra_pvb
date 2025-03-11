CREATE TABLE IF NOT EXISTS security_symbol (
    id           INTEGER GENERATED ALWAYS AS IDENTITY,
    exchange_id  INTEGER NOT NULL,
    ticker       VARCHAR(255) NOT NULL,
    instrument   VARCHAR(255) NOT NULL,
    name         VARCHAR(255) NOT NULL,
    sector       VARCHAR(255),
    currency     VARCHAR(64),
    created      TIMESTAMPTZ DEFAULT NOW() NOT NULL,
    updated      TIMESTAMPTZ DEFAULT NOW() NOT NULL,

    CONSTRAINT security_symbol_pkey PRIMARY KEY (id),
    CONSTRAINT security_symbol_exchange_id_fkey FOREIGN KEY (exchange_id) REFERENCES exchange(id) ON DELETE CASCADE
);

CREATE INDEX idx_security_symbol_ticker ON security_symbol (ticker);
