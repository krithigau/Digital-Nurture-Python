create database Cognizant;
use Cognizant;
create table sessions (
    session_id int primary key auto_increment,
    event_id int,
    title varchar(200) not null,
    speaker_name varchar(100) not null,
    start_time DATETIME not null,
    end_time datetime not null,
    foreign key(event_id) references events(event_id)
);

INSERT INTO Sessions (event_id, title, speaker_name, start_time, end_time) VALUES
(1, 'Opening Keynote', 'Dr. Tech', '2025-06-10 10:00:00', '2025-06-10 11:00:00'),
(1, 'Future of Web Dev', 'Alice Johnson', '2025-06-10 11:15:00', '2025-06-10 12:30:00'),
(2, 'AI in Healthcare', 'Charlie Lee', '2025-05-15 09:30:00', '2025-05-15 11:00:00'),
(3, 'Intro to HTML5', 'Bob Smith', '2025-07-01 10:00:00', '2025-07-01 12:00:00');

SELECT * FROM Sessions;
create table events(
    event_id int Primary key auto_increment,
    title varchar(100) not null,
    description text ,
    city varchar(100) not null,
    start_date DATETIME not null,
    end_date DATETIME not null,
    status enum('upcoming','completed','cancelled') default 'upcoming',
    organizer_id int ,
    foreign key (organizer_id) references users(user_id) 
);

INSERT INTO Events (title, description, city, start_date, end_date, status, organizer_id) VALUES
('Tech Innovators Meetup', 'A meetup for tech enthusiasts.', 'New York', '2025-06-10 10:00:00', '2025-06-10 16:00:00', 'upcoming', 1),
('AI & ML Conference', 'Conference on AI and ML advancements.', 'Chicago', '2025-05-15 09:00:00', '2025-05-15 17:00:00', 'completed', 3),
('Frontend Development Bootcamp', 'Hands-on training on frontend tech.', 'Los Angeles', '2025-07-01 10:00:00', '2025-07-03 16:00:00', 'upcoming', 2);

 select * from events;

create table feedback(
    feedback_id int primary key auto_increment,
    user_id int,
    event_id int,
    rating int check(rating between 1 and 5),
    comments text,
    feedback_date date not null,
    foreign key (user_id) references users(user_id),
    foreign key (event_id) references events(event_id)
);

INSERT INTO Feedback (user_id, event_id, rating, comments, feedback_date) VALUES
(3, 2, 4, 'Great insights!', '2025-05-16'),
(4, 2, 5, 'Very informative.', '2025-05-16'),
(2, 1, 3, 'Could be better.', '2025-06-11');

SELECT * FROM Feedback;
create table resources (
    resource_id int primary key auto_increment,
    event_id int,
    resource_type enum('pdf','image','link') default 'link',
    resource_url varchar(255) not null,
    uploaded_at DATETIME not null,
    foreign key (event_id) references events(event_id)
);

INSERT INTO Resources (event_id, resource_type, resource_url, uploaded_at) VALUES
(1, 'pdf', 'https://portal.com/resources/tech_meetup_agenda.pdf', '2025-05-01 10:00:00'),
(2, 'image', 'https://portal.com/resources/ai_poster.jpg', '2025-04-20 09:00:00'),
(3, 'link', 'https://portal.com/resources/html5_docs', '2025-06-25 15:00:00');

SELECT * FROM Resources;

create table registrations(
    registeration_id int primary key auto_increment,
    user_id int ,
    event_id int,
    registration_date date not null,
    foreign key (user_id) references users(user_id),
    foreign key(event_id) references events(event_id)
);

INSERT INTO Registrations (user_id, event_id, registration_date) VALUES
(1, 1, '2025-05-01'),
(2, 1, '2025-05-02'),
(3, 2, '2025-04-30'),
(4, 2, '2025-04-28'),
(5, 3, '2025-06-15');

SELECT * FROM Registrations;

create table users(
    user_id int primary key auto_increment,
    full_name varchar(100) not null,
    email varchar(100) not null unique,
    city varchar(100) not null,
    registration_date DATE not null
);

insert into users(full_name,email,city,registration_date) values
('Alice Johnson', 'alice@example.com', 'New York', '2024-12-01'),
('Bob Smith', 'bob@example.com', 'Los Angeles', '2024-12-05'),
('Charlie Lee', 'charlie@example.com', 'Chicago', '2024-12-10'),
('Diana King', 'diana@example.com', 'New York', '2025-01-15'),
('Ethan Hunt', 'ethan@example.com', 'Los Angeles', '2025-02-01');

-- Statement 1 : Show a list of all upcoming events a user is registered for in their city, sorted by date.
select e.title,e.city,u.full_name,e.status,e.start_date 
from users u 
join registrations r on u.user_id= r.user_id
join events e on r.event_id = e.event_id
where e.status='upcoming' and u.city= e.city order by e.start_date;

-- 	Statement 2: Identify events with the highest average rating, considering only those that have received at 
-- least 10 feedback submissions. 
select e.title, count(f.user_id) total_feedback,AVG(f.rating) avg_rating from events e 
join feedback f on e.event_id = f.event_id 
GROUP BY e.event_id,e.title HAVING count(f.user_id)>=10
ORDER BY avg_rating DESC ;

-- Q3  Retrieve users who have not registered for any events in the last 90 days.
SELECT u.full_name,u.city from users u 
WHERE u.user_id not in
(SELECT user_id from registrations where registration_date >=curdate() - interval 90 day);

-- Q4 Peak Session Hours 
-- Count how many sessions are scheduled between 10 AM to 12 PM for each event.
SELECT e.title, COUNT(s.session_id) FROM events e
join sessions s on e.event_id=s.event_id 
WHERE TIME(s.start_time)>='10:00:00' and TIME(s.end_time) <='12:00:00'
GROUP BY s.event_id ;

-- 5. Most Active Cities
-- List the top 5 cities with the highest number of distinct user registrations.
SELECT e.city , COUNT(DISTINCT(r.user_id)) counter 
from registrations r join events e on r.event_id=e.event_id
GROUP BY e.city
 ORDER BY counter desc LIMIT 5;

-- 6. Event Resource Summary
-- Generate a report showing the number of resources (PDFs, images, links) uploaded for each
-- event.
SELECT e.title ,COUNT(r.resource_type) no_of_resouces from resources r 
left  join events e
on e.event_id = r.event_id GROUP BY e.event_id;

-- 7. Low Feedback Alerts
-- List all users who gave feedback with a rating less than 3, along with their comments and
-- associated event names.
SELECT u.full_name , e.title , f.rating , f.comments
from users u
join feedback f on u.user_id = f.user_id 
join events e on f.event_id = e.event_id 
where f.rating < 3;

-- 8. Sessions per Upcoming Event
-- Display all upcoming events with the count of sessions scheduled for them.

SELECT e.title , COUNT(s.session_id) no_of_sessions  from events e 
left join sessions s on e.event_id = s.event_id
 where e.status='upcoming' 
 GROUP BY  e.title;

-- 9. Organizer Event Summary (KRITHIGA U)
-- For each event organizer, show the number of events created and their current status
-- (upcoming, completed, cancelled).

SELECT u.full_name ,COUNT(e.event_id)no_of_events , e.status
from users u 
join events e on u.user_id = e.organizer_id
GROUP BY e.organizer_id ,e.status ;

-- 10. Feedback Gap (KRITHIGA U)
-- Identify events that had registrations but received no feedback at all.
SELECT e.title from events e 
JOIN registrations r ON e.event_id = r.event_id
LEFT JOIN feedback f on r.event_id = f.event_id 
where f.feedback_id is null;


-- 11. Daily New User Count (KRITHIGA U)
-- Find the number of users who registered each day in the last 7 days.
SELECT registration_date, COUNT(user_id) registered_last_7days from registrations 
where registration_date > sysdate()- interval 7 day
GROUP BY registration_date;


-- 12. Event with Maximum Sessions (KRITHIGA)
-- List the event(s) with the highest number of sessions.

SELECT e.title , COUNT(s.session_id) no_of_sessions from events e 
join sessions s on e.event_id = s.event_id 
GROUP BY e.event_id , e.title ORDER BY no_of_sessions desc limit 1;

-- 13.  Average Rating per City
-- Calculate the average feedback rating of events conducted in each city.
 SELECT e.city, AVG(f.rating) ratings from events e 
 join feedback f on e.event_id = f.event_id
 GROUP BY (e.city);


-- 14. Most Registered Events
-- List top 3 events based on the total number of user registrations.
SELECT e.title , count(r.user_id) no_of_reg FROM events e join registrations r
on e.event_id = r.event_id
GROUP BY e.event_id ORDER BY no_of_reg desc LIMIT 3;


-- 15. Event Session Time Conflict (krithiga u)
-- Identify overlapping sessions within the same event (i.e., session start and end times that
-- conflict).
SELECT s1.event_id , s1.title , s1.start_time , s1.end_time ,
s2.start_time , s2.end_time from sessions s1 
join sessions s2 ON s1.event_id = s2.event_id 
and s1.session_id < s2.session_id
WHERE s1.start_time < s2.end_time and s1.end_time > s2.start_time;

-- 16. Unregistered Active Users
-- Find users who created an account in the last 30 days but haven’t registered for any events.

SELECT full_name from users 
WHERE registration_date >= sysdate() - interval 30 day
and user_id not in (SELECT user_id from registrations) ;

-- 17. Multi-Session Speakers
-- Identify speakers who are handling more than one session across all events.
SELECT speaker_name , count(session_id) event_handling from sessions 
GROUP BY speaker_name HAVING event_handling>1;

-- 18. Resource Availability Check (KRITHIGA U)
-- List all events that do not have any resources uploaded.
SELECT title from events where event_id not in(select event_id from resources);

-- 19. Completed Events with Feedback Summary
-- For completed events, show total registrations and average feedback rating.

SELECT e.title ,COUNT(distinct r.registeration_id) 'tot_reg ', AVG(f.rating) 'avg_ratings'
from events e 
JOIN registrations r on r.event_id = e.event_id 
JOIN feedback f on f.event_id = e.event_id
where e.status='completed'
GROUP BY e.event_id ;

-- 20. User Engagement Index *(KRITHIGA U)
-- For each user, calculate how many events they attended and how many feedbacks they
-- submitted.
SELECT u.full_name ,COUNT(r.event_id) events_attended,
COUNT(f.feedback_id) feedback_submitted from users u
LEFT JOIN feedback f on u.user_id = f.user_id
LEFT JOIN  registrations r on u.user_id = r.user_id
GROUP BY u.full_name;

-- 21. Top Feedback Providers (KRITHIGA U)
-- List top 5 users who have submitted the most feedback entries.
select u.full_name,count(f.feedback_id) no_of_feedback
from feedback f 
right join users u
on u.user_id=f.user_id
group by u.user_id 
order by 2 desc limit 5;

-- 22. Duplicate Registrations Check (KRITHIGA U)
-- Detect if a user has been registered more than once for the same event.
select user_id,event_id ,count(*) count
from registrations
group by user_id,event_id
having count>1;

-- 23. Registration Trends krithiga u
-- Show a month-wise registration count trend over the past 12 months.
select DATE_FORMAT(registration_date, '%Y-%m') AS month,
    count(*) AS registration_count
from registrations
where registration_date >= DATE_SUB(Date('2026-01-01'), INTERVAL 12 MONTH)
group by DATE_FORMAT(registration_date, '%Y-%m')
order by month asc;

-- 24.
select e.title, avg(timestampdiff(minute, s.start_time,s.end_time)) as avg_timestamp
from Sessions s
join Events e on e.event_id = s.event_id
group by e.event_id,e.title;


-- 25. Events Without Sessions -KRITHIGA U
-- List all events that currently have no sessions scheduled under them.
select e.title from events e 
left join sessions s 
on s.event_id = e.event_id
where s.session_id is null;