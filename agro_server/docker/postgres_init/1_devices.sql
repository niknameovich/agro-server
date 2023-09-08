CREATE TABLE devices (
  id bigint,
  name varchar(100) NOT NULL,
  created_at timestamp without time zone NOT NULL,
  disconnected_at timestamp without time zone NULL,
  is_active bool not null, 
  area bigint  NOT NULL,
  parent bigint NULL,
  CONSTRAINT devices_pkey PRIMARY KEY (id),
  CONSTRAINT devices_main_cond CHECK (upper(name) <> '' AND created_at::date > '2023-01-01'::date)
);
CREATE INDEX idx_device_created_at_active on devices (is_active, created_at DESC,area);
CREATE INDEX idx_device_hierarchy on devices (parent, is_active);
CREATE UNIQUE INDEX idx_device_upper_name on devices (upper(name));
