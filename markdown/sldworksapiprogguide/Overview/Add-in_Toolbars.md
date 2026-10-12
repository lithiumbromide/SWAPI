---
title: "Add-in Toolbars"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Add-in_Toolbars.htm"
---

# Add-in Toolbars

The first time a SOLIDWORKS add-in runs, its toolbars are instantiated, which means that the add-in acquires a toolbar ID for each of its toolbars and their buttons. Toolbar IDs are stored in the registry.

To change an add-in toolbar during development, you can clear the registry before changing the toolbar. However, for the release version of the add-in, assign a new toolbar ID to each new add-in toolbar so that it becomes a new toolbar in the CommandGroup. Users who run different versions of the add-in and SOLIDWORKS can then use the appropriate version of the add-in toolbar, because activating an add-in toolbar won't collide with a different version of SOLIDWORKS.

To learn more about add-ins and their menu items and toolbars:

- [Add-in Callbacks](Add-in_Callbacks.htm)
- [Add-in Icons](Add-in_Icons.htm)
- [Add-in Shortcut Menus](Add-in_Shortcut_Menus.htm)
- [Using SwAddin to Create a SOLIDWORKS Add-in](Using_SwAddin_to_Create_a_SolidWorks_Addin.htm)
- [SOLIDWORKS API Add-in Templates and Wizards](SolidWorks_API_Add-Ins,_Project_Templates,_and_Wizards.htm)
