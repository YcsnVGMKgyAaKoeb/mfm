
-- Test datas for Nodes label
-- ----------------------------------------------------------------------------


INSERT INTO "Nodes" ("id", "parent_id", "label") VALUES
(0, 0, 'Node0'),
(1, 0, 'Node1'),
(2, 0, 'Node2'),
(3, 2, 'Node3'),
(4, 3, 'Node4'),
(5, 3, 'Node5'),
(6, 2, 'Node6'),
(7, 0, 'Node7'),
(8, 7, 'Node8'),
(9, 0, 'Node9');


-- the above insert represent the follwing tree
-- Node0
--  -> Node1
--  -> Node2
--      -> Node3
--          -> Node4
--          -> Node5
--      -> Node6
--  -> Node7
--      -> Node8
--  -> Node9
