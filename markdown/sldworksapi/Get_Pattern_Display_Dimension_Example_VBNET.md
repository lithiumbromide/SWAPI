---
title: "Get Pattern Display Dimension Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Pattern_Display_Dimension_Example_VBNET.htm"
---

# Get Pattern Display Dimension Example (VB.NET)

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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim selMan As SelectionMgr
     Dim feat As Feature
     Dim dispDim As DisplayDimension

     Sub main()

         Part = swApp.ActiveDoc
         selMan = Part.SelectionManager
         feat = selMan.GetSelectedObject6(1, -1)
         Debug.Print(" Feature = " & feat.Name)

         dispDim = feat.GetDisplayDimension(swFeatureDimensionParameter_e.swPatternInstanceCount1)
         Debug.Print(" Instance count 1 display dimension = " & dispDim.GetNameForSelection)
         Debug.Print(" Type of dimension as defined in swDimensionType_e = " & dispDim.Type2)
         dispDim = feat.GetDisplayDimension(swFeatureDimensionParameter_e.swPatternSpacing1)
         Debug.Print(" Spacing 1 display dimension = " & dispDim.GetNameForSelection)
         Debug.Print(" Type of dimension as defined in swDimensionType_e = " & dispDim.Type2)

     End Sub

     Public swApp As SldWorks

 End  Class
```
