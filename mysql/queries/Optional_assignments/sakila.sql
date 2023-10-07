################1
select t1.first_name,t1.last_name,t1.email,t2.address,t3.city_id from customer as t1 
left join address as t2 on t1.address_id=t2.address_id
left join city as t3 on t2.city_id=t3.city_id where t3.city_id=312;

################2
select t1.title,t1.description,t1.release_year,t1.special_features,t3.name
from film as t1
left join film_category as t2 on t1.film_id=t2.film_id
left join category as t3 on t2.category_id=t3.category_id 
where t3.name='Comedy';

################3
select t3.actor_id,t3.first_name,t3.last_name,t1.title,t1.description,t1.release_year
from film as t1
left join film_actor as t2 on t1.film_id=t2.film_id
left join actor as t3 on t2.actor_id=t3.actor_id where t3.actor_id=5;

################4
select t1.first_name,t1.last_name,t1.email,t2.address,t3.city_id,t3.city from customer as t1 
left join address as t2 on t1.address_id=t2.address_id
left join city as t3 on t2.city_id=t3.city_id where t3.city_id in (1,42,312,459) and t1.store_id=1;

################5
select t1.title,t1.description,t1.release_year,t1.rating,t1.special_features
from film as t1
left join film_actor as t2 on t1.film_id=t2.film_id
left join actor as t3 on t2.actor_id=t3.actor_id where t1.rating='G' and t1.special_features like '%Behind the Scenes%' and 
t3.actor_id=15;

################6
select t1.film_id,t1.title,t3.actor_id,t3.first_name,t3.last_name
from film as t1
left join film_actor as t2 on t1.film_id=t2.film_id
left join actor as t3 on t2.actor_id=t3.actor_id where t1.film_id=369;

################7
select t1.title,t1.description,t1.release_year,t1.special_features,t3.name
from film as t1
left join film_category as t2 on t1.film_id=t2.film_id
left join category as t3 on t2.category_id=t3.category_id 
where t3.name='Drama' and t1.rental_rate=2.99;


################8
select tnew.film_id,tnew.title,tnew.description,tnew.release_year,tnew.special_features,t5.first_name,t5.last_name from
(select t1.film_id,t1.title,t1.description,t1.release_year,t1.special_features,t3.name as genra
from film as t1
left join film_category as t2 on t1.film_id=t2.film_id
left join category as t3 on t2.category_id=t3.category_id 
where t3.name='Action') as tnew
left join film_actor as t4 on tnew.film_id=t4.film_id
left join actor as t5 on t4.actor_id=t5.actor_id 
where t5.first_name='SANDRA'
and t5.last_name='KILMER'