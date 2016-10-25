
-- Get the childs Nodes from a node id
--
--  parent_id = the node from which we want the path, must be an integer
--
-- https://stackoverflow.com/questions/6802539/hierarchical-label-database-for-directories-in-filesystem#6802879
-- ----------------------------------------------------------------------------


SELECT
    Nodes.id, Nodes.label
FROM
    Nodes
JOIN
    Tree
ON
    Tree.child_id = Nodes.id
WHERE
    Tree.child_depth = 1
AND
    Tree.parent_id = {parent_id};
