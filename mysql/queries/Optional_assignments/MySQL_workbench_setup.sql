use lead_gen_business;

select * from billing;
INSERT INTO billing (id, amount, charged_datetime, clients_id) VALUES ('27', '500', '2023-10-04 09:38:00', '1');
UPDATE billing SET amount = '1000' WHERE (id = '26');
DELETE FROM billing WHERE (id = '27'); 