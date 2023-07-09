SELECT St.student_id, St.student_name, Su.subject_name, COUNT(E.subject_name) AS attended_exams
FROM Students St
    CROSS JOIN Subjects Su
    LEFT JOIN Examinations E ON St.student_id = E.student_id AND Su.subject_name = E.subject_name
GROUP BY St.student_id, St.student_name, Su.subject_name
ORDER BY St.student_id, Su.subject_name;