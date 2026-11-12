---
title: "Fire Undo and Redo Pre- and Post-notifications in Part Document (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Undo_and_Redo_Pre_and_Post-notifications_in_Part_Document_Example_VBNET.htm"
---

# Fire Undo and Redo Pre- and Post-notifications in Part Document (VB.NET)

This example shows how to fire undo and redo pre- and post-notifications in a part document.

```vb
' --------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\cstick.sldprt.
 '
 ' Postconditions:
 ' 1. Creates a circle, undoes it, redoes it, and undoes it again.
 ' 2. Fires a pre- and post-notification and displays a message box
 '    before and after each Undo and Redo.
 ' 3. Click OK to close each message box.
 '
 ' NOTE: Because the part is used elsewhere, do not save changes.
 ' --------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Collections
Partial Class SolidWorksMacro
    Public WithEvents swPart As PartDoc
    Public Sub Main()
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchManager As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim boolstatus As Boolean
        Dim openPart As Hashtable

        swModel = swApp.ActiveDoc

        ' Set up event notification
        swPart = swModel
        openPart = New Hashtable
        AttachEventHandlers()

        ' Create a circle on the
        ' top face of the candlestick
        swModelDocExt = swModel.Extension
        boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00140404215739, 0.2199999999999, 0.001897848026772, False, 0, Nothing, 0)
        swSketchManager = swModel.SketchManager
        swSketchSegment = swSketchManager.CreateCircle(0.0#, 0.0#, 0.0#, 0.01296, -0.006347, 0.0#)

        ' Undo creation of circle
        ' and fire an undo post-notification
        swModel.EditUndo2(1)

        ' Redo creation of circle
        ' and fire a redo post-notification
        swModel.EditRedo2(1)

        ' Undo creation of circle
        ' to leave model document unchanged
        ' and fire an Undo post-notification
        swModel.EditUndo2(1)

        swModel.ClearSelection2(True)
        swModel.ForceRebuild3(True)
    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swPart.UndoPostNotify, AddressOf Me.swPart_UndoPostNotify
        AddHandler swPart.UndoPreNotify, AddressOf Me.swPart_UndoPreNotify
        AddHandler swPart.RedoPostNotify, AddressOf Me.swPart_RedoPostNotify
        AddHandler swPart.RedoPostNotify, AddressOf Me.swPart_RedoPreNotify
    End Sub

    Function swPart_UndoPostNotify() As Integer
        ' Show message after an Undo
        ' Display message after Undo
        ' NOTE: Because the message box might be displayed
        ' behind an opened window, you might not see it.
        ' If so, then check the Taskbar for it.
        MsgBox("An Undo post-notification event has been fired.")
    End Function

    Function swPart_UndoPreNotify() As Integer
        ' Show message after an Undo
        ' Display message after Undo
        ' NOTE: Because the message box might be displayed
        ' behind an opened window, you might not see it.
        ' If so, then check the Taskbar for it.
        MsgBox("An Undo pre-notification event has been fired.")
    End Function

    Function swPart_RedoPostNotify() As Integer
        ' Show message after an Undo
        ' Display message after Undo
        ' NOTE: Because the message box might be displayed
        ' behind an opened window, you might not see it.
        ' If so, then check the Taskbar for it.
        MsgBox("A Redo post-notification event has been fired.")
    End Function

    Function swPart_RedoPreNotify() As Integer
        ' Show message after an Undo
        ' Display message after Undo
        ' NOTE: Because the message box might be displayed
        ' behind an opened window, you might not see it.
        ' If so, then check the Taskbar for it.
        MsgBox("A Redo pre-notification event has been fired.")
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
