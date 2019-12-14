drop database if exists javabook;
create database javabook;

create user if not exists 'jonathan'@'localhost' identified by 'temppass';
grant all privileges on *.* to 'jonathan'@'%' identified by 'temppass';

use javabook;

drop table if exists Address;

create table Address (
  name varchar(25),
  street varchar(50),
  city varchar(25),
  state char(2),
  zipcode char(5),
  primary key (name));
  
insert into Address values (
  'Jeremy Joe', '89 Pulaski Hwy', 'Wilmington', 'DE', '19801');
insert into Address values (
  'Alison Ranch', '6 Peninsula St', 'Grand Rapids', 'MI', '49503');
insert into Address values (
  'Kendra Lamar', '631 Carraige Court', 'Alabaster', 'AL', '35007');
insert into Address values (
  'Maverick Johnson', '229 Santa Clara Court', 'Apex', 'NC', '27502');
insert into Address values (
  'Bob Bomon', '726 Eagle Drive', 'Elkton', 'MD', '21921');
insert into Address values (
  'Linda Keller', '697 Mechanic Street', 'Newark', 'DE', '19061');
insert into Address values (
  'Aaron Kent', '966 N. Gregory Street', 'Irwin', 'PA', '15642');
insert into Address values (
  'Sam Jack', '7803 Grandrose St', 'Windermere', 'FL', '34786');
insert into Address values (
  'Zach Bell', '996 Fordham St', 'New Kensington', 'PA', '15068');
insert into Address values (
  'Chris Johnson', '467 S. Edgefield St', 'Ridgewood', 'NJ', '07450');
insert into Address values (
  'Jason Smith', '28 Kent Drive', 'Utica', 'NY', '13501');
insert into Address values (
  'Vivian Green', '628 East Ivy St', 'Alexandria', 'VA', '22304');

commit;