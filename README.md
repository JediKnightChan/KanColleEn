# KanColleEn - Kantai Collection English localization

KanColleEn uses MITMProxy for replacing game data on Japanese with translated content

## Warning
### Open Beta Test
Not properly tested yet and not ready for mass distribution

Accounts banned: 0/1 (0%)

There IS a potential risk. (Though no malicious
scripts such as hash checkers have been found yet)

## Translation Progress
- Main game menu (ring menu)
- Side game menu
- "Build" tab

## Installation
- Install MITMProxy from their official site: https://mitmproxy.org/
- Pass KanColleEn.py to one of 3 MITMProxy programs (mitmdump/mitmweb/mitmproxy)
    ```cmd
    > mitmdump.exe --set anticache -s .\KanColleEn.py
    ```
    
## Features
- Can translate game interface
- TODO: add translating game API (dialogues, quests, fleet girls, etc)
