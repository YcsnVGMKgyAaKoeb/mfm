
-- Get the childs nodes from a node id
--
--  path_separator = for a filesystem tree use the os path separator
--  parent_id = the node from which we want the path, must be an integer

SELECT
    nodes.id, nodes.label
FROM
    nodes
JOIN
    nodes_tree
ON
    nodes_tree.child_id = nodes.id
WHERE
    nodes_tree.child_depth = 1;
AND
    nodes_tree.parent_id = {parent_id}
