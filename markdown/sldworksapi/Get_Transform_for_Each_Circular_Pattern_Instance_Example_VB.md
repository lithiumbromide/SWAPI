---
title: "Get Transform for Each Circular Pattern Instance Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Transform_for_Each_Circular_Pattern_Instance_Example_VB.htm"
---

# Get Transform for Each Circular Pattern Instance Example (VBA)

This example shows how to get the transform for each instance in a circular pattern feature.

```
'-----------------------------------------------
' Preconditions:
' 1. Verify that the specified part exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects the circular-pattern feature.
' 3. Get the number of instances in the circular-pattern
'    feature.
' 4. Gets the transform for each instance
'    in the circular-pattern feature.
' 5. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'-----------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExtension As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swCircularPatternFeatureData As SldWorks.CircularPatternFeatureData
Dim swMathTransform As SldWorks.MathTransform
Dim boolstatus As Boolean
Dim nErrors As Long
Dim nWarnings As Long
Dim NbrInstances As Long
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\introtosw\pressure_plate.sldprt", swDocPART, swOpenDocOptions_Silent, "", nErrors, nWarnings)
    Set swModelDocExtension = swModel.Extension
```

```
    ' Select the circular-pattern feature
    boolstatus = swModelDocExtension.SelectByID2("CirPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swCircularPatternFeatureData = swFeature.GetDefinition
```

```
    ' Get the number of instances in the circular-pattern feature
    NbrInstances = swCircularPatternFeatureData.TotalInstances
    Debug.Print "Number of instances: " & NbrInstances
```

```
    ' Get the transform for each instance
    ' in the circular-pattern feature
    For i = 0 To (NbrInstances - 1)
        Debug.Print "  Processing instance " & (i + 1) & "..."
        Set swMathTransform = swCircularPatternFeatureData.GetTransform(i)
        ' TODO: Do something with the transform
    Next
```

```
End Sub
```
