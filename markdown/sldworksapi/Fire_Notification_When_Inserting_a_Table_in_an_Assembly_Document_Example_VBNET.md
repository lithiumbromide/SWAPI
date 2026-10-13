---
title: "Fire Notification When Inserting a Table in an Assembly Document Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Inserting_a_Table_in_an_Assembly_Document_Example_VBNET.htm"
---

# Fire Notification When Inserting a Table in an Assembly Document Example (VB.NET)

This example shows how to fire a notification when a table is inserted in an assembly document.

```vb
 '---------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document.
 ' 2. Verify that the Tools > Options > System Options >
 '    Stop VSTA debugger on macro exit check box is not selected.
 ' 3. Run this macro (press F5).
 ' 4. Click Insert > Tables > Bill of Materials.
 ' 5. Click OK in the Bill of Materials PropertyManager page and
 '    click OK again.
 '
 ' Postconditions:
 ' 1. Displays a message box informing you that a table will be
 '    inserted in the assembly.
 '    NOTE: Check the taskbar for the message box if you don't
 '    see it.
 ' 2. Click OK to close the message box.
 ' 3. Click to place the table.
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
         AddHandler swAssemblyDoc.InsertTableNotify, AddressOf Me.swAssemblyDoc_InsertTableNotify
     End Sub

     Private Function  swAssemblyDoc_InsertTableNotify(ByVal TableAnnotation As TableAnnotation, ByVal TableType As String, ByVal TemplatePath As String) As  Integer
         MsgBox("A table will be inserted. Title: " & TableAnnotation.Title & ", Type: " & TableType & ", and Template path: " & TemplatePath)
     End Function

     Public swApp As SldWorks

 End  Class
```
