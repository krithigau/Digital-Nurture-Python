# Event Management System - SQL Query Portfolio

## Description
A comprehensive collection of SQL queries demonstrating database analysis and manipulation for an Event Management System. This repository contains solutions to 16 complex data extraction scenarios, highlighting advanced querying techniques, data aggregation, and performance-optimized table joins.

## Database Schema Overview
The queries are built around a normalized relational database containing the following core tables:
* **Users:** Account details and registration dates.
* **Events:** Event metadata, organizers, and statuses (e.g., upcoming, completed).
* **Registrations:** Ticket purchases linking users to specific events.
* **Sessions:** Individual schedule blocks and time slots within events.
* **Feedback:** User ratings and reviews submitted for events.
* **Resources:** Files and materials attached to events.

## Key SQL Concepts Demonstrated
* **Advanced Joins:** `INNER JOIN`, `LEFT JOIN`, and Self-Joins to compare rows within the exact same table (e.g., finding time conflicts).
* **Anti-Joins:** Utilizing `LEFT JOIN` + `IS NULL` and `NOT IN` subqueries to find missing or non-existent data (e.g., finding events with zero resources).
* **Aggregations:** Grouping data using `GROUP BY` and filtering aggregated metrics using the `HAVING` clause.
* **Date & Time Functions:** Using `DATE_FORMAT`, `TIMESTAMPDIFF`, `CURRENT_DATE`, and `INTERVAL` for trend analysis and precise time-gap calculations.
* **Subqueries:** Implementing nested queries for complex filtering logic and exclusion lists.

## Repository Contents
The SQL file in this repository includes queries that solve real-world analytical business questions, such as:
1. Identifying active users and calculating average feedback ratings grouped by city.
2. Finding precise schedule conflicts using mathematical time-overlap formulas.
3. Generating month-wise user registration trends over a 12-month period.
4. Discovering events with zero registrations or brand new users who haven't registered for any events.
5. Highlighting top-performing events based on attendance and identifying multi-session speakers.

## Author
**Krithiga U**

B.Tech Artificial Intelligence and Machine Learning 
SAVEETHA ENGINEERING COLLEGE
