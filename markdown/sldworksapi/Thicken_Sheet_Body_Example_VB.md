---
title: "Thicken Sheet Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Thicken_Sheet_Body_Example_VB.htm"
---

# Thicken Sheet Body Example (VBA)

This example shows how to thicken a sheet (surface) body.

```
'--------------------------------------------------
' Preconditions:
' 1. Open a part that contains a sheet body.
' 2. Select the sheet body in the Surface Bodies folder.
'
' Postconditions:
' 1. Thickens the sheet body and creates a temporary
'    thickened body.
' 2. Examine the FeatureManager design tree and
'    graphics area.
'-------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
```

```
Sub main()
```

```
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim swBody As SldWorks.Body2
    Dim swFace As SldWorks.Face2
    Dim swOriginalSheetBody As SldWorks.Body2
    Dim swThickenedbody As SldWorks.Body2
    Dim swModeler As SldWorks.Modeler
    Dim dThickness As Double
    Dim vSheets As Variant
    Dim lOptions As Long
    Dim lErrors As Long
    Dim lNumSheets As Long
    Dim aBodies(0) As SldWorks.Body2
    Dim vBodies As Variant
    Dim swFeature As SldWorks.Feature
```

```
    ' Thickness
    dThickness = 0.01
```

```
    ' Connect to SOLIDWORKS Design
    Set swApp = Application.SldWorks
```

```
    ' Get modeler
    Set swModeler = swApp.GetModeler
    Debug.Assert Not swModeler Is Nothing
```

```
    ' Get active document
    Set swModel = swApp.ActiveDoc
```

```
    ' Cast down to part
    Set swPart = swModel
```

```
    ' Get the selected sheet body
    Set swBody = swModel.SelectionManager.GetSelectedObject6(1, -1)
```

```
    ' Make a copy, so you can later sew together with other sheets
    Set swOriginalSheetBody = swBody.Copy
    Set swThickenedbody = swModeler.ThickenSheet(swOriginalSheetBody, dThickness, swThickenDirection_Side1)
    Debug.Assert (Not (swThickenedbody Is Nothing))
    Debug.Assert (swThickenedbody.GetType = swBodyType_e.swSolidBody)
    Set aBodies(0) = swThickenedbody
    vBodies = aBodies
```

```
    ' Turn temporary body into a feature
    Set swFeature = swPart.CreateFeatureFromBody3(vBodies(0), False, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck)
```

```
    swModel.EditRebuild3
```

```
End Sub
```
