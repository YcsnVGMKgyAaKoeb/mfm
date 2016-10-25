
-- Create the base tables and triggers for a flat nodes storage
--
--
-- ----------------------------------------------------------------------------

-- the table for the datas
CREATE TABLE IF NOT EXISTS "Nodes"(
    "id" INTEGER NOT NULL,
    "label" TEXT NOT NULL, -- eg. store dirpath/filepath for a filesystem tree
    "type" TEXT NOT NULL, -- eg. f for file d for dir for a filesystem tree
    "datas" BLOB DEFAULT NULL, -- eg. file binary datas for a filesystem tree
    PRIMARY KEY ("id")
);
