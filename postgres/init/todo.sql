DROP DATABASE IF EXISTS todo;
CREATE DATABASE todo;
\c todo;

DROP TABLE IF EXISTS todos;
CREATE TABLE todos (
  id VARCHAR(8) NOT NULL,
  task_name VARCHAR(64) NOT NULL,
  description TEXT,
  create_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ON todos (id);
