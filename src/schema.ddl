DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS instructor;
DROP TABLE IF EXISTS grade;
DROP TABLE IF EXISTS feedback;
DROP TABLE IF EXISTS remark;

CREATE TABLE student(
  username TEXT PRIMARY KEY,
  password TEXT NOT NULL
);

CREATE TABLE instructor(
  username TEXT PRIMARY KEY,
  password TEXT NOT NULL
);

CREATE TABLE grade(
  username TEXT REFERENCES student(username) ON DELETE RESTRICT,
  type TEXT NOT NULL,
  date_time TEXT NOT NULL,
  grade INTEGER NOT NULL,
  PRIMARY KEY(username, type, date_time)
);

CREATE TABLE feedback(
  username TEXT NOT NULL REFERENCES instructor(username) ON DELETE RESTRICT,
  date_time TEXT PRIMARY KEY,
  question_a TEXT,
  question_b TEXT,
  question_c TEXT,
  question_d TEXT
);

CREATE TABLE remark(
  username TEXT NOT NULL REFERENCES student(username) ON DELETE RESTRICT,
  type TEXT NOT NULL,
  date_time TEXT NOT NULL,
  request TEXT NOT NULL,
  PRIMARY KEY(username, type, date_time)
);