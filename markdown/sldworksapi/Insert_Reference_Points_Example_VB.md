---
title: "Insert Reference Points Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Reference_Points_Example_VB.htm"
---

# Insert Reference Points Example (VBA)

This example shows how to inserts six, evenly spaced referenced points on the selected edge.

```
'-----------------------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. Select an edge.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Creates six evenly spaced reference points on the
'    selected edge.
' 2. Examine the Immediate window, FeatureManager design
'    tree, and graphics area.
'------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swFeatMgr As SldWorks.FeatureManager
    Dim vFeatArr As Variant
    Dim vFeat As Variant
    Dim swFeat As SldWorks.Feature
    Dim swRefPt As SldWorks.RefPoint
    Dim swRefPtData As SldWorks.RefPointFeatureData
    Dim swMathPt As SldWorks.MathPoint
    Dim nStatus As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swFeatMgr = swModel.FeatureManager
    Debug.Print "File = " & swModel.GetPathName
```

```
    ' An edge must be preselected
    vFeatArr = swFeatMgr.InsertReferencePoint(swRefPointAlongCurve, swRefPointAlongCurveEvenlyDistributed, 0#, 6)
    For Each vFeat In vFeatArr
        Set swFeat = vFeat
        Set swRefPt = swFeat.GetSpecificFeature2
        Set swRefPtData = swFeat.GetDefinition
        Set swMathPt = swRefPt.GetRefPoint
        Debug.Print "  " & swFeat.Name
        Debug.Print "    Pt = (" & swMathPt.ArrayData(0) * 1000# & ", " & swMathPt.ArrayData(1) * 1000# & ", " & swMathPt.ArrayData(2) * 1000# & ") mm"
        Debug.Print "    AlongCurveOption   = " & swRefPtData.AlongCurveOption
        Debug.Print "    Distance           = " & swRefPtData.Distance * 1000# & " mm"
        Debug.Print "    Type               = " & swRefPtData.Type
    Next
```

```
End Sub
```
