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
('Jack', 'A1', datetime('now'), 90),
('Jack', 'A2', datetime('now'), 88),
('Katrina', 'A1', datetime('now'), 60),
('Jack', 'TT1', datetime('now'), 70),
('Katrina', 'A2', datetime('now'), 90),

('Levi', 'TT1', datetime('now'), 100),
('Levi', 'A1', datetime('now'), 95),
('Levi', 'A2', datetime('now'), 90),
('Levi', 'A3', datetime('now'), 87),
('Levi', 'Labs', datetime('now'), 85),
('Levi', 'Final', datetime('now'), 100),

('student1', 'TT1', datetime('now'), 67),
('student1', 'TT2', datetime('now'), 90),
('student1', 'A1', datetime('now'), 80),
('student1', 'A2', datetime('now'), 90),
('student1', 'A3', datetime('now'), 20),
('student1', 'Labs', datetime('now'), 50),
('student1', 'Final', datetime('now'), 88),

('student2', 'TT2', datetime('now'), 50),
('student2', 'A1', datetime('now'), 30),
('student2', 'A2', datetime('now'), 20),
('student2', 'TT1', datetime('now'), 67),
('student2', 'Labs', datetime('now'), 85),
('student2', 'Final', datetime('now'), 87)
;

INSERT INTO feedback VALUES
('Anna', datetime('now'), 'content for qa', 'content for qb', 'content for qc', 'content for qd');

INSERT INTO remark VALUES
('Jack', 'A1', datetime('now'), 'I would like to remark', 'Not yet started'),
('Katrina', 'A2', datetime('now'), 'I would like to remark', 'In progress'),

('Levi', 'Labs', datetime('now'), 'I think I deserve better mark', 'Addressed'),
('Levi', 'Midterm', datetime('now'), 'Because I can', 'Not yet started'),
('Levi', 'A1', datetime('now'), 'I want remark', 'In progress')
;
