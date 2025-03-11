CREATE TABLE IF NOT EXISTS data_vendor (
    id            INTEGER GENERATED ALWAYS AS IDENTITY,
    name         VARCHAR(100) UNIQUE NOT NULL,
    website      VARCHAR(255),
    api_endpoint VARCHAR(255) NOT NULL,
    auth_type    VARCHAR(20) NOT NULL,
    api_key      VARCHAR(255),
    supports_tick BOOLEAN DEFAULT FALSE,
    rate_limit    INTEGER DEFAULT NULL,
    active        BOOLEAN DEFAULT TRUE,
    created       TIMESTAMPTZ DEFAULT NOW() NOT NULL,
    updated       TIMESTAMPTZ DEFAULT NOW() NOT NULL,

    CONSTRAINT data_vendor_pkey PRIMARY KEY (id),
    CONSTRAINT data_vendor_auth_type_check CHECK (auth_type IN ('API_KEY', 'OAuth2', 'None'))
);


CREATE INDEX idx_data_vendor_active ON data_vendor (active);
