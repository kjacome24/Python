select * from dojos;
insert into dojos (dojo_name,created_at,updated_at) values ('Cobra kai',now(),now());
insert into dojos (dojo_name,created_at,updated_at) values ('Miyagi dojo',now(),now());
insert into dojos (dojo_name,created_at,updated_at) values ('Miyagi-fang',now(),now());
delete from dojos where id in (1,2,3);
insert into dojos (dojo_name,created_at,updated_at) values ('Cobra kai revolution',now(),now());
insert into dojos (dojo_name,created_at,updated_at) values ('Miyagi dojo origins',now(),now());
insert into dojos (dojo_name,created_at,updated_at) values ('Miyagi-fang evolution',now(),now());
select * from ninjas;
insert into ninjas (first_name,Last_name,age,created_at,updated_at,dojo_id) values ('Tory','Nichols',33,now(),now(),4);
insert into ninjas (first_name,Last_name,age,created_at,updated_at,dojo_id) values ('Terry','Silver',45,now(),now(),4);
insert into ninjas (first_name,Last_name,age,created_at,updated_at,dojo_id) values ('Jhn','Kreese',17,now(),now(),4);
insert into ninjas (first_name,Last_name,age,created_at,updated_at,dojo_id) values ('Kevin','San',33,now(),now(),5);
insert into ninjas (first_name,Last_name,age,created_at,updated_at,dojo_id) values ('Daniel','Larusso',45,now(),now(),5);
insert into ninjas (first_name,Last_name,age,created_at,updated_at,dojo_id) values ('Miguel','Diaz',17,now(),now(),5);
insert into ninjas (first_name,Last_name,age,created_at,updated_at,dojo_id) values ('Eli','Moskowitz',33,now(),now(),6);
insert into ninjas (first_name,Last_name,age,created_at,updated_at,dojo_id) values ('Johnny','Lawrence',45,now(),now(),6);
insert into ninjas (first_name,Last_name,age,created_at,updated_at,dojo_id) values ('Gambito','Torres',17,now(),now(),6);
select concat_ws(' ',ninjas.first_name,ninjas.last_name),dojos.dojo_name from ninjas left join dojos on ninjas.dojo_id=dojos.id where dojos.dojo_name='Cobra kai revolution';
select concat_ws(' ',ninjas.first_name,ninjas.last_name),dojos.dojo_name from ninjas left join dojos on ninjas.dojo_id=dojos.id where dojos.dojo_name='Miyagi dojo origins';
select concat_ws(' ',ninjas.first_name,ninjas.last_name),dojos.dojo_name from ninjas left join dojos on ninjas.dojo_id=dojos.id where dojos.dojo_name='Miyagi-fang evolution';

select dojos.dojo_name from ninjas left join dojos on ninjas.dojo_id=dojos.id order by ninjas.id desc limit 1