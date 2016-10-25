

PRAGMA encoding="UTF-8";
PRAGMA foreign_keys="ON";
PRAGMA journal_mode="MEMORY";


CREATE TABLE IF NOT EXISTS
"Networks"(
    "id" INTEGER,
    "name" VARCHAR(255) UNIQUE NOT NULL,
    "desciption" TEXT DEFAULT NULL,
    PRIMARY KEY ("id")
);

INSERT INTO "Networks" ("id", "name", "desciption") VALUES
(0, "internet", "le world wide web :p"),
(1, "anet", "réseau local du bureau"),
(2, "bnet", "réseau local du domicile");


CREATE TABLE IF NOT EXISTS
"Hosts"(
    "id" INTEGER,
    "name" VARCHAR(255) UNIQUE NOT NULL,
    "desciption" TEXT DEFAULT NULL,
    PRIMARY KEY ("id")
);

INSERT INTO "Hosts" ("id", "name", "desciption") VALUES
(0, "abox", "mon pc au bureau"),
(1, "bbox", "mon pc a la maison"),
(2, "cmob", "mon pc portable");


CREATE TABLE IF NOT EXISTS
"Network_has_hosts"(
    "host_id" INTEGER,
    "network_id" INTEGER,
    "ip4" VARCHAR(12) DEFAULT NULL,
    "ip6" VARCHAR(45) DEFAULT NULL,
    PRIMARY KEY ("network_id", "host_id"),
    FOREIGN KEY ("network_id") REFERENCES "Networks" ("id"),
    FOREIGN KEY ("host_id") REFERENCES "Hosts" ("id")
);

INSERT INTO "Network_has_hosts" ("network_id", "host_id", "ip4") VALUES
(0, 0, "192.168.0.1"),
(1, 0, "192.168.0.9"),
(0, 1, "10.0.0.8"),
(2, 1, "192.168.0.19"),
(0, 2, "192.168.0.211"),
(2, 2, "10.0.0.1");


CREATE TABLE IF NOT EXISTS
"Users"(
    "id" INTEGER,
    "name" VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY ("id")
);

INSERT INTO "Users" ("id", "name") VALUES
(0, 'rw');


CREATE TABLE IF NOT EXISTS
"Nodes"(
    "id" INTEGER,
    "parent_id" INTEGER,
    "label" TEXT NOT NULL, -- eg. store dirname for a filesystem label
    "datas" BLOB DEFAULT NULL, -- eg. file binaries for a filesystem label
    PRIMARY KEY ("id")
);

INSERT INTO "Nodes" ("id", "parent_id", "label") VALUES
(0, 0, 'Dir0'),
(1, 0, 'Dir1'),
(2, 0, 'Dir2'),
(3, 2, 'Dir3'),
(4, 3, 'Dir4'),
(5, 3, 'Dir5'),
(6, 2, 'Dir6'),
(7, 0, 'Dir7'),
(8, 7, 'Dir8'),
(9, 0, 'Dir9');
-- Dir0
--  -> Dir1
--  -> Dir2
--      -> Dir3
--          -> Dir4
--          -> Dir5
--      -> Dir6
--  -> Dir7
--      -> Dir8
--  -> Dir9

CREATE TABLE  IF NOT EXISTS
"Tree"(
    "parent_id" INTEGER,
    "child_id" INTEGER,
    "child_depth" INTEGER,
    PRIMARY KEY ("parent_id", "child_id"),
    FOREIGN KEY ("parent_id") REFERENCES "Nodes" ("id"),
    FOREIGN KEY ("child_id") REFERENCES "Nodes" ("id")
);

INSERT INTO "Tree" ("parent_id", "child_id", "child_depth") VALUES
(0,0,0),(0,1,1),(0,2,1),(0,3,2),(0,4,3),(0,5,3),(0,6,2),(0,7,1),(0,8,2),(0,9,1),
(1,1,0),
(2,2,0),(2,3,1),(2,4,2),(2,5,2),(2,6,1),
(3,3,0),(3,4,1),(3,5,1),
(4,4,0),
(5,5,0),
(6,6,0),
(7,7,0),(7,8,1),
(8,8,0),
(9,9,0);


CREATE TABLE IF NOT EXISTS
"files"(
    "id" INTEGER,
    "dir_id" INTEGER NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    PRIMARY KEY ("id", "dir_id")
    FOREIGN KEY ("dir_id") REFERENCES "dirs" ("id")
);


CREATE TABLE IF NOT EXISTS
"lastviews"(
    "dir_id" INTEGER NOT NULL,
    "file_path" VARCHAR(255) NOT NULL,
    PRIMARY KEY ("dir_id")
);
