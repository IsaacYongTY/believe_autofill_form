# Introduction
I developed this script to aid in filling up repeated forms in Believe Backstage. I release my music through Believe Digital to various Digital Streaming Platforms, such as Spotify and Apple Music, and a part of the release process is to fill up a form indicating information such as social media and biography.

# Pain Points
- The form had to be filled manually for every release. There are no option to save previous entry so time is spent on manually copy and paste into each row.
- The manual process impedes productivity and creativity leading to slower music releases and suboptimal promotion write up

# Features
- Written with Python
- PyQt5 GUI
- Navigate to release pages and fill in the form automatically
- Optional auto-save option after form is filled

# Use Case
1. Fire up the script 
2. Once auto-login, find the release number of the intended release and key it in the script.
3. Upon running, the browser navigates itself to the release, fill up the form with the information provided. If there are already information, it will be cleared before being filled with the latest data.
4. If the save option is checked, the script will also save upon filling up the form

# Releases
## Current Release
### v1.1.0
  - Update code formatting
## Previous Release
### v1.0.0
  - Redesign UI
  - Update UI from tkinter to PyQt5
  - Refactor codes
### v.0.0.0
  - Working alpha build
