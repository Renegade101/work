SELECT id, 
Case 
when p_id IS NULL then 'Root'
when id in (SELECT p_id FROM Tree) then 'Inner'
else 'Leaf'
end as type
FROM Tree
