BEGIN TRANSACTION;

CREATE TABLE "annotations" (
	`domain1`	TEXT,
	`domain2`	TEXT,
	`domain3`	TEXT,
	`object1`	TEXT NOT NULL,
	`object2`	TEXT NOT NULL,
	`object3`	TEXT 
);

CREATE INDEX annotation_to_object ON annotations (object1, object2, domain2);
CREATE INDEX annotation_to_annotation ON annotations (object1, domain1, object2, domain2);
CREATE INDEX obejct_to_object ON annotations (object1, object2, object3, domain3);

COMMIT;
