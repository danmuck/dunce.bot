# big idiot bot

## coming soon...

### credit to: [guide](https://www.youtube.com/watch?v=F1HbEOp-jdg&list=PLYeOw6sTSy6ZGyygcbta7GcpI8a5-Cooc&index=1)

---

## fhi:

### download git: 

#### linux [debian]
`sudo apt update`   
`sudo apt-get install git`

#### macos [homebrew]
 `brew install git`

#### [windows](https://git-scm.com/downloads) 

---
### install python:
###### note: use `python3 --V` or `python3 --version` to check current version

#### linux (debian):
`sudo apt-get install python3`

#### [windows](https://python.org/downloads/)

---

### install pip: 
- #### check version:
    ###### note: could be `pip3`
    `pip --version` 
    or 
        `pip --V` 
    
    
- #### if no directory:

    linux (debian):
        `sudo apt-get update`
        `sudo apt-get -y install -U python3-pip`
        `pip3 --version`

---
### dependencies:

###### note: [ dotenv import optional ] if you'd rather comment the import lines out as they are not actively used
##### linux
    pip3 -m install -U discord.py apscheduler aiosqlite python-dotenv

##### windows
    py -m pip install -U discord.py apscheduler aiosqlite python-dotenv

##### macos 
    pip install discord.py apscheduler aiosqlite python-dotenv

###### note: IMPORTANT! create text file: 'token.0' in /client with _your_ bot token

###### note: you need to edit in your own id numbers until its finished
