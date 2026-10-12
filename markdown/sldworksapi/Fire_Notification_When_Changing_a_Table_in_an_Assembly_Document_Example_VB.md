---
title: "Fire Notification When Changing a Table in an Assembly Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Changing_a_Table_in_an_Assembly_Document_Example_VB.htm"
---

# Fire Notification When Changing a Table in an Assembly Document Example (VBA)

This example shows how to fire a notification when a table is changed in an assembly document.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Copy Main to the main module.
' 3. Click Insert > Class Module and copy Class to that module.
' 4. Click Insert > Tables > Bill of Materials.
' 5. Click OK in the Bill of Materials PropertyManager page
'    click OK again.
' 6. Run this macro (press F5).
' 7. Right-click a column in the table and select Delete > Column.
'
' Postconditions:
' 1. Displays a message box informing you that the table was modified.
' 2. Click OK to close the message box.
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
```

```vb
Set swApp = Application.SldWorks
 Set swModel = swApp.ActiveDoc
'Set up events
 Set swAssem = swModel
 Set swAssemEvents = New Class1
 Set swAssemEvents.swAssem = swApp.ActiveDoc
```

```vb
End Sub
Back to top
```

###### 'Class

```vb
Option Explicit
Public WithEvents swAssem As SldWorks.AssemblyDoc

Private Function swAssem_ModifyTableNotify(ByVal TableAnnotation As SldWorks.ITableAnnotation, ByVal TableType As Long, ByVal reason As Long, ByVal RowInfo As Long, ByVal ColumnInfo As Long, ByVal DataInfo As String) As Long
 MsgBox "A table was modified. Title: " & TableAnnotation.Title & ", Type: " & TableType & ", Reason code: " & reason & ", RowInfo: " & RowInfo & ", ColumnInfo: " & ColumnInfo & ", DataInfo: " & DataInfo
 End Function
```

```
Back to top
```
