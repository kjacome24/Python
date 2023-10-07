SET SQL_SAFE_UPDATES = 0;

select * from books;
select * from favorites;
select * from users;
#########################

insert into users (name,created_at,updated_at) value ('Jane Austen',now(),now());
insert into users (name,created_at,updated_at) value ('Emily Dickinson',now(),now());
insert into users (name,created_at,updated_at) value ('Fyodor Dostoevsky',now(),now());
insert into users (name,created_at,updated_at) value ('William Shakespeare',now(),now());
insert into users (name,created_at,updated_at) value ('Lau Tzu',now(),now());
###################
insert into books (title,author,num_pages,updated_at,created_at) value ('C Sharp','Kevin Sharp',150,now(),now());
insert into books (title,author,num_pages,updated_at,created_at) value ('Java','Arturo Java',220,now(),now());
insert into books (title,author,num_pages,updated_at,created_at) value ('Python','Prince Python',250,now(),now());
insert into books (title,author,num_pages,updated_at,created_at) value ('PHP','Altamar Php',100,now(),now());
insert into books (title,author,num_pages,updated_at,created_at) value ('Ruby','Barnd Ruby',100,now(),now());
###################
update books set title='C #',updated_at=now() where id=1;
update users set name='Bill',updated_at=now() where id=4;
###################
insert into favorites (book_id,user_id) value (1,1);
insert into favorites (book_id,user_id) value (2,1);
###################
insert into favorites (book_id,user_id) value (1,2);
insert into favorites (book_id,user_id) value (2,2);
insert into favorites (book_id,user_id) value (3,2);
######################
insert into favorites (book_id,user_id) value (1,3);
insert into favorites (book_id,user_id) value (2,3);
insert into favorites (book_id,user_id) value (3,3);
insert into favorites (book_id,user_id) value (4,3);
###################
insert into favorites (book_id,user_id) value (1,4);
insert into favorites (book_id,user_id) value (2,4);
insert into favorites (book_id,user_id) value (3,4);
insert into favorites (book_id,user_id) value (4,4);
insert into favorites (book_id,user_id) value (5,4);


#####################
select * from users as t1 left join favorites as t2 on t1.id=t2.user_id
left join books as t3 on t2.book_id=t3.id where t2.book_id=3;
######################
delete from favorites where book_id=3 and user_id=(select * from (
select t1.id from users as t1 left join favorites as t2 on t1.id=t2.user_id
left join books as t3 on t2.book_id=t3.id where t2.book_id=3 limit 1) as new);
#################
insert into favorites (book_id,user_id) values (2,5);
select * from users as t1 left join favorites as t2 on t1.id=t2.user_id
left join books as t3 on t2.book_id=t3.id;
#################
select t1.name,group_concat(' ',t3.title) from users as t1 left join favorites as t2 on t1.id=t2.user_id
left join books as t3 on t2.book_id=t3.id where t1.id=3 group by t1.name
#################
select t1.name from users as t1 left join favorites as t2 on t1.id=t2.user_id
left join books as t3 on t2.book_id=t3.id where t2.book_id=5
