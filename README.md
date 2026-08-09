# Frankenstein RO
## Credits, References & Disclaimer

---

# Disclaimer

This project does not intentionally distribute original Ragnarok Online game files, proprietary assets or commercial content.

Frankenstein RO is a personal experimental project created for learning, research and development purposes.

The main objective of this project is to study and experiment with Ragnarok Online server development, rAthena, client integration, scripting, database management, custom systems and gameplay modifications.

This project uses a combination of publicly available resources, community contributions, Ragnarok Online related references, personal modifications and experimental implementations.

However, I cannot guarantee that every listed source is the original author or creator of the content. Some references may point to reposts, mirrors, modifications or community archives where the original creator is unknown.

If you are the original author of any content used in Frankenstein RO and your name is missing, incorrect or incomplete, please contact me so proper credit can be added or corrected when possible.

This project is provided for educational and research purposes only.

I am not responsible for any misuse, unauthorized use, redistribution, modifications or any other use made by third parties using this project.

The purpose of this document is to preserve references and give credit to the Ragnarok Online community and its contributors.

---

# Project Information

## Frankenstein RO

Frankenstein RO is an experimental Ragnarok Online project built by combining different technologies, resources, scripts, references and ideas from the Ragnarok Online community.

The name reflects the development process:

A combination of different components brought together into a single customized Ragnarok Online experience, similar to the concept of assembling different parts into one creation.

---

# Project History and Purpose

Frankenstein RO was not originally created as a public project.

The repository was created after experiencing the difficulty of maintaining and combining multiple systems, resources, scripts, configurations and modifications into a single Ragnarok Online environment.

During development, several components were merged, tested, modified and adapted. Without proper version control and organization, the project became difficult to recover and maintain, resulting in loss of previous work and development history.

The purpose of this repository is to preserve the development process, maintain version history and document the experiments made during the creation of Frankenstein RO.

After reaching a more stable state, the project was made public as a technical reference for people interested in Ragnarok Online server development, rAthena customization and experimental development processes.

The repository represents the history of an experimental development process, including successes, failures, tests and solutions discovered along the way.

---

The project includes:

- rAthena server base;
- Ragnarok Online related content references;
- Community contributions;
- Custom systems;
- Client modifications;
- Gameplay adjustments;
- Experimental features.

---

# Original Game Rights

## Gravity Co., Ltd.

Ragnarok Online is a game developed and owned by Gravity Co., Ltd.

Official website:

https://www.gravity.co.kr/

Frankenstein RO is an unofficial fan-made experimental project created for educational and research purposes.

This project is not affiliated with, endorsed by, or supported by Gravity Co., Ltd.

All original Ragnarok Online intellectual property, including:

- Characters;
- Names;
- Lore;
- Maps;
- Artwork;
- Official assets;
- Game concepts;

belong to Gravity Co., Ltd. and their respective owners.

---

# Server Base

## rAthena

Main server emulator base.

Website:

https://rathena.org/

Repository:

https://github.com/rathena/rathena

Used for:

- Server emulator core;
- Script engine;
- Database structure;
- Main server framework;
- Development foundation.

---

# Community References

## OfflineRO

Reference:

https://www.youtube.com/@offlinero

Used for:

- rAthena development studies;
- Server customization references;
- Feature research;
- Fake player simulation research and experimentation.

Notes:

OfflineRO provided references and inspiration for custom server features, including fake player systems used for simulation and experimentation.

### Fake Player System

Frankenstein RO includes an experimental **Fake Player** system inspired by studies and references from the **OfflineRO** project.

The system is provided for **development, testing and server simulation** purposes and is **disabled by default**.

#### Enabling Fake Players

Open the following file:

```text
npc/re/scripts_monsters.conf
```

Locate this line:

```text
//npc: npc/re/mobs/cust_wsm.txt
```

Remove the leading `//` so it becomes:

```text
npc: npc/re/mobs/cust_wsm.txt
```

Save the file and restart the server, or reload the NPC scripts.

#### Disabling Fake Players

Open:

```text
npc/re/scripts_monsters.conf
```

Locate:

```text
npc: npc/re/mobs/cust_wsm.txt
```

Comment the line by adding `//` at the beginning:

```text
//npc: npc/re/mobs/cust_wsm.txt
```

Save the file and restart the server, or reload the NPC scripts.

> **Note:** This system is intended for development, testing and simulation environments. It is optional, disabled by default, and can be enabled or disabled at any time through the NPC configuration without affecting the rest of the project.

---

## PercyNPC

Reference:

https://www.youtube.com/@PercyNPC

Used for:

- VIP system studies;
- rAthena 2026 implementation references;
- OpenKore integration research;
- Automation system studies.

---

# Class Implementations

## Druid / Karnos / Alitea Classes

Author:

datawulf

GitHub:

https://github.com/datawulf

Reference:

rAthena Pull Request #9765

https://github.com/rathena/rathena/pull/9765

Used for:

- Druid class implementation;
- Karnos class implementation;
- Alitea class implementation.

Status:

Integrated into Frankenstein RO.

---

# Localization Contributions

## PT-BR Translation

Some NPC and script translations were based on the project:

- NPC-PTBR
- Author: NYD-DARK
- Repository:
  https://github.com/NYD-DARK/NPC-PTBR

The translations were adapted and integrated into Frankenstein RO, with compatibility adjustments for the current rAthena version.

---

# Client & Resources

## 2026-01-07 Ragexe ClientInfo + WARP

Author:

VictorHug0

Reference:

https://rathena.org/board/topic/149414-2026-01-07-ragexe-clientinfo-warp/

Profile:

https://rathena.org/board/profile/22192-victorhug0/

Used for:

- 2026 Ragnarok Online client research;
- Ragexe ClientInfo studies;
- WARP compatibility;
- Modern client environment testing;
- Client-side integration research.

Notes:

This reference was used during the client modernization process of Frankenstein RO.

Credits belong to VictorHug0 and all original contributors involved in this reference.

---

## Ragnarok Online Client Resources

Used resources include:

- Client resources from different Ragnarok Online environments and community references;
- Sprites;
- Effects;
- Interface improvements;
- Visual updates;
- Compatibility research and adjustments.

Sources:

Additional client resources are documented separately as their original sources are identified.

Notes:

Some resources may originate from official clients, community projects, private distributions or modified releases.

Original creators should be credited whenever identified.

---

# Scripts & Episode References

## rAthena Scripts / Official Episodes

Sources:

- rAthena official scripts;
- Official episode scripts;
- Community contributions.

Used for:

- Quests;
- NPC systems;
- Episode content;
- Official gameplay mechanics.

Modifications:

- Custom adjustments;
- Balance changes;
- Translation adaptations;
- Gameplay adaptations.

---

# Server Tools

## Server Monitor 2.2.6

Author:

DarkIrata

Reference:

https://rathena.org/board/files/file/2433-server-monitor/

Used for:

- Server monitoring;
- Administration tools;
- Server status tracking.

---

# Integration Work

## Frankenstein RO Integration

This project combines and adapts different components from multiple sources into a single Ragnarok Online environment.

Integration work includes:

- Server compatibility adjustments;
- Database merges;
- Client/server synchronization;
- Script adaptations;
- Resource integration;
- Custom balancing;
- Testing and debugging;
- Feature integration.

The main purpose of Frankenstein RO is not only collecting resources, but understanding how different systems interact and creating a functional customized environment.

---

# Custom Development

## Frankenstein RO Custom Modifications

Custom modifications created specifically for this project.

## Server Systems

- Custom VIP system;
- VIP plans;
- VIP shop;
- VIP buffs;
- NPC modifications;
- Gameplay balancing;
- Server configuration improvements.

## Client Improvements

- Modern client integration;
- Resource integration;
- Visual improvements;
- Compatibility fixes.

## Experimental Systems

- Fake player system research;
- OpenKore compatibility and automation research;
- Native Auto Hunt research;
- Automation studies;
- Custom gameplay experiments.

---

# Development Notes

## Client Visibility Fix

Problem:

Monsters were visible only at short distance despite camera adjustments.

Solution:

Changed `conf/battle/client.conf` (`area_size`).

---

## GM Appearance Issue

Problem:

A clientinfo account/group ID displayed GM appearance without actual GM permissions.

Solution:

Adjusted clientinfo configuration.

---

# Development Environment

## Tools Used

- GRF Editor;
- Git;
- Visual Studio;
- MySQL;
- phpMyAdmin;
- OpenKore;
- rAthena development tools.

---

# Project Status

Frankenstein RO is a personal experimental Ragnarok Online development project.

The project started as a study to verify if different Ragnarok Online technologies, resources and systems could be combined into a functional customized environment.

After reaching this initial objective, the project continued as a personal research and experimentation environment, including server improvements, translation integration, client compatibility research, gameplay adjustments and custom system development.

This repository is maintained as a record of development, experiments, solutions and discoveries made during the project.

There is no commitment to provide regular updates, future versions, new classes, quests or continuous feature additions.

Development will continue according to personal interest, available time and curiosity regarding new experiments.

The project may remain inactive for periods of time and this does not represent abandonment or a commitment failure.

The repository exists primarily as a technical reference and historical record of the development process.

---

# Credits Policy

All credits belong to their respective authors, developers and communities.

Third-party content remains property of its respective authors and copyright holders.

This document exists only to preserve references, acknowledge contributions and maintain transparency.

If any credit information is incorrect, incomplete or missing, please contact me so corrections can be made when possible.

---

# Frankenstein RO

Built from many pieces.

Built as an experiment.

Built to explore how different systems could become one functional experience.
