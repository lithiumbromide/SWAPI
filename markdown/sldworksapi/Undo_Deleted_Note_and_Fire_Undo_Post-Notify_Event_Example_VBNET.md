---
title: "Undo Deleted Note and Fire Undo Post-Notify Event Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm"
---

# Undo Deleted Note and Fire Undo Post-Notify Event Example (VB.NET)

## Undo Deleted Note and Fire Undo Pre- and Post-notify Events Example (VB.NET)

This example demonstrates firing Undo pre- and post-notification events in a drawing document.

```vb
'---------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\AutoCAD\7550-021.slddrw.
 '
 ' Postconditions:
 ' 1. Selects and deletes the note in Drawing View1.
 ' 2. Undoes the deleted note.
 ' 3. Fires pre-notification event indicating that an undo action is about to
 '    occur and fires post-notification event indicating that an undo
 '    action occurred.
 ' 4. Click OK to close each message box.
 '
 ' NOTE: Because the drawing is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Collections
Imports System.Windows.Forms

Partial Class SolidWorksMacro

    Public WithEvents swDrawing As DrawingDoc

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim boolstatus As Boolean
        Dim openDrawing As Hashtable

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension

        ' Event notification
        swDrawing = swModel
        openDrawing = New Hashtable
        AttachEventhandlers()

        ' Activate the drawing view that contains
        ' the note you want to delete
        boolstatus = swDrawing.ActivateView("Drawing View3")
        boolstatus = swModelDocExt.SelectByID2("DetailItem77@Drawing View3", "NOTE", 0.3058741216774, 0.1870419466786, 0, False, 0, Nothing, 0)

        ' Delete the selected note
        swModel.EditDelete()

        ' Undo deletion of note
        ' Pre- and post-notifications fired
        swModel.EditUndo2(1)

        ' Rebuild the drawing
        swModel.ForceRebuild3(True)

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swDrawing.UndoPostNotify, AddressOf Me.swDrawing_UndoPostNotify
        AddHandler swDrawing.UndoPreNotify, AddressOf Me.swDrawing_UndoPreNotify

    End Sub

    Private Function swDrawing_UndoPostNotify() As Integer
        ' Display message after Undo
        ' NOTE: Because the message box may be displayed
        ' behind an opened window, you might not see it.
        ' If so, then check the Taskbar.
        MsgBox("An undo post-notification event has been fired.")
    End Function

    Private Function swDrawing_UndoPreNotify() As Integer
        ' Display message after Undo
        ' NOTE: Because the message box may be displayed
        ' behind an opened window, you might not see it.
        ' If so, then check the Taskbar.
        MsgBox("An Undo pre-notification event has been fired.")
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
