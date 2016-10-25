
-- Print all Nodes pathes from Nodes label
--
-- https://karwin.blogspot.fr/2010/03/rendering-labels-with-closure-tables.html
-- ----------------------------------------------------------------------------

SELECT
    GROUP_CONCAT(n.label, '/') AS "path"
FROM
    Nodes AS n
JOIN
    Tree AS t
ON
    t.parent_id = n.id
WHERE
    t.child_id >= 0
GROUP BY
    t.child_id;
