---
title: "Administration Menu for Add-ins"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/AddInAdminMenu.htm"
---

# Administration Menu for Add-ins

An add-in often contains commands intended both for end users and the administrator of the system. You can add these commands as menu items using the [IEdmCmdMgr5::AddCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddCmd.html) method. The downside to this is that the administrator commands are displayed in the File Explorer and, unless you check the logged-in user, all users are able to run the administrator commands.

In SOLIDWORKS PDM Professional 6.4, a new flag is added to IEdmCmdMgr5::AddCmd, [EdmMenuFlags::EdmMenu_Administration](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMenuFlags.html), which controls whether a menu command is hidden in the File Explorer. When the flag is set, the command is displayed only in SOLIDWORKS PDM Professional’s Administration tool when you right-click the add-in.
