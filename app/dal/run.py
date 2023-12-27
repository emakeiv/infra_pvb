def do():
      if check_db_exists(credentials):
            
            commands = (
                  """
                  CREATE TABLE exchange (
                        id SERIAL PRIMARY KEY,
                        abbrev TEXT NOT NULL,
                        name TEXT NOT NULL,
                        currency VARCHAR(64) NULL,
                        created_date TIMESTAMP NOT NULL,
                        last_updated_date TIMESTAMP NOT NULL
                  )
                  """,
                  """

                  """
            )