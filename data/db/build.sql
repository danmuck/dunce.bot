CREATE TABLE IF NOT EXISTS exp (
    UserID integer PRIMARY KEY,
    XP integer DEFAULT 0,
    Level integer DEFAULT 0,
    XPLock text DEFAULT CURRENT_TIMESTAMP
);

-- create table for client guilds for custom prefix
CREATE TABLE IF NOT EXISTS guilds (
    GuildID integer PRIMARY KEY,
    Prefix text DEFAULT "?"
);

CREATE TABLE IF NOT EXISTS roles (
    GuildID integer PRIMARY KEY,
    Roles text DEFAULT "roles"
);