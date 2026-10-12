---
title: "Fire Notifications When Renaming Part Document Belonging to Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notifications_When_Renaming_Part_Document_Belonging_to_Assembly_Example_VB.htm"
---

# Fire Notifications When Renaming Part Document Belonging to Assembly Example (VBA)

This example shows how to fire notifications when you:

- are about to rename a part document belonging to an assembly.
- rename the part document.

```
'----------------------------------------------------------------------
' Preconditions:
' 1. Copy and paste Main into your project.
' 2. Insert a class module and copy and paste Class1 into that module.
' 3. Open public_documents\samples\tutorial\EDraw\claw\center.sldprt.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Renames center to centerXXX.
' 2. Fires the PreRenameItemNotify and RenameItemNotify events.
' 3. Examine the FeatureManager design tree and Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------------
'Main
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swPart As SldWorks.PartDoc
Dim swPartEvents As Class1
Dim errors As Long
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    'Set up event
    Set swPart = swModel
    Set swPartEvents = New Class1
    Set swPartEvents.swPart = swApp.ActiveDoc
```

```
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("center.SLDPRT", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    errors = swModelDocExt.RenameDocument("centerXXX")
```

```
End Sub
```

```
'Class1
Option Explicit

Public WithEvents swPart As SldWorks.PartDoc

Private Function swPart_PreRenameItemNotify(ByVal EntityType As Long, ByVal oldName As String, ByVal newName As String) As Long
	Debug.Print "PreRenameItemNotify fired"
End Function

'Fire notification when item is renamed
Public Function swPart_RenameItemNotify(ByVal entType As Long, ByVal oldName As String, ByVal newName As String) As Long
	Debug.Print "RenameItemNotify fired"
End Function
```
