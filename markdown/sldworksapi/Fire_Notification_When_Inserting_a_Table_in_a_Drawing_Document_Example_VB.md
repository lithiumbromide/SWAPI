---
title: "Fire Notification When Inserting a Table in a Drawing Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Inserting_a_Table_in_a_Drawing_Document_Example_VB.htm"
---

# Fire Notification When Inserting a Table in a Drawing Document Example (VBA)

This example shows how to fire a notification when a table is inserted in a drawing document.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open a drawing document.
' 2. Copy Main to the main module.
' 3. Click Insert > Class Module and copy Class to that module.
' 4. Run this macro (press F5).
' 5. Select a drawing view.
' 6. Click Insert > Tables > Bill of Materials.
' 7. Click OK in the Bill of Materials PropertyManager page.
'
' Postconditions:
' 1. Displays a message box informing you that a table will be inserted.
' 2. Click OK to close the message box.
' 3. Click to place the table.
'---------------------------------------------------------------
'Main

Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swDraw As SldWorks.DrawingDoc
 Dim errorstatus As Long, warningstatus As Long
 Dim swDrawEvents As Class1
Sub main()
```

```vb
Set swApp = Application.SldWorks
 Set swModel = swApp.ActiveDoc
'Set up events
 Set swDraw = swModel
 Set swDrawEvents = New Class1
 Set swDrawEvents.swDraw = swApp.ActiveDoc
```

```vb
End Sub
Back to top
'Class
Option Explicit
Public WithEvents swDraw As SldWorks.DrawingDoc
Private Function swDraw_InsertTableNotify(ByVal TableAnnotation As SldWorks.ITableAnnotation, ByVal TableType As String, ByVal TemplatePath As String) As Long
 MsgBox "A table will be inserted. Title: " & TableAnnotation.Title & ", Type: " & TableType & ", and Template path: " & TemplatePath
 End Function
```

```
Back to top
```
