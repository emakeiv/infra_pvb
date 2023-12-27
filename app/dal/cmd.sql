CREATE TABLE security_symbol (
      id SERIAL PRIMARY KEY,
      symbol TEXT NOT NULL,
      name TEXT NOT NULL,
      exchange TEXT NOT NULL
);

CREATE TABLE security_price (
      security_id INTEGER NOT NULL,
      dt TIMESTAMP WITHOUT TIME ZONE NOT NULL,
      open NUMERIC NOT NULL,
      high NUMERIC NOT NULL,
      low NUMERIC NOT NULL,
      close NUMERIC NOT NULL,
      volume NUMERIC NOT NULL,
      PRIMARY KEY (security_id, dt),
      CONSTRAINT fk_security FOREIGN KEY (security_id) REFERENCES security_symbol (id)
);

CREATE TABLE etf_holding (

);
