CREATE TABLE IF NOT EXISTS security_daily_price (
    security_id    INTEGER NOT NULL,
    data_vendor_id INTEGER NOT NULL REFERENCES data_vendor(id) ON DELETE CASCADE,
    created        TIMESTAMPTZ DEFAULT NOW() NOT NULL,
    updated        TIMESTAMPTZ DEFAULT NOW() NOT NULL,
    datetime       TIMESTAMPTZ NOT NULL,
    open_price     NUMERIC(18,6),
    high_price     NUMERIC(18,6),
    low_price      NUMERIC(18,6),
    close_price    NUMERIC(18,6),
    volume         BIGINT,

    CONSTRAINT security_daily_price_id_pk               PRIMARY KEY (security_id, datetime),
    CONSTRAINT security_daily_price_id_symbol_fkey      FOREIGN KEY (security_id)    REFERENCES security_symbol(id) ON DELETE CASCADE,
    CONSTRAINT security_daily_price_id_data_vendor_fkey FOREIGN KEY (data_vendor_id) REFERENCES data_vendor(id)     ON DELETE SET NULL
);

CREATE INDEX idx_security_daily_price_datetime ON security_daily_price (datetime);
CREATE INDEX idx_security_daily_price_security ON security_daily_price (security_id);

SELECT create_hypertable('security_daily_price', 'datetime', chunk_time_interval => INTERVAL '1 month');
