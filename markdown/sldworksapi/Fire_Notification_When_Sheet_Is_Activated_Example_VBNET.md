---
title: "Fire Notification When Activating a Sheet Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Sheet_Is_Activated_Example_VBNET.htm"
---

# Fire Notification When Activating a Sheet Example (VB.NET)

This example shows how to fire a notification when a sheet is activated in a drawing document.

```
'-------------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
'
' Postconditions:
' 1. Displays a message box informing you that a sheet is about to be
'    activated.
' 2. Click OK to close the message box.
'
' NOTES:
' * The IDrawingDoc ActivateSheetPostNotify event only fires
'   when a sheet is interactively activated in SOLIDWORKS; this event
'   does not fire when a sheet is activated through the API.
' * Because the drawing is used elsewhere, do not save changes.
'--------------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Windows.Forms
Imports System.Collections
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public WithEvents swDrawingDoc As DrawingDoc

    Dim swModel As ModelDoc2
    Dim status As Boolean

    Sub Main()

        swModel = swApp.ActiveDoc

        'Set up events
        swDrawingDoc = swModel
        AttachEventHandlers()

        ' Activate Sheet4
        status = swDrawingDoc.ActivateSheet("Sheet4")

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swDrawingDoc.ActivateSheetPreNotify, AddressOf Me.swDraw_ActivateSheetPreNotify
    End Sub

    Function swDraw_ActivateSheetPreNotify(ByVal SheetName As String) As Integer
        MsgBox("A sheet is about to be activated.")
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
