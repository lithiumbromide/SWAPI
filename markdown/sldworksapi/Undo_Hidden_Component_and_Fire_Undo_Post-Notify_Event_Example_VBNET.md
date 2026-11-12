---
title: "Undo Hidden Component and Fire Undo Post-Notify Event Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm"
---

# Undo Hidden Component and Fire Undo Post-Notify Event Example (VB.NET)

This example shows how to fire an undo post-notification in an assembly document.

```vb
'--------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\smartcomponents\stepped_shaft.sldasm.
 '
 ' Postconditions:
 ' 1. Selects and hides the base-plate<1> component.
 ' 2. Undoes the hiding of the base-plate<1> component.
 ' 3. Fires a post-notification indicating that an undo action occurred.
 ' 4. Click OK to close the message box.
 '
 ' NOTE: Because the assembly is used elsewhere, do not save changes.
 '--------------------------------------------------------------------------
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
        swModel.EditUndo2(1)

        ' Fire undo post-notification

       ' Rebuild the model
        swModel.ForceRebuild3(True)

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swAssemblyDoc.UndoPostNotify, AddressOf Me.swAssembly_UndoPostNotify
    End Sub

    Private Function swAssembly_UndoPostNotify() As Integer
        'Display message after undo event occurs
        MsgBox("An undo post-notification event has been fired.")
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
