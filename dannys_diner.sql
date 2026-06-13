/* --------------------
   Case Study Questions
   --------------------*/

-- 1. What is the total amount each customer spent at the restaurant?
-- 2. How many days has each customer visited the restaurant?
-- 3. What was the first item from the menu purchased by each customer?
-- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?
-- 5. Which item was the most popular for each customer?
-- 6. Which item was purchased first by the customer after they became a member?
-- 7. Which item was purchased just before the customer became a member?
-- 8. What is the total items and amount spent for each member before they became a member?
-- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
-- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?

-- Example Query:
--SELECT
  --	product_id,
    --product_name,
    --price
--FROM dannys_diner.menu
--ORDER BY price DESC
--LIMIT 5;



CREATE database dannys_diner;
use dannys_diner;

CREATE TABLE sales (
  "customer_id" VARCHAR(1),
  "order_date" DATE,
  "product_id" INTEGER
);

INSERT INTO sales
  ("customer_id", "order_date", "product_id")
VALUES
  ('A', '2021-01-01', '1'),
  ('A', '2021-01-01', '2'),
  ('A', '2021-01-07', '2'),
  ('A', '2021-01-10', '3'),
  ('A', '2021-01-11', '3'),
  ('A', '2021-01-11', '3'),
  ('B', '2021-01-01', '2'),
  ('B', '2021-01-02', '2'),
  ('B', '2021-01-04', '1'),
  ('B', '2021-01-11', '1'),
  ('B', '2021-01-16', '3'),
  ('B', '2021-02-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-07', '3');
  select * from sales;

CREATE TABLE menu (
  "product_id" INTEGER,
  "product_name" VARCHAR(5),
  "price" INTEGER
);

INSERT INTO menu
  ("product_id", "product_name", "price")
VALUES
  ('1', 'sushi', '10'),
  ('2', 'curry', '15'),
  ('3', 'ramen', '12');
  
select * from menu;

CREATE TABLE members (
  "customer_id" VARCHAR(1),
  "join_date" DATE
);

INSERT INTO members
  ("customer_id", "join_date")
VALUES
  ('A', '2021-01-07'),
  ('B', '2021-01-09');

select * from members;

--ans1.
SELECT s.customer_id,sum(m.price) as totalmoneyspend
from sales s 
inner join menu m
on s.product_id=m.product_id
group by s.customer_id;

--ans2.
select customer_id,count(distinct order_date) as Days
from sales
group by customer_id;

--ans3.
select s.customer_id,m.product_name 
from sales s join menu m
on s.product_id=m.product_id
where s.order_date=
( select min(order_date) from sales
 where customer_id=s.customer_id)
 group by s.customer_id, m.product_name;

--ans4.
select m.product_name, s.product_id
from menu m join sales s
on m.product_id=s.product_id
where s.product_id in (select top 1 product_id from sales group by product_id order by count(product_id) desc)
group by product_name,s.product_id;

--ans5.
select top 3
s.customer_id,m.product_name, count(s.product_id) as total_count
from sales s join menu m
on s.product_id=m.product_id
group by s.customer_id, m.product_name
order by count(s.product_id) desc, customer_id desc ;

--ans6.
 select m.customer_id,s.product_id,order_date,u.product_name
 from members m join sales s 
 on m.customer_id=s.customer_id
 join menu u 
 on s.product_id=u.product_id
 where s.order_date in( select min(order_date) from sales group by product_id);
 
--ans7
 select m.customer_id,s.product_id,order_date,u.product_name
 from members m join sales s 
 on m.customer_id=s.customer_id
 join menu u 
 on s.product_id=u.product_id
 where s.order_date in( select max(order_date) from sales where order_date<join_date group by customer_id);
 
--ans8
select m.customer_id, count(s.product_id) as total_count,sum(u.price) as total_price
 from members m join sales s 
 on m.customer_id=s.customer_id
 join menu u 
 on s.product_id=u.product_id
 where s.order_date in(select order_date from sales where order_date<join_date)
 group by m.customer_id;

--ans9
select s.customer_id, sum(m.price) as total_price, 
if m.product_name=


(total_price*10
from sales s join menu m
on s.product_id = m.product_id
group by s.customer_id;

--ans9 using cte
WITH customer_points AS (
    SELECT 
        s.customer_id,
        COUNT(m.product_name) AS total_items, -- <-- Yahan comma lagaya
        -- SUM ko CASE ke bahar lagaya aur logic sahi kiya
        SUM(
            CASE 
                WHEN m.product_name = 'sushi' THEN m.price * 20
                ELSE m.price * 10
            END
        ) AS points
    FROM sales s
    INNER JOIN menu m ON s.product_id = m.product_id
    GROUP BY s.customer_id
)
-- Yeh line likhna zaroori tha CTE ko complete karne ke liye:
SELECT customer_id, points 
FROM customer_points;