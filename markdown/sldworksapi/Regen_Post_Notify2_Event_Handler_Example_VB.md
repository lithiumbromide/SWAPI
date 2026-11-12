---
title: "Fire Assembly Rebuild Events Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Regen_Post_Notify2_Event_Handler_Example_VB.htm"
---

# Fire Assembly Rebuild Events Example (VBA)

This example shows how to handle pre-notification and post-notification events for an assembly, which are fired when the assembly is rebuilt.

```
'----------------------------------------------------------------------------
' Preconditions:
'  1. Copy and paste this code in the main module.
'  2. Click Insert > Class module and copy and paste this code in that module.
'  3. Verify that the specified assembly document to open exists.
'  4. Open the Immediate window.
'
' Postconditions:
'  1. Opens the specified assembly document.
'  2. Inserts a cut-extrude assembly feature.
'  3. Pops up a dialog with the rebuild pre-notification.
'  4. Click OK to close the dialog.
'  5. Rebuilds the assembly.
'  6. Pops up a dialog with the rebuild post-notification.
'  7. Click OK to close the dialog.
'  8. Rolls back the rollback bar and pops up a dialog with the
'     rebuild post-notification.
'  9. Click OK to close the dialog.
' 10. Examine the Immediate window and FeatureManager design tree.
' 11. Click Reset in the IDE to exit the macro.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
' ----------------------------------------------------------------------------
```

```
' Main module code
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssembly as SldWorks.AssemblyDoc
Dim swSketchManager As SldWorks.SketchManager
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.feature
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim fileName As String
Dim errors As Long
Dim warnings As Long
Dim swAssemblyEvents As Class1
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open assembly
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\smartcomponents\stepped_shaft.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    ' Insert a cut-extrude assembly feature
    Set swModelDocExt = swModel.Extension
    swModelDocExt.SelectByID2 "Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0
    swModel.ClearSelection2 True
    Set swSketchManager = swModel.SketchManager
    swSketchManager.InsertSketch True
    Set swSketchSegment = swSketchManager.CreateCircle(-0.016076, -0.532382, 0#, 0.044465, -0.546417, 0#)
    swModel.ClearSelection2 True
    swModelDocExt.SelectByID2 "Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.FeatureCut3(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, True, True, True, True, False, 0, 0, False)
    Set swSelectionMgr = swModel.SelectionManager
    swSelectionMgr.EnableContourSelection = False
    swModel.ClearSelection2 True
```

```
    ' Event notification
    Set swAssembly = swModel
    Set swAssemblyEvents = New Class1
    Set swAssemblyEvents.swAssembly = swApp.ActiveDoc
```

```
    ' Rebuild the model
    swModel.ForceRebuild3 True

    ' Roll back the model
    swFeatureManager.EditRollback swMoveRollbackBarTo_e.swMoveRollbackBarToBeforeFeature, swFeature.Name
```

```
End Sub
```

```
Back to top
```

```
'Class1 module
Option Explicit
```

```
Public WithEvents swAssembly As SldWorks.AssemblyDoc
```

```
Private Function swAssembly_RegenNotify() As Long
' Display message before rebuild
    MsgBox "A rebuild pre-notification event was fired."
End Function
```

```
Private Function swAssembly_RegenPostNotify2(ByVal stopFeature As Object) As Long
' Display message after rebuild
    If Not stopFeature Is Nothing Then
        Dim feature As SldWorks.feature
        Set feature = stopFeature
        Debug.Print "The rollback bar is above " & feature.Name & " in the FeatureManager design tree."
    End if
    MsgBox "A rebuild post-notification event was fired."
End Function
```

```
Back to top
```
