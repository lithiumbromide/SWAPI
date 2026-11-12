---
title: "Fire Assembly Rebuild Events Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Regen_Post_Notify2_Event_Handler_Example_VBNET.htm"
---

# Fire Assembly Rebuild Events Example (VB.NET)

This example shows how to handle pre-notification and post-notification events for an assembly, which are fired when the assembly is rebuilt.

```
'----------------------------------------------------------------------------
' Preconditions:
'  1. Verify that the specified assembly document to open exists.
'  2. Open the Immediate window.
'
' Postconditions:
'  1. Opens the specified assembly document.
'  2. Inserts a cut-extrude assembly feature.
'  3. Pops up a dialog with the rebuild pre-notification.
'  4. Click OK to close the dialog.
'  5. Rebuilds the assembly.
'  6. Pops up a dialog with the rebuild post-notification.
'  7. Click OK to close the dialog.
'  8. Rolls back the rollback bar and pops up a dialog with the rebuild
'     post-notification.
'  9. Click OK to close the dialog.
' 10. Examine the Immediate window and FeatureManager design tree.
' 11. Click Tools > Options > System Options > Stop VSTA debugger on macro exit > OK.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
' ----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swSketchManager As SketchManager
    Dim swModelDocExt As ModelDocExtension
    Dim swSketchSegment As SketchSegment
    Dim swFeatureManager As FeatureManager
    Dim swFeature As Feature
    Dim swSelectionMgr As SelectionMgr
    Dim fileName As String
    Dim errors As Integer
    Dim warnings As Integer
    Public WithEvents swAssembly As AssemblyDoc

    Sub main()

        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, False)

        ' Open assembly
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\smartcomponents\stepped_shaft.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        ' Insert a cut-extrude assembly feature
        swModelDocExt = swModel.Extension
        swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swSketchManager = swModel.SketchManager
        swSketchManager.InsertSketch(True)
        swSketchSegment = swSketchManager.CreateCircle(-0.016076, -0.532382, 0.0#, 0.044465, -0.546417, 0.0#)
        swModel.ClearSelection2(True)
        swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        swFeatureManager = swModel.FeatureManager
        swFeature = swFeatureManager.FeatureCut3(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, False, True, True, True, True, False, 0, 0, False)
        swSelectionMgr = swModel.SelectionManager
        swSelectionMgr.EnableContourSelection = False
        swModel.ClearSelection2(True)

        ' Event notification
        swAssembly = swModel
        AttachEventHandlers()

        ' Rebuild the model
        swModel.ForceRebuild3(True)

        ' Roll back the rollback bar
        swFeatureManager.EditRollback(swMoveRollbackBarTo_e.swMoveRollbackBarToBeforeFeature, swFeature.Name)

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swAssembly.RegenNotify, AddressOf Me.swAssembly_RegenNotify
        AddHandler swAssembly.RegenPostNotify2, AddressOf Me.swAssembly_RegenPostNotify2
    End Sub

    Private Function swAssembly_RegenNotify() As Integer
        ' Display message before rebuild
        MsgBox("A rebuild pre-notification event was fired.")
    End Function

    Private Function swAssembly_RegenPostNotify2(ByVal stopFeature As Object) As Integer
        ' Display message after rebuild
        If Not stopFeature Is Nothing Then
            Dim feature As Feature
            feature = stopFeature
            Debug.Print("The rollback bar is above " & feature.Name & " in the FeatureManager design tree.")
        End If
        MsgBox("A rebuild post-notification event was fired.")
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
