# Capstone
Using Python, create a program that enumerates and helps detect malicious files on your computer

# Multiphase 
Three Phase project
## Phase 1
TODO:
- [x] File hashing
    - [x] MultiProcessing
    - [x] MultiThreading
    - [x] Error Handling
- [x] Windows Registry Enumeration
    - [x] Error Handling
## Phase 2
TODO:
- [x] Logging
    - [x] Error Handling
- [x] Caching
    - [x] Implement Context Manager
    - [x] Ability to update/reset File hashing cache
    - [x] Ability to update/reset VirusTotal cache
    - [x] Error Handling
- [x] VirusTotal API
    - [x] Meet Free tier requirements
        - [ ] Auto schedule/limit daily API calls
    - [x] Error Handling
## Phase 3
TODO:
- [ ] GUI
    - [x] For each hash: Display VirusTotal results 
    - [x] For each hash: Enable shortcut to Virustotal webpage
    - [ ] Implement table filter when given a string 
        - [ ] add regex functionality
    - [ ] Error Handling