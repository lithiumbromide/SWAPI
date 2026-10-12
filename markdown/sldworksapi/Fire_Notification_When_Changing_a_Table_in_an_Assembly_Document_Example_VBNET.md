---
title: "Fire Notification When Changing a Table in an Assembly Document Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Changing_a_Table_in_an_Assembly_Document_Example_VBNET.htm"
---

# Fire Notification When Changing a Table in an Assembly Document Example (VB.NET)

This example shows how to fire a notification when a table is changed in an assembly document.

```vb
 '---------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document.
 ' 2. Verify that the Tools > Options > System Options >
 '    Stop VSTA debugger on macro exit check box is not selected.
 ' 3. click Insert > Tables > Bill of Materials.
 ' 4. Click OK in the Bill of Materials PropertyManager page and
 '    click OK again.
 ' 5. Run this macro (press F5).
 ' 6. Right-click a column in the table and select Delete > Column.
 '
 ' Postconditions:
  ' 1. Displays a message box informing you that the table was modified.
 '    NOTE: Check the taskbar for the message box if it is not displayed.
 ' 2. Click OK to close the message box.
 ' 3. Stop the debugger.
 '---------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics
 Imports System.Collections

 Partial Class SolidWorksMacro

     Public WithEvents swAssemblyDoc As AssemblyDoc

     Public Sub Main()

         Dim swModel As ModelDoc2
         Dim openAssem As Hashtable

         swModel = swApp.ActiveDoc

         ' Set up event
         swAssemblyDoc = swModel
         openAssem = New Hashtable
         AttachEventHandlers()

     End Sub

     Sub AttachEventHandlers()
         AttachSWEvents()
     End Sub

     Sub AttachSWEvents()
         AddHandler swAssemblyDoc.ModifyTableNotify,  AddressOf  Me.swAssemblyDoc_ModifyTableNotify
     End Sub

     Private Function swAssemblyDoc_ModifyTableNotify(ByVal TableAnnotation As TableAnnotation, ByVal TableType As Integer, ByVal reason As Integer, ByVal RowInfo As Integer, ByVal ColumnInfo As Integer, ByVal DataInfo As String) As Integer
         MsgBox("A table was modified. Title: " & TableAnnotation.Title & ", Type: " & TableType & ", Reason code: " & reason & ", RowInfo: " & RowInfo & ", ColumnInfo: " & ColumnInfo & ", DataInfo: " & DataInfo)
     End Function

     Public swApp As SldWorks

 End Class
```
