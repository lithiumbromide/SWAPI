---
title: "Fire Notification When Changing a Table in a Drawing Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Changing_a_Table_in_a_Drawing_Document_Example_VB.htm"
---

# Fire Notification When Changing a Table in a Drawing Document Example (VBA)

This example shows how to fire a notification when a table is changed in a drawing document:

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open a drawing document.
' 2. Copy Main to the main module.
' 3. Click Insert > Class Module and copy Class to that module.
' 4. Select a drawing view and click Insert > Tables > Bill of Materials.
' 5. Click OK in the Bill of Materials PropertyManager page.
' 6. Run this macro (press F5).
' 7. Right-click a column and select Delete > Column.
'
' Postconditions:
' 1. Displays a message box informing you that the table was modified.
' 2. Click OK to close the message box.
'---------------------------------------------------------------
```

###### 'Main

```vb
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swDraw As SldWorks.DrawingDoc
 Dim errorstatus As Long, warningstatus As Long
 Dim swDrawEvents As Class1
Sub main()
Set swApp = Application.SldWorks
 Set swModel = swApp.ActiveDoc
'Set up events
 Set swDraw = swModel
 Set swDrawEvents = New Class1
 Set swDrawEvents.swDraw = swApp.ActiveDoc
End Sub
Back to top
```

###### 'Class

```vb
Option Explicit
Public WithEvents swDraw As SldWorks.DrawingDoc

Private Function swDraw_ModifyTableNotify(ByVal TableAnnotation As SldWorks.ITableAnnotation, ByVal TableType As Long, ByVal reason As Long, ByVal RowInfo As Long, ByVal ColumnInfo As Long, ByVal DataInfo As String) As Long
MsgBox "A table was modified. Title: " & TableAnnotation.Title & ", Type: " & TableType & ", Reason code: " & reason & ", RowInfo: " & RowInfo & ", ColumnInfo: " & ColumnInfo & ", DataInfo: " & DataInfo
End Function
```

```
Back to top
```
