INSERT INTO user VALUES
('Jack', 'jackpw', "student"),
('Anna', 'annapw', "instructor"),
('Erwin', 'erwinpw', "instructor"),
('Levi', 'levipw', "student");

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
('Levi', 'Final', datetime('now'), 100)
;

INSERT INTO feedback VALUES
('Levi','Anna', datetime('now'), 'content for qa', 'content for qb', 'content for qc', 'content for qd');

INSERT INTO remark VALUES
('Jack', 'A1', datetime('now'), 'I would like to remark'),
('Katrina', 'A2', datetime('now'), 'I would like to remark'),
('Levi', 'Labs', datetime('now'), 'I think I deserve better mark')
;
