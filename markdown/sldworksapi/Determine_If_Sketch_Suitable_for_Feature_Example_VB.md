---
title: "Determine if Sketch Suitable for Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Determine_If_Sketch_Suitable_for_Feature_Example_VB.htm"
---

# Determine if Sketch Suitable for Feature Example (VBA)

This example shows how to determine if a sketch is suitable for use in a feature.

**NOTE:** Sketch geometry can be used in a variety of ways in SOLIDWORKS Design. However, not every sketch is suitable for every purpose. For example, (non-thin) extrusions require a closed profile.

```
'------------------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. Select a sketch.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Checks the selected sketch.
' 2. Examine the Immediate window.
'--------------------------------------------------
Option Explicit
```

```
' List of feature types to be used with the ISketch::CheckFeatureUse
Public Enum swSketchCheckFeatureProfileUsage_e
    swSketchCheckFeature_UNSET = 0
    swSketchCheckFeature_BASEEXTRUDE = 1
    swSketchCheckFeature_BASEEXTRUDETHIN = 2
    swSketchCheckFeature_BOSSEXTRUDE = 3
    swSketchCheckFeature_BOSSEXTRUDETHIN = 4
    swSketchCheckFeature_SURFACEEXTRUDE = 5
    swSketchCheckFeature_BASEREVOLVE = 6
    swSketchCheckFeature_BASEREVOLVETHIN = 7
    swSketchCheckFeature_BOSSREVOLVE = 8
    swSketchCheckFeature_BOSSREVOLVETHIN = 9
    swSketchCheckFeature_SURFACEREVOLVE = 10
    swSketchCheckFeature_CUTEXTRUDE = 11
    swSketchCheckFeature_CUTEXTRUDETHIN = 12
    swSketchCheckFeature_CUTREVOLVE = 13
    swSketchCheckFeature_CUTREVOLVETHIN = 14
    swSketchCheckFeature_SWEEPSECTION = 15
    swSketchCheckFeature_SURFACESWEEPSECTION = 16
    swSketchCheckFeature_SWEEPPATHORGUIDE = 17
    swSketchCheckFeature_LOFTSECTION = 18
    swSketchCheckFeature_SURFACELOFTSECTION = 19
    swSketchCheckFeature_LOFTGUIDE = 20
    swSketchCheckFeature_RIBSECTION = 21
    swSketchCheckFeature_SHEETMETAL_BASEFLANGE = 22
End Enum
```

```
' A list of return status values for the ISketch::CheckFeatureUse
Public Enum swSketchCheckFeatureStatus_e
    swSketchCheckFeatureStatus_UnknownError = -1
    swSketchCheckFeatureStatus_OK = 0
    swSketchCheckFeatureStatus_EntXEnt = 1
    swSketchCheckFeatureStatus_EntXSelf = 2
    swSketchCheckFeatureStatus_EntUnspecBad = 3
    swSketchCheckFeatureStatus_ThreeEnts = 4
    swSketchCheckFeatureStatus_EmptySketch = 5
    swSketchCheckFeatureStatus_WrongOpen = 6
    swSketchCheckFeatureStatus_WrongManyContours = 7
    swSketchCheckFeatureStatus_ZeroLengthEnt = 8
    swSketchCheckFeatureStatus_ManyOpen = 9
    swSketchCheckFeatureStatus_NoOpen = 10
    swSketchCheckFeatureStatus_MixedContours = 11
    swSketchCheckFeatureStatus_CturXCtur = 12
    swSketchCheckFeatureStatus_DisjCturs = 13
    swSketchCheckFeatureStatus_OpenWantClosed = 14
    swSketchCheckFeatureStatus_ClosedWantOpen = 15
    swSketchCheckFeatureStatus_DoubleContainment = 16
    swSketchCheckFeatureStatus_MoreThanOneContour = 17
    swSketchCheckFeatureStatus_OneOpenContourExpected = 18
    swSketchCheckFeatureStatus_OneClosedContourExpected = 19
    swSketchCheckFeatureStatus_WantSingleOpenOrMultiClosedDisjoint = 20
    swSketchCheckFeatureStatus_NeedsAxis = 21
    swSketchCheckFeatureStatus_OpenOrUnclear = 22
    swSketchCheckFeatureStatus_ContourIntersectsCenterLine = 23
End Enum
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
    Dim nRetVal As Long
    Dim nOpenCount As Long
    Dim nClosedCount As Long
    Dim i As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swSketch = swFeat.GetSpecificFeature2
```

```
    Debug.Print "Feature = " & swFeat.Name
```

```
    For i = 0 To 22
        nRetVal = swSketch.CheckFeatureUse(i, nOpenCount, nClosedCount)
```

```
        Debug.Print "  FeatCheckType  = " & i
        Debug.Print "    RetVal       = " & nRetVal
        Debug.Print "    OpenCount    = " & nOpenCount
        Debug.Print "    ClosedCount  = " & nClosedCount
        Debug.Print ""
```

```
    Next i
```

```
    Debug.Print ""
```

```
End Sub
```
