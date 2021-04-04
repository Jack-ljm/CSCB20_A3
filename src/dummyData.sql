INSERT INTO user VALUES
('Jack', 'jackpw', "student"),
('Anna', 'annapw', "instructor");

INSERT INTO grade VALUES
('Jack', 'A1', datetime('now'), 90),
('Jack', 'A2', datetime('now'), 88),
('Katrina', 'A1', datetime('now'), 60),
('Jack', 'TT1', datetime('now'), 70),
('Katrina', 'A2', datetime('now'), 90);

INSERT INTO feedback VALUES
('Anna', datetime('now'), 'content for qa', 'content for qb', 'content for qc', 'content for qd');

INSERT INTO remark VALUES
('Jack', 'A1', datetime('now'), 'I would like to remark'),
('Katrina', 'A2', datetime('now'), 'I would like to remark');
