CREATE TABLE telemetry (
  sensor bigint NOT NULL REFERENCES sensors (id),
  property bigint NOT NULL REFERENCES properties (id),
  value numeric NOT NULL,
  received_at timestamp without time zone NOT NULL,
  CONSTRAINT telemetry_pley PRIMARY KEY (sensor,property,received_at)
);
CREATE INDEX idx_current_telemetry on telemetry (received_at DESC, sensor);
CREATE INDEX idx_specific_telemetry on telemetry (received_at DESC, property);
CREATE INDEX idx_anomaly_telemetry on telemetry (received_at DESC, property, value);
