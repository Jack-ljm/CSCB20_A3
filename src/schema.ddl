DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS grade;
DROP TABLE IF EXISTS feedback;
DROP TABLE IF EXISTS remark;

CREATE TABLE user(
  username TEXT PRIMARY KEY,
  password TEXT NOT NULL,
  role TEXT CHECK(role == "student" or role == "instructor")
);

CREATE TABLE grade(
  username TEXT REFERENCES user(username) ON DELETE RESTRICT,
  type TEXT NOT NULL,
  date_time TEXT NOT NULL,
  grade INTEGER NOT NULL,
  PRIMARY KEY(username, type, date_time)
);

CREATE TABLE feedback(
  username TEXT NOT NULL REFERENCES user(username) ON DELETE RESTRICT,
  feedback_to TEXT,
  date_time TEXT PRIMARY KEY,
  question_a TEXT,
  question_b TEXT,
  question_c TEXT,
  question_d TEXT
);

CREATE TABLE remark(
  username TEXT NOT NULL REFERENCES user(username) ON DELETE RESTRICT,
  type TEXT NOT NULL,
  date_time TEXT NOT NULL,
  request TEXT NOT NULL,
  status TEXT NOT NULL,
  PRIMARY KEY(username, type, date_time)
);