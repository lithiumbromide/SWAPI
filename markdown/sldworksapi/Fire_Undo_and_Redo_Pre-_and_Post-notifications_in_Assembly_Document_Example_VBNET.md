---
title: "Fire Undo and Redo Pre- and Post-notifications in Assembly Document (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_VBNET.htm"
---

# Fire Undo and Redo Pre- and Post-notifications in Assembly Document (VB.NET)

This example shows how to fire Undo and Redo pre- and post-notifications in an assembly document.

```vb
'---------------------------------------------------------------------------
' Preconditions: Open  public_documents\samples\tutorial\smartcomponents\stepped_shaft.sldasm.
 '
 ' Postconditions:
 ' 1. Selects  and hides the base-plate<1> component and
 '    fires pre- and post-notifications indicating that an
 '    Undo has occurred.
 ' 2. Performs a Redo and fires pre- and post-notifications.
 ' 3. Performs another Undo and fires pre- and post-notifications
 '    so that the assembly document returns to its just-opened state.
 ' 4. Click OK to close each message box.
 '
 ' NOTE: Because the assembly is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Collections
Imports System.Windows.Forms
Partial Class SolidWorksMacro
    Public WithEvents swAssemblyDoc As AssemblyDoc
    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim boolstatus As Boolean
        Dim openAssembly As Hashtable

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension

        ' Event notification
        swAssemblyDoc = swModel
        openAssembly = New Hashtable
        AttachEventHandlers()

        ' Select a component and hide it
        boolstatus = swModelDocExt.SelectByID2("base_plate-1@stepped_shaft", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swModel.HideComponent2()
        swModel.ClearSelection2(True)

        ' Undo hiding of the component
        ' and fire pre- and post notifications
        swModel.EditUndo2(1)

        ' Redo hiding of the component
        ' and fire pre- and post-notifications
        swModel.EditRedo2(1)

        ' Undo hiding of the component
        ' so that the assembly document
        ' is unchanged
        swModel.EditUndo2(1)

        ' Rebuild model
        swModel.ForceRebuild3(True)
    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swAssemblyDoc.UndoPostNotify, AddressOf Me.swAssembly_UndoPostNotify
        AddHandler swAssemblyDoc.UndoPreNotify, AddressOf Me.swAssembly_UndoPreNotify
        AddHandler swAssemblyDoc.RedoPostNotify, AddressOf Me.swAssembly_RedoPostNotify
        AddHandler swAssemblyDoc.RedoPreNotify, AddressOf Me.swAssembly_RedoPreNotify
    End Sub

    Private Function swAssembly_UndoPostNotify() As Integer
        ' Display message after Undo
        ' NOTE: Because the message box may be displayed
        ' behind an opened window, you might not see it.
        ' If so, then check the Taskbar for it.
        MsgBox("An Undo post-notification event has been fired.")
    End Function

    Private Function swAssembly_UndoPreNotify() As Integer
        ' Display message after Undo
        ' NOTE: Because the message box may be displayed
        ' behind an opened window, you might not see it.
        ' If so, then check the Taskbar for it.
        MsgBox("An Undo pre-notification event has been fired.")
    End Function

    Private Function swAssembly_RedoPostNotify() As Integer
        ' Display message after Redo
        ' NOTE: Because the message box may be displayed
        ' behind an opened window, you might not see it.
        ' If so, then check the Taskbar for it.
        MsgBox("A Redo post-notification event has been fired.")
    End Function

    Private Function swAssembly_RedoPreNotify() As Integer
        ' Display message after Undo
        ' NOTE: Because the message box may be displayed
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
