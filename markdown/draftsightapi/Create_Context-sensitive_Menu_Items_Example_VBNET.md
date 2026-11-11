---
title: "Create Context-sensitive Menu Items Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Context-sensitive_Menu_Items_Example_VBNET.htm"
---

# Create Context-sensitive Menu Items Example (VB.NET)

This example shows how to create default, command, and object context-sensitive menu items.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this code into the VB.NET project.
' 3. Add a reference to
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Add a reference to System.Windows.Forms.
' 5. Start DraftSight.
' 6. Press F5.
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

Imports System
Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System.Windows.Forms

Module Module1

    Sub Main()

        Dim dsApp As DraftSight.Interop.dsAutomation.Application

        'Connect to DraftSight application
        dsApp = GetObject(, "DraftSight.Application")

        If dsApp Is Nothing Then
            Return
        End If
```

```
        'Abort any command currently running in DraftSight to avoid nested commands
        dsApp.AbortRunningCommand()

        'Get active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        'Create three user commands for the context-sensitive menus
        Dim [error] As dsCreateCommandError_e
        Dim lineUserCmd As UserCommand = dsApp.CreateUserCommand("APIUUID", "TEST_LINE", "^C^C_LINE" & vbLf, "Line", String.Empty, String.Empty, _
         dsUIState_e.dsUIState_Document, [error])
        Dim helpUserCmd As UserCommand = dsApp.CreateUserCommand("APIUUID", "TEST_HELP", "'_HELP" & vbLf, "Help", String.Empty, String.Empty, _
         dsUIState_e.dsUIState_Document, [error])
        Dim patternUserCmd As UserCommand = dsApp.CreateUserCommand("APIUUID", "TEST_PATTERN", "_-PATTERN _L 3 3 5 5" & vbLf & vbLf, "Pattern", String.Empty, String.Empty, _
         dsUIState_e.dsUIState_Document, [error])

        Dim menuItemType As dsMenuItemType_e = dsMenuItemType_e.dsMenuItemType_UserCommand

        'Add default context-sensitive menu item for first user command
        Dim dsDefaultContextMenuItem As ContextMenuItem = dsApp.AddDefaultContextMenu("APIUUID", menuItemType, "Execute line command", lineUserCmd.GetID())

        'Add command context-sensitive menu item for second user command
        Dim dsCommandContextMenuItem As ContextMenuItem = dsApp.AddCommandContextMenu("APIUUID", menuItemType, "Open Help", helpUserCmd.GetID(), "_LINE")

        'Add object context-sensitive menu item for third user command
        Dim dsObjectContextMenuItem As ContextMenuItem = dsApp.AddObjectContextMenu("APIUUID", menuItemType, "Do pattern", patternUserCmd.GetID(), dsObjectType_e.dsLineType)

        MessageBox.Show("Perform steps 7a - 7f.")

    End Sub

End Module
```
