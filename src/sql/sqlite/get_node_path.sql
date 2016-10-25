
-- Get the full path from a node id
--
--  path_separator = for a filesystem label use the os path separator
--  parent_id = the node from which we want the path, must be an integer
--
-- https://stackoverflow.com/questions/6802539/hierarchical-label-database-for-directories-in-filesystem#6802879
-- ----------------------------------------------------------------------------


SELECT
    GROUP_CONCAT(Nodes.label, '{path_separator}') AS "path"
FROM
    Nodes
JOIN
    Tree
ON
    Tree.parent_id = Nodes.id
WHERE
    Tree.child_id = {parent_id};
