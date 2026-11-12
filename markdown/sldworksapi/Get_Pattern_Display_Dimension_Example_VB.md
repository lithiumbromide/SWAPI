---
title: "Get Pattern Display Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Pattern_Display_Dimension_Example_VB.htm"
---

# Get Pattern Display Dimension Example (VBA)

This example shows how to get the display dimensions for various pattern properties of a linear pattern.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part with a linear pattern.
 ' 2. Select the linear pattern feature.
 ' 3. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim selMan As SldWorks.SelectionMgr
 Dim feat As SldWorks.Feature
 Dim dispDim As SldWorks.DisplayDimension
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks

    Set Part = swApp.ActiveDoc
     Set selMan = Part.SelectionManager
     Set feat = selMan.GetSelectedObject6(1, -1)
     Debug.Print " Feature = " & feat.Name

    Set dispDim = feat.GetDisplayDimension(swFeatureDimensionParameter_e.swPatternInstanceCount1)
     Debug.Print " Instance count 1 display dimension = " & dispDim.GetNameForSelection
     Debug.Print " Type of dimension as defined in swDimensionType_e = " & dispDim.Type2
     Set dispDim = feat.GetDisplayDimension(swFeatureDimensionParameter_e.swPatternSpacing1)
     Debug.Print " Spacing 1 display dimension = " & dispDim.GetNameForSelection
     Debug.Print " Type of dimension as defined in swDimensionType_e = " & dispDim.Type2

End Sub
```
