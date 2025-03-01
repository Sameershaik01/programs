select * from employee;
use sameer;

SELECT COUNT(*) FROM employee;
SHOW TABLES;
select * from employee where ename='smith';
with tmp as(select *,row_number() over(order by sal desc ) as ranks from employee) select * from tmp where ranks=2;
select e.ename,d.dname from employee e inner join department d on(d.deptno=e.deptno) where e.sal>2300;