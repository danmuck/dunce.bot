CREATE TABLE IF NOT EXISTS exp (
    UserID integer PRIMARY KEY,
    UserName text DEFAULT "?",
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

CREATE TABLE IF NOT EXISTS todo_ (
    Added text DEFAULT CURRENT_TIMESTAMP,
    Notes text PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS items (
    ItemID int PRIMARY KEY,
    Name text DEFAULT Null,
    Description text DEFAULT Null,
    Category text DEFAULT Null
);

CREATE TABLE IF NOT EXISTS gusers (
    gUserName text PRIMARY KEY,
    gPassword text DEFAULT ""
);

