---
title: "Remove Menu Commands, Menus, and Toolbar Buttons Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Remove_Menu_Commands_Menus_and_Toolbar_Buttons_Example_VB.htm"
---

# Remove Menu Commands, Menus, and Toolbar Buttons Example (VBA)

This example shows how to:

- retrieve the name of the parent menu.
- remove a toolbar button.
- remove a command from the main frame and context-sensitive menus.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Open a part document.
' 2. Verify that the Filter Edges button appears on the
'    Selection Filter toolbar.
'
' Postconditions:
' 1. Removes the Filter Edges button on the Selection
'    Filter toolbar for this SOLIDWORKS Design session.
' 2. Removes the Suppress command from the main frame and
'    context-sensitive menus for this SOLIDWORKS Design session.
' 3. Examine the Selection Filter toolbar to verify step 1.
' 4. Click or right-click a feature to verify step 2.
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim parentName As String
Dim name As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Get the name of the parent menu for the first occurrence
    ' of the Suppress command in part documents
    name = swApp.GetMenuStrings(swCommands_Suppress, 1, parentName)
```

```
    ' Remove the Filter Edges button from the Selection Filter toolbar
    ' in part documents
    swApp.RemoveFromMenu swCommands_FilterEdges, 1, 3, True

    ' Remove the Suppress command from all main frame menus in part documents; do
    ' not remove the parent menus
    swApp.RemoveFromMenu swCommands_Suppress, 1, 3, False
```

```
    ' Remove the Suppress command from all context-sensitive menus; do not
    ' remove the parent menus
    swApp.RemoveFromPopupMenu swCommands_Suppress, 1, swSelEVERYTHING, False
```

```
End Sub
```
