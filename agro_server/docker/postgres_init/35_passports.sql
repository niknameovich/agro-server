CREATE TABLE passports (
  id bigint NOT NULL PRIMARY KEY, 
  type_id bigint NOT NULL REFERENCES types (id),
  data json NOT NULL
);
