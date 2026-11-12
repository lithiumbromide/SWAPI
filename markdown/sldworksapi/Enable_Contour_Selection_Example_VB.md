---
title: "Enable Contour Selection Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Enable_Contour_Selection_Example_VB.htm"
---

# Enable Contour Selection Example (VBA)

This example shows how to select the contour of a sketch region and extrude the selected region.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Ensure that the specified document template exists.
 '
 ' Postconditions: The selected sketch region is extruded.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim vSkLines As Variant
 Dim boolstatus As Boolean
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2014\templates\Part.prtdot", 0, 0, 0)
     Set swModel = swApp.ActiveDoc
     boolstatus = swModel.SetUserPreferenceToggle(swUserPreferenceToggle_e.swDisplayOrigins, True)
     swModel.ClearSelection2 True

    vSkLines = swModel.SketchManager.CreateCornerRectangle(-3.90769010920735E-02, 4.05984975017191E-02, 0, 1.29020232818107E-02, -1.66534302871355E-02, 0)
     swModel.ClearSelection2 True
     vSkLines = swModel.SketchManager.CreateCornerRectangle(-7.51826843645631E-03, 1.56092594749566E-02, 0, 4.87922329685375E-02, -0.041704950991857, 0)
     swModel.ClearSelection2 True
     swModel.SketchManager.InsertSketch True

    ' Enable contour selection
     swModel.SelectionManager.EnableContourSelection = True
     ' Select a contour to extrude
     swModel.Extension.SelectByID2 "Sketch1", "SKETCHREGION", 0, 0.01, 0, True, 4, Nothing, 0
     swModel.FeatureManager.FeatureExtrusion3 True, False, False, 0, 0, 0.01, 0.01, False, False, False, False, 0, 0, False, False, False, False, True, True, True, 0, 0, False
     ' Disable contour selection
     swModel.SelectionManager.EnableContourSelection = False
     swModel.ClearSelection2 True
End Sub
```
