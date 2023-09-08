CREATE TABLE device_sensors_rel (
id bigint not null PRIMARY KEY, 
device bigint not null REFERENCES devices (id),
sensor bigint not null REFERENCES sensors (id),
created_at timestamp without time zone NOT NULL,
deleted_at timestamp without time zone NULL
);
