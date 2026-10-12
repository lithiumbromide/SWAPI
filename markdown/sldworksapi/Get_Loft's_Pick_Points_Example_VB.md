---
title: "Get Loft's Pick Points Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Loft's_Pick_Points_Example_VB.htm"
---

# Get Loft's Pick Points Example (VBA)

This example shows how to get the pick points of a loft feature.

```vb
'----------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\floxpress\ball valve\handle.sldprt.
' 2. Select the feature named 1 (a loft feature).
'
' Postconditions: None
'-----------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim swFeatData As SldWorks.LoftFeatureData
Dim swMathPoint As SldWorks.MathPoint
Dim newMathPoint() As SldWorks.MathPoint
Dim pickPointData As Variant
Dim pointVar As Variant
Dim newTopVar As Variant
Dim pointData As Variant
Dim selCount As Long
Dim chainCount As Long
Dim pointCount As Long
Dim numberOfChains As Long
Dim numOfPointInEachChain As Long
Dim newCount As Long
Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
selCount = swSelMgr.GetSelectedObjectCount
If selCount <> 1 Then
    MsgBox ("Select a loft feature and re-run the macro.")
End If

Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
Set swFeatData = swFeat.GetDefinition

' Get the loft's pick points
newCount = 0
pickPointData = swFeatData.PickPoints
numberOfChains = UBound(pickPointData) + 1
Debug.Print ("No. of chains = " & (UBound(pickPointData) + 1))
Debug.Print ""
For chainCount = LBound(pickPointData) To UBound(pickPointData)
    pointData = pickPointData(chainCount)
    numOfPointInEachChain = UBound(pointData) + 1
    ReDim Preserve newMathPoint(0 To ((numberOfChains * numOfPointInEachChain) - 1))
    Debug.Print ("Chain = " & chainCount & ", Number of points = " & (UBound(pointData) + 1))
    For pointCount = LBound(pointData) To UBound(pointData)
        Set swMathPoint = pointData(pointCount)
        pointVar = swMathPoint.ArrayData
        Set newMathPoint(newCount) = swMathPoint
        newMathPoint(newCount).ArrayData = pointVar
        Debug.Print ("X = " & pointVar(0) * 1000 & " Y = " & pointVar(1) * 1000 & " Z = " & pointVar(2) * 1000)
        newCount = newCount + 1
    Next pointCount
    Debug.Print ""
Next chainCount
End Sub
```
