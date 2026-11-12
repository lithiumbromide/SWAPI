---
title: "Create Context-sensitive Menu Items Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Context-sensitive_Menu_Items_Example_VBA.htm"
---

# Create Context-sensitive Menu Items Example (VBA)

This example shows how to create default, command, and object context-sensitive menu items.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Press F5.
'
' Postconditions:
' 1. Connects to DraftSight.
' 2. Gets the active document.
' 3. Creates three user commands.
' 4. Adds a default context-sensitive menu item for the first user command.
' 5. Adds a command context-sensitive menu item for the second user command.
' 6. Adds an object context-sensitive menu item for the third user command.
' 7. Displays a message box informing you to perform steps 7a - 7f. Click OK
'    to close the message box before performing these steps.
'    a. Right-click anywhere in the the graphics area and
'       select Execute line command in the context-sensitive menu.
'       The crosshair pointer is displayed.
'    b. Right-click anywhere in the graphics area and select Open Help
'       in the context-sensitive menu. The user-interface DraftSight
'       Help system opens and displays the Constructing Lines Help topic.
'    c. Read the Help topic and close the Help.
'    d. Construct a line and select the line.
'    e. Right-click anywhere in the graphics area and
'       select Do pattern in the context-sensitive menu.
'       A pattern of the selected Line is constructed.
'    f. Press the Enter key and exit DraftSight.
'----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
```

```
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get active document
    Dim dsDoc As DraftSight.Document
    Set dsDoc = dsApp.GetActiveDocument()
```

```
    'Create three user commands for the context-sensitive menus
    Dim error As Long
    Dim lineUserCmd As UserCommand
    Dim helpUserCmd As UserCommand
    Dim patternUserCmd As UserCommand
```

```
    Set lineUserCmd = dsApp.CreateUserCommand("APIUUID", "TEST_LINE", "^C^C_LINE" + vbLf, "Line", "", "", dsUIState_e.dsUIState_Document, error)
    Set helpUserCmd = dsApp.CreateUserCommand("APIUUID", "TEST_HELP", "'_HELP" + vbLf, "Help", "", "", dsUIState_e.dsUIState_Document, error)
    Set patternUserCmd = dsApp.CreateUserCommand("APIUUID", "TEST_PATTERN", "_-PATTERN _L 3 3 5 5" + vbLf + vbLf, "Pattern", "", "", dsUIState_e.dsUIState_Document, error)
```

```
    Dim menuItemType As Long
    menuItemType = dsMenuItemType_e.dsMenuItemType_UserCommand
```

```
    Dim dsDefaultContextMenuItem As ContextMenuItem
    Dim dsCommandContextMenuItem As ContextMenuItem
    Dim dsObjectContextMenuItem As ContextMenuItem
```

```
    'Add default context-sensitive menu item for first user command
    Set dsDefaultContextMenuItem = dsApp.AddDefaultContextMenu("APIUUID", menuItemType, "Execute line command", lineUserCmd.GetID)

    'Add command context-sensitive menu item for second user command
    Set dsCommandContextMenuItem = dsApp.AddCommandContextMenu("APIUUID", menuItemType, "Open Help", helpUserCmd.GetID, "_LINE")

    'Add object context-sensitive menu item for third user command
    Set dsObjectContextMenuItem = dsApp.AddObjectContextMenu("APIUUID", menuItemType, "Do pattern", patternUserCmd.GetID, dsObjectType_e.dsLineType)
```

```
    MsgBox "Perform steps 7a - 7f."
```

```
End Sub
```
