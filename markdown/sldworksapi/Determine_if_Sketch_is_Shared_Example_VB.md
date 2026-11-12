---
title: "Determine if Sketch is Shared Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Determine_if_Sketch_is_Shared_Example_VB.htm"
---

# Determine if Sketch is Shared Example (VBA)

This example shows how to determine whether or not a sketch is shared with multiple features.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a part, assembly, or drawing.
' 2. Select a sketch used to create a feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets whether the sketch for the selected
'    feature is shared.
' 2. Gets the children of the feature.
' 3. Examine the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swSketch As SldWorks.Sketch
    Dim i As Long
    Dim bRet As Boolean
    Dim vChildArr As Variant
    Dim vChild As Variant
    Dim swChildFeat As SldWorks.Feature
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swSketch = swFeat.GetSpecificFeature2
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Sketch = " & swFeat.Name
    Debug.Print "    IsShared = " & swSketch.IsShared
```

```
    vChildArr = swFeat.GetChildren: If IsEmpty(vChildArr) Then Exit Sub
    For Each vChild In vChildArr
        Set swChildFeat = vChild
        Debug.Print "      " & swChildFeat.Name & " [" & swChildFeat.GetTypeName & "]"
    Next vChild
```

```
End Sub
```
