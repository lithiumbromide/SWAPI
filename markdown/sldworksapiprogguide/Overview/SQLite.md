---
title: "SQLite"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/SQLite.htm"
---

# SQLite

Only one instance of SQLite can run in SOLIDWORKS process space. SOLIDWORKS maintains a reference to the SQLite singleton. To ensure compatiblity, your SOLIDWORKS add-in must use a version of **System.Data.SQLite.dll** that is the same as the version used by SOLIDWORKS. In File Explorer, place your cursor over `install_dir`**\System.Data.SQLite.dll** to get the version used by your SOLIDWORKS installation.

For example, if you discover that SOLIDWORKS uses SQLite version 1.0.76.0, then download and set up the compatible SQLite version for your add-in:

**[http://system.data.sqlite.org/downloads/1.0.76.0/sqlite-netFx40-setup-bundle-x64-2010-1.0.76.0.exe](http://system.data.sqlite.org/downloads/1.0.76.0/sqlite-netFx40-setup-bundle-x64-2010-1.0.76.0.exe)**
