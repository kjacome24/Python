######################
insert into users (first_name,last_name,created_at,updated_at) values ('Kevin','Jacome',now(),now()),('Arturo','Duque',now(),now()),
('Emir','Duque',now(),now()),('Arturo','Jacome',now(),now()),('Matias','G',now(),now()),('Arnold','S',now(),now());

select * from users;
select * from friendships;
###################
insert into friendships (user_id,friend_id,created_at,updated_at) values (1,2,now(),now()),(1,4,now(),now()),(1,6,now(),now());
############
insert into friendships (user_id,friend_id,created_at,updated_at) values (2,1,now(),now()),(2,3,now(),now()),(2,5,now(),now());
############
insert into friendships (user_id,friend_id,created_at,updated_at) values (3,2,now(),now()),(3,5,now(),now());
############
insert into friendships (user_id,friend_id,created_at,updated_at) values (4,3,now(),now());
############
insert into friendships (user_id,friend_id,created_at,updated_at) values (5,1,now(),now()),(5,6,now(),now());
############
insert into friendships (user_id,friend_id,created_at,updated_at) values (6,2,now(),now()),(6,3,now(),now());
##############

select t1.first_name,t1.last_name,t3.first_name as friend_first_name, t3.last_name as friend_last_name from users as t1 left join friendships as t2 on t1.id=t2.user_id
left join users as t3 on t2.friend_id=t3.id

#######
select concat_ws(' ',t1.first_name,t1.last_name) as User_full_name,group_concat(' ',t3.first_name,' ',t3.last_name) as friend_full_name from users as t1 left join friendships as t2 on t1.id=t2.user_id
left join users as t3 on t2.friend_id=t3.id where t1.id=1 group by concat_ws(' ',t1.first_name,t1.last_name)

#######
select count(t3.id) as '# of friends' from 
users as t1 left join friendships as t2 on t1.id=t2.user_id
left join users as t3 on t2.friend_id=t3.id 
#################

select concat_ws(' ',t1.first_name,t1.last_name) as User_full_name,count(t3.id) as Number_of_friends, group_concat(' ',t3.first_name,' ',t3.last_name) as friends_full_name from 
users as t1 left join friendships as t2 on t1.id=t2.user_id
left join users as t3 on t2.friend_id=t3.id group by concat_ws(' ',t1.first_name,t1.last_name) order by Number_of_friends desc limit 1;

##############

select concat_ws(' ',t3.first_name,t3.last_name) as friend_full_name from users as t1 left join friendships as t2 on t1.id=t2.user_id
left join users as t3 on t2.friend_id=t3.id where t1.id=3 order by friend_full_name
