CREATE TABLE properties (
  id  bigint NOT NULL PRIMARY KEY,
  type bigint NOT NULL REFERENCES types (id),
  name varchar(100) NOT NULL CHECK (name <> '') DEFAULT upper(substr(md5(random()::text), 0, 25)),
  display_as varchar(500) NOT NULL DEFAULT 'NOT SET',
  created_at timestamp without time zone NOT NULL,
  terminated_at timestamp without time zone NULL
);
CREATE UNIQUE INDEX idx_unique_property_name on properties (upper(name));
CREATE INDEX idx_properties_spec_by_type on properties (type, created_at DESC) where terminated_at is null;
