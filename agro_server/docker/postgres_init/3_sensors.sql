CREATE TABLE sensors (
  id bigint NOT NULL PRIMARY KEY,
  type bigint NOT NULL REFERENCES types (id) ON DELETE CASCADE,
  name varchar(100) NOT NULL CHECK (name <> '') UNIQUE,
  created_at timestamp without time zone NOT NULL CHECK (created_at::date > '2023-01-01'::date),
  passport bigint NOT NULL REFERENCES passports (id)
);
CREATE UNIQUE INDEX idx_unique_sensor_upper_name on sensors (upper(name));
