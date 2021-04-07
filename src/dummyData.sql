INSERT INTO user VALUES
('Jack', 'jackpw', "student"),
('Anna', 'annapw', "instructor"),
('Erwin', 'erwinpw', "instructor"),
('Levi', 'levipw', "student"),
('student1', 'student1', "student"),
('student2', 'student2', "student"),
('instructor1', 'instructor1', "instructor"),
('instructor2', 'instructor2', "instructor")
;

INSERT INTO grade VALUES
('Jack', 'A1', "2021-04-06 11:34:56", 90),
('Jack', 'A2', "2021-04-06 11:24:56", 88),
('Katrina', 'A1', "2021-04-06 11:04:56", 60),
('Jack', 'TT1', "2021-04-06 06:24:56", 70),
('Katrina', 'A2', "2021-04-06 12:18:56", 90),
('Levi', 'TT1', "2021-04-06 11:34:56", 100),
('Levi', 'A1', "2021-03-06 11:34:56", 95),
('Levi', 'A2', "2021-03-06 11:14:56", 90),
('Levi', 'A3', "2021-04-06 11:34:56", 87),
('Levi', 'Labs', "2021-02-06 11:04:56", 85),
('Levi', 'Final', "2021-04-07 11:34:56", 100),
('student1', 'TT1', "2021-04-06 11:34:56", 100),
('student1', 'A1', "2021-03-06 11:34:56", 95),
('student1', 'A2', "2021-03-06 11:14:56", 90),
('student1', 'A3', "2021-04-06 11:34:56", 87),
('student1', 'Labs', "2021-02-06 11:04:56", 85),
('student1', 'Final', "2021-04-07 11:34:56", 100)
;

INSERT INTO feedback VALUES
('Anna', "2021-04-07 11:34:56", 'content for qa', 'content for qb', 'content for qc', 'content for qd');

INSERT INTO remark VALUES
('Jack', 'A1', datetime('now'), 'I would like to remark', 'Not yet started'),
('Katrina', 'A2', datetime('now'), 'I would like to remark', 'In progress'),

('Levi', 'Labs', datetime('now'), 'I think I deserve better mark', 'Addressed'),
('Levi', 'Midterm', datetime('now'), 'Because I can', 'Not yet started'),
('Levi', 'A1', datetime('now'), 'I want remark', 'In progress'),
('student1', 'Labs', datetime('now'), 'I think I deserve better mark', 'Addressed'),
('student1', 'Midterm', datetime('now'), 'Because I can', 'Not yet started'),
('student1', 'A1', datetime('now'), 'I want remark', 'In progress')
;
