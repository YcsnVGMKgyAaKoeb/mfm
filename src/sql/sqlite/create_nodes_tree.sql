
-- Create the base tables and triggers for a hierachical node storage
--
--
-- https://stackoverflow.com/questions/4048151/what-are-the-options-for-storing-hierarchical-data-in-a-relational-database
-- https://stackoverflow.com/questions/6802539/hierarchical-label-database-for-directories-in-filesystem#6802879
-- http://www.slideshare.net/billkarwin/models-for-hierarchical-data
-- http://dirtsimple.org/2010/11/simplest-way-to-do-tree-based-queries.html
-- http://www.sqlteam.com/article/more-trees-hierarchies-in-sql
-- ----------------------------------------------------------------------------

-- the table for the datas
CREATE TABLE IF NOT EXISTS "Nodes"(
    "id" INTEGER NOT NULL,
    "parent_id" INTEGER NOT NULL, -- root Nodes are Nodes where id = parent_id
    "label" TEXT NOT NULL, -- eg. store dirname/filename for a filesystem tree
    "datas" BLOB DEFAULT NULL, -- eg. file binary datas for a filesystem tree
    PRIMARY KEY ("id", "parent_id")
);

-- the closure table for tree queries
CREATE TABLE  IF NOT EXISTS "Tree"(
    "parent_id" INTEGER,
    "child_id" INTEGER,
    "child_depth" INTEGER, -- MAX(child_depth) is the depth of the tree
    PRIMARY KEY ("parent_id", "child_id", "child_depth")
);
-- ----------------------------------------------------------------------------

-- triggers on node insertions
-- create the (self, self, 0) reference in the closure table
CREATE TRIGGER "BeforeNodeInsert" BEFORE INSERT ON Nodes
BEGIN
    INSERT INTO
        Tree("parent_id", "child_id", "child_depth")
    VALUES
        (new.id, new.id, 0);
END;

-- create all the childs path references in the closure table
CREATE TRIGGER "AfterNodeInsert" AFTER INSERT ON Nodes
WHEN NEW.id != NEW.parent_id
BEGIN
    INSERT INTO
        Tree("parent_id", "child_id", "child_depth")
    SELECT
        tp.parent_id,
        tc.child_id,
        tp.child_depth + tc.child_depth + 1
    FROM
        Tree AS "tp",
        Tree AS "tc"
    WHERE
        tp.child_id = NEW.parent_id
    AND
        tc.parent_id = NEW.id;
END;
-- ----------------------------------------------------------------------------
-- TODO: triggers on node modifications

-- ----------------------------------------------------------------------------
-- TODO: triggers on node deletions

-- ----------------------------------------------------------------------------
-- views for easy selections

CREATE VIEW "TreeView" AS
    SELECT
        GROUP_CONCAT(n.id, '/') AS "id",
        GROUP_CONCAT(n.label, '/') AS "label"
    FROM
        "Nodes" AS "n"
    JOIN
        "Tree" AS "t"
    ON
        t.parent_id = n.id
    WHERE
        t.child_id >= 0
    GROUP BY
        t.child_id
    ORDER BY
        id;
