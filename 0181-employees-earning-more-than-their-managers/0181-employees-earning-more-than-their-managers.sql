# Write your MySQL query statement below
SELECT e.name As Employee FROM Employee e Join Employee m ON e.managerID = m.id
WHERE e.salary >m.salary;