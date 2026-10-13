---
title: "Fire Events When PropertyManager Page Opened and Canceled Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VB.htm"
---

# Fire Events When PropertyManager Page Opened and Canceled Example (VBA)

This example shows how to get the SOLIDWORKS command ID, PropertyManager title, and whether the user interface is active. Events are fired before the PropertyManager page is opened and when it is canceled.

```
'------------------------------------------
' Preconditions:
' 1. Copy Main into the macro.
' 2. Click Insert > Class Module and copy Class1
'    into the module.
' 2. Add a reference to SOLIDWORKS <version>
'    commands type library.
' 3. Open the Immediate window.
' 4. Verify that the part to open exists.
'
' Postconditions:
' 1. Opens the part.
' 2. Fires the CommandOpenPreNotify event; click
'    OK to close the message box.
' 3. Opens the Fillet PropertyManager page.
' 4. Gets the title of the PropertyManager page, whether the
'    user interface is active, and whether the command ID
'    is a fillet.
' 5. Click X on the Fillet PropertyManager
'    page to cancel it.
' 6. Fires the CommandCloseNotify event; click OK
'    to close the message box.
' 7. Examine the Immediate window.
'--------------------------------------------
'Main
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim modelName As String
Dim errors As Long
Dim warnings As Long
Dim commandID As Long
Dim pmpTitle As String
Dim isUIActive As Boolean
Dim swAppEvents As New Class1
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
```

```
' Set up event
Set swAppEvents.swApp = swApp
```

```
' Open the model
modelName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
Set swModel = swApp.OpenDoc6(modelName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
Set swModelDocExt = swModel.Extension
```

```
' Open the Fillet PropertyManager Page,
' which causes the CommandOpenPreNotify event
' to fire
swModelDocExt.RunCommand swCommands_Fillet, "Fillet"
```

```
' Get the command ID if the command is a fillet,
' get the PropertyManager page title if one is active,
' and get whether the user interface is active
swApp.GetRunningCommandInfo commandID, pmpTitle, isUIActive
If pmpTitle <> "" Then Debug.Print "Title of PropertyManager page: " & pmpTitle
Debug.Print "Is user interface active? " & isUIActive
If (commandID = 9) Then
    Debug.Print "Command ID: " & "swCommands_Fillet"
Else
    Debug.Print "Command ID: " & "Not a fillet."
End If
```

```
End Sub
```

Class1

```
Option Explicit
```

```
Public WithEvents swApp As SldWorks.SldWorks
```

```
Private Function swApp_CommandOpenPreNotify(ByVal command As Long, ByVal userCommand As Long) As Long
    'Send message when the Fillet PropertyManager page is about to open
    If (command = swCommands_e.swCommands_Fillet) Then MsgBox "Fillet PropertyManager page is about to open."
End Function
```

```
Private Function swApp_CommandCloseNotify(ByVal command As Long, ByVal reason As Long) As Long
    'Send message because the Fillet PropertyManager page was canceled by clicking the X button
    MsgBox "Fillet PropertyManager page was canceled."
End Function
```
