---
title: "Fire Notification When Activating a Sheet Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Sheet_is_Activated_Example_VB.htm"
---

# Fire Notification When Activating a Sheet Example (VBA)

This example shows how to fire a notification when a sheet is activated in a drawing document.

```vb
 '---------------------------------------------------------------
 ' Preconditions:
 ' 1. Copy Main into the macro.
 ' 2. Click Insert > Class Module and copy Class1 into that
 '    module.
 ' 3. Open a drawing with two or more sheets.
 '
 ' Postconditions:
 ' 1. Click an inactive sheet's tab to activate it.
 ' 2. Displays a message box informing you that a sheet is about
 '    to be activated.
 ' 3. Click OK to close the message box.
 ' 4. Displays a message box informing you that a sheet was activated.
 ' 5. Click OK to close the message box.
 '---------------------------------------------------------------
 'Main
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swDraw As SldWorks.DrawingDoc
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
```

###### 'Class1

```vb
Option Explicit
Public WithEvents swDraw As SldWorks.DrawingDoc
Private Function swDraw_ActivateSheetPreNotify(ByVal SheetName As String) As Long
     MsgBox "A sheet is about to be activated."
 End Function
Private Function swDraw_ActivateSheetPostNotify(ByVal SheetName As String) As Long
     MsgBox "A sheet was activated."
 End Function
```

[Back to top](#Top)
