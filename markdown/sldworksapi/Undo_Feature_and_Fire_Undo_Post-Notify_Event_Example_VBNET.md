---
title: "Undo Feature and Fire Undo Post-Notify Event Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm"
---

# Undo Feature and Fire Undo Post-Notify Event Example (VB.NET)

## Undo Feature and Fire Undo Post-Notify Event (VB.NET)

This example shows how to fire an undo post-notification in a part.

```vb
 '-----------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\cstick.sldprt.
 '
 ' Postconditions:
 ' 1. Creates a cut-extrude feature on the top face of the
 '    candlestick.
 ' 2. Undoes the cut-extrude feature and fires an undo post-notification.
 ' 3. Click OK to close the message box.
 ' 4. Deletes the cut-extrude sketch and all absorbed features.
 '
 ' NOTE: Because the part is used elsewhere, do not save changes.
 '-----------------------------------------------------------------------

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
        Dim swFeatureManager As FeatureManager
        Dim swFeature As Feature
        Dim boolstatus As Boolean
        Dim openPart As Hashtable

        swModel = swApp.ActiveDoc

        ' Set up event notification
        swPart = swModel
        openPart = New Hashtable
        AttachEventHandlers()

        ' Create a cut-extrude feature on the
        ' top face of the candlestick
        swModelDocExt = swModel.Extension
        boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00140404215739, 0.2199999999999, 0.001897848026772, False, 0, Nothing, 0)
        swSketchManager = swModel.SketchManager
        swSketchSegment = swSketchManager.CreateCircle(0.0#, 0.0#, 0.0#, 0.01296, -0.006347, 0.0#)
        swModel.ClearSelection2(True)
        boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        swFeatureManager = swModel.FeatureManager
        swFeature = swFeatureManager.FeatureCut(True, False, False, 0, 0, 0.01, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, False, True, True)
        swModel.ClearSelection2(True)

        ' Undo the cut-extrude feature
        swModel.EditUndo2(1)

        ' Fire undo notification

        ' Select the circle and delete it
        boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        boolstatus = swModelDocExt.DeleteSelection2(swDeleteSelectionOptions_e.swDelete_Absorbed)

        swModel.ForceRebuild3(True)

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swPart.UndoPostNotify, AddressOf Me.swPart_UndoPostNotify
    End Sub

    Function swPart_UndoPostNotify() As Integer
        ' Show message after undo action occurs
        ' NOTE: Because the message box might be displayed
        ' behind an open window, you might not see it.
        ' If so, then check the Taskbar.
        MsgBox("An undo post-notification event has been fired.")
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
