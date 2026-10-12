---
title: "Create Cut Extrude in Sheet Metal Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Cut_Extrude_in_Sheet_Metal_Part_Example_VB.htm"
---

# Create Cut Extrude in Sheet Metal Part Example (VBA)

This example shows how to create an optimized, normal, cut extrude in a sheet metal part.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Verify that the sheet metal part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the sheet metal part.
' 2. Selects a face.
' 3. Sketches a circle on the selected face.
' 4. Creates Cut-Extrude2, which is an optimized, normal, cut
'    extrude.
' 5. Examine the FeatureManager design tree, graphics area,
'    Immediate window.
'
' NOTE: Because the part document is used elsewhere, do not save
' changes.
'--------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swExtrudeFeatureData as SldWorks.ExtrudeFeatureData2
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\2012-sm.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

    'Select a face
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByRay(-2.87275955400048E-02, 3.01558252805876E-02, 5.09460972091347E-03, 0.369531106281609, -0.495005022745071, -0.786394804756136, 1.15698538052806E-03, 2, False, 0, 0)

    'Sketch a circle
    Set swSketchManager = swModel.SketchManager
    Set swSketchSegment = swSketchManager.CreateCircle(0#, 0#, 0#, 0.004122, -0.003029, 0#)

    'Create an optimized, normal, cut extrude
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.FeatureCut4(True, False, False, 1, 0, 0.01, 0.01, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, True, True, False, 0, 0, False, True)

    swModel.ClearSelection2 True
```

```
    Set swExtrudeFeatureData = swFeature.GetDefinition
    Debug.Print "Normal cut? " & swExtrudeFeatureData.NormalCut
    Debug.Print "Geometry optimized? " & swExtrudeFeatureData.OptimizeGeometry
```

```
End Sub
```
