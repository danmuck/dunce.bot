CREATE TABLE IF NOT EXISTS exp (
    UserID integer PRIMARY KEY,
    UserName text DEFAULT "n/a",
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

-- CREATE TABLE IF NOT EXISTS starboard (
--     RootMessageID integer PRIMARY KEY,
--     StarMessageID integer,
--     Stars integer DEFAULT 1

-- );

CREATE TABLE IF NOT EXISTS links (
    ChannelID integer,
    Link text PRIMARY KEY,
    Category text DEFAULT "n/a",
    OrigMessage text DEFAULT "n/a"
);

CREATE TABLE IF NOT EXISTS stuffs (
    Added text DEFAULT CURRENT_TIMESTAMP,
    Statuses text PRIMARY KEY
)