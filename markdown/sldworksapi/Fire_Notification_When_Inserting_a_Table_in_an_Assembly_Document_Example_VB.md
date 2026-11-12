---
title: "Fire Notification When Inserting a Table in an Assembly Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Inserting_a_Table_in_an_Assembly_Document_Example_VB.htm"
---

# Fire Notification When Inserting a Table in an Assembly Document Example (VBA)

This example shows how to fire a notification when a table is inserted in an assembly document.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Copy Main to the main module.
' 3. Click Insert > Class Module and copy Class to that module.
' 4. Run this macro (press F5).
' 5. Click Insert > Tables > Bill of Materials.
' 6. Click OK in the Bill of Materials PropertyManager page and
'    click OK again.
'
' Postconditions:
' 1. Displays a message box informing you that a table will be
'    inserted in the assembly.
' 2. Click OK to close the message box.
' 3. Click to place the table.
'---------------------------------------------------------------
'Main
```

```vb
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swAssem As SldWorks.AssemblyDoc
 Dim errorstatus As Long, warningstatus As Long
 Dim swAssemEvents As Class1
Sub main()
Set swApp = Application.SldWorks
 Set swModel = swApp.ActiveDoc
'Set up events
 Set swAssem = swModel
 Set swAssemEvents = New Class1
 Set swAssemEvents.swAssem = swApp.ActiveDoc
End Sub
Back to top
```

###### 'Class

```vb
Option Explicit
Public WithEvents swAssem As SldWorks.AssemblyDoc
Private Function swAssem_InsertTableNotify(ByVal TableAnnotation As SldWorks.ITableAnnotation, ByVal TableType As String, ByVal TemplatePath As String) As Long
     MsgBox "A table will be inserted. Title: " & TableAnnotation.Title & ", Type: " & TableType & ", and Template path: " & TemplatePath
 End Function
```

```
Back to top
```
