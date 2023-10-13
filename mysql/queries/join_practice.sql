#########Simple join
select clients.first_name,clients.last_name,billing.amount,billing.charged_datetime from clients join billing on clients.id=billing.clients_id;
select sites.domain_name,concat_ws(' ',leads.first_name,leads.last_name) as 'Lead Name' from sites join leads on sites.id=leads.sites_id order by sites.domain_name,leads.first_name;
##########Multiple joins
select concat_ws(' ',clients.first_name,clients.Last_name) as 'client Name',sites.domain_name,concat_ws(' ',leads.first_name,leads.last_name) as 'Lead name' from clients join sites on clients.id=sites.clients_id
join leads on sites.id=leads.sites_id order by concat_ws(' ',clients.first_name,clients.Last_name),sites.domain_name,concat_ws(' ',leads.first_name,leads.last_name);

###############Lef join 
select concat_ws(' ',clients.first_name,clients.Last_name) as 'client Name',sites.domain_name from clients left join sites on clients.id=sites.clients_id order by concat_ws(' ',clients.first_name,clients.Last_name),sites.domain_name ;

###############Group by
select clients.first_name,clients.last_name,sum(billing.amount) as 'total amount',count(billing.id) as '# transacctions' from clients left join billing on clients.id=billing.clients_id group by clients.id;
select concat_ws(' ',clients.first_name,clients.Last_name) as 'client Name',group_concat(' ',sites.domain_name) as 'domains' from clients join sites on clients.id=sites.clients_id group by clients.id;

################count with group by

select sites.domain_name,count(leads.id) as '# of leads' from sites join leads on sites.id=leads.sites_id group by sites.domain_name


###############Alias for joins
select t1.first_name,t1.last_name,year(t2.charged_datetime),sum(t2.amount) as 'total amount',count(t2.id) as '# transacctions' from clients as t1 left join billing as t2 on t1.id=t2.clients_id group by t1.id, year(t2.charged_datetime);


#######Autounion(slef-join) concept

select concat_ws(' ',t1.first_name,t1.last_name),concat_ws(' ',t3.first_name,t3.last_name) from users as t1 left join follows as t2 on t1.id=t2.followed_id 
left join users as t3 on t2.follower_id=t3.id
where t1.id=1


###########Nested query

select * from users where users.id not in (
select t2.follower_id as 'follower' from users as t1 left join follows as t2 on t1.id=t2.followed_id 
left join users as t3 on t2.follower_id=t3.id
where t1.id=2) and users.id !=2