# Alert project
The project consists of two parts:
- [`Alert system part`](https://github.com/SkrobatDmitry/alert_project/tree/master/alert_system) processes and analyzes logs and catches errors.
- [`File receiving emulation part`](https://github.com/SkrobatDmitry/alert_project/tree/master/file_receiving_emulator) emulates the operation of a mobile application for receiving logs.

## Launch of the project
The project is launched with a single command that installs all dependencies, configure volumes, configure container addresses and runs them:
```bash
docer-compose up
```