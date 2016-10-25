
-- Get the parents Nodes from a node id
--
--  parent_id = the node from which we want the path, must be an integer
--
-- https://stackoverflow.com/questions/6802539/hierarchical-label-database-for-directories-in-filesystem#6802879
-- ----------------------------------------------------------------------------


SELECT
    n.id, n.label
FROM
    Nodes n
JOIN
    Tree t
ON
    t.parent_id = n.id
WHERE
    t.child_id = {parent_id};
