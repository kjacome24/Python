
INSERT INTO users (first_name, last_name, email, create_at, updated_at) VALUES ('Kevin', 'Jacome', 'kduque@coding.la', now(), now());
INSERT INTO users (first_name, last_name, email, create_at, updated_at) VALUES ('Arturo', 'Duque', 'aduque@coding.la', now(), now());
INSERT INTO users (first_name, last_name, email, create_at, updated_at) VALUES ('Emir', 'Duque', 'eduque@coding.la', now(), now());
select * from users;
select * from users where email='kdque@coding.la';
select * from users where id=3;
update users set last_name='Panqueques' where id=3;
delete from users where id=2;
select * from users order by first_name desc;
