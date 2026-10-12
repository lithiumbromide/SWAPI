---
title: "Fire Notification When Inserting a Table in a Drawing Document Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Inserting_a_Table_in_a_Drawing_Document_Example_VBNET.htm"
---

# Fire Notification When Inserting a Table in a Drawing Document Example (VB.NET)

This example shows how to fire a notification when a table is inserted in a drawing document.

```vb
 '---------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing document.
 ' 2. Verify that the Tools > Options > System Options >
 '    Stop VSTA debugger on macro exit check box is not selected.
 ' 3. Run this macro (press F5).
 ' 4. Select a drawing view.
 ' 5. Click Insert > Tables > Bill of Materials.
 ' 6. Click OK in the Bill of Materials PropertyManager page.
 '
 ' Postconditions:
 ' 1. Displays a message box informing you that a table will be inserted.
 ' 2. Click OK to close the message box.
 '    NOTE: Check the taskbar for the message box if you don't
 '    see it.
 ' 3. Click to place the table.
 ' 4. Stop the debugger.
 '---------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics
 Imports System.Collections

 Partial Class SolidWorksMacro

     Public WithEvents swDrawingDoc As DrawingDoc

     Public Sub Main()

         Dim swModel As ModelDoc2
         'Dim openDraw As Hashtable

         swModel = swApp.ActiveDoc

         ' Set up event
         swDrawingDoc = swModel
         'openDraw = New Hashtable
         AttachEventHandlers()

     End Sub

     Sub AttachEventHandlers()
         AttachSWEvents()
     End Sub

     Sub AttachSWEvents()
         AddHandler swDrawingDoc.InsertTableNotify,  AddressOf  Me.swDrawingDoc_InsertTableNotify
     End Sub

     Private Function swDrawingDoc_InsertTableNotify(ByVal TableAnnotation As TableAnnotation, ByVal TableType As String, ByVal TemplatePath As String) As Integer
         MsgBox("A table will be inserted. Title: " & TableAnnotation.Title & ", Type: " & TableType & ", and Template path: " & TemplatePath)
     End Function

     Public swApp As SldWorks

 End Class
```
