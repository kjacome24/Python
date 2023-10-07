############################1
select countries.name,languages.language,concat(languages.percentage,'%') as Percentage  from countries left join languages on countries.id=languages.country_id where languages.language like "%Slovene%" order by Percentage desc;

############################2

select newx.id,newx.name,group_concat(' ',t2.language) as languages,newx.Number_of_cities from (select countries.id, countries.name,count(cities.id) as Number_of_cities from countries join cities on countries.id=cities.country_id group by countries.id,countries.name) as newx
join languages as t2 on newx.id=t2.country_id
group by newx.id,newx.name
order by newx.Number_of_cities desc
;


############################3

select cities.name,cities.population from countries left join cities on countries.id=cities.country_id  where countries.name='Mexico'and cities.population>500000 order by cities.population desc ;


###########################4
select countries.name,languages.language,concat(languages.percentage,'%') as Percentage  from countries 
left join languages on countries.id=languages.country_id  where languages.percentage>89 order by Percentage desc;

###########################5
select name,surface_area,population from countries where surface_area<501 and population>100000;

###########################6

select name,government_form,capital,life_expectancy from countries 
where life_expectancy>75 and government_form='Constitutional Monarchy' and capital>200;

###########################7
select countries.name,cities.name,cities.district,cities.population from countries left join cities on countries.id=cities.country_id where cities.district like '%Buenos%'and cities.population>500000;

###########################8

select region,count(id) as countries from countries group by region order by countries desc;