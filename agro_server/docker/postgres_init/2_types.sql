CREATE TABLE types (
  id bigint NOT NULL PRIMARY KEY,
  name varchar(100) NOT NULL CHECK (name <>''),
  created_at timestamp without time zone NOT NULL,
  description text NULL);
CREATE UNIQUE INDEX idx_types_unique_upper_name on types (upper(name));
