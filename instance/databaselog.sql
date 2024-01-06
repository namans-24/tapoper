BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "User" (
    "id" INTEGER,
    "Email" TEXT NOT NULL,
    "Password" VARCHAR NOT NULL,
    "Company Name" TEXT NOT NULL,
    "Username" TEXT NOT NULL,
    PRIMARY KEY("id")
);
INSERT INTO "User" VALUES (1, 'namans10@gmail.com', 'Superman123', 'Kowtow', 'Naman');
COMMIT;
