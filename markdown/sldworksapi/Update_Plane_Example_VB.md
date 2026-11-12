---
title: "Update Plane Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_Plane_Example_VB.htm"
---

# Update Plane Example (VBA)

This example shows how to update a reference plane so that it is parallel to the screen.

```
'---------------------------------------------------------------------------
' Preconditions: Verify that the specified part template exists.
'
' Postconditions:
' 1. Creates Boss-Extrude1 and Plane1.
' 2. Rotates Boss-Extrude1.
' 3. Examine Plane1 in the graphics area.
' 4. Press F5.
' 5. Updates Plane1 so that it is parallel to the screen.
' 6. Examine Plane1 in the graphics area.
'---------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swRefPlane As SldWorks.RefPlane
Dim swModelView As SldWorks.ModelView
Dim swRefPlaneFeatureData As SldWorks.RefPlaneFeatureData
Dim status As Boolean

Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Create Boss-Extrude1 and Plane1
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSketchManager = swModel.SketchManager
    swSketchManager.InsertSketch True
    Set swSketchSegment = swSketchManager.CreateLine(-0.049503, 0.030205, 0#, -0.049503, 0#, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(-0.049503, 0#, 0#, 0#, 0#, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0#, 0#, 0#, 0#, 0.019088, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0#, 0.019088, 0#, -0.03503, 0.037127, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(-0.03503, 0.037127, 0#, -0.049503, 0.030205, 0#)
    swSketchManager.InsertSketch True
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.FeatureExtrusion3(True, False, False, 0, 0, 0.04, 0.01, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
    Set swSelectionMgr = swModel.SelectionManager
    swSelectionMgr.EnableContourSelection = False
    status = swModelDocExt.SelectByID2("", "VERTEX", -3.50298017733792E-02, 3.71273946939409E-02, 0.04, True, 0, Nothing, 0)
    Set swRefPlane = swFeatureManager.InsertRefPlane(4096, 0, 0, 0, 0, 0)
    swModel.ClearSelection2 True
```

```
    'Rotate Boss-Extrude1
    status = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 0, 8.28812132228465E-03
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 0, 8.28812132228465E-03
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 0
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 1.65762426445693E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 8.28812132228465E-03
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 0, 1.65762426445693E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 1.15338191827598E-02, 2.48643639668539E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 1.15338191827598E-02, 3.31524852891386E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 2.48643639668539E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 1.65762426445693E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 0, 2.48643639668539E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 1.65762426445693E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 1.65762426445693E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 4.14406066114233E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 3.31524852891386E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 3.31524852891386E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 1.15338191827598E-02, 5.80168492559925E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 4.14406066114233E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 5.80168492559925E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 0, 6.63049705782772E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 6.63049705782772E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 5.76690959137988E-03, 0.1077455771897
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 0, 9.94574558674158E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 0, 7.45930919005618E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 0, 9.11693345451311E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 0, 8.28812132228465E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 0, 7.45930919005618E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 0, 5.80168492559925E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 0, 2.48643639668539E-02
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 0, 8.28812132228465E-03
    swModel.ClearSelection2 True
```

```
    Stop
    'Examine Plane1
    'Press F5 to continue
```

```
    'Update Plane1 so that it is parallel to the screen
    status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swRefPlaneFeatureData = swFeature.GetDefinition
    swRefPlaneFeatureData.UpdatePlane = True
    swFeature.ModifyDefinition swRefPlaneFeatureData, swModel, Nothing
```

```
End Sub
```
