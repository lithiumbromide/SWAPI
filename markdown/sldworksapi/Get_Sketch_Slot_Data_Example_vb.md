---
title: "Get Sketch Slot Data (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Slot_Data_Example_vb.htm"
---

# Get Sketch Slot Data (VBA)

This example shows how to get sketch slot data.

```vb
'-------------------------------------
' Preconditions: Model document is active and contains
'                a Sketch3 feature with one or more
'                sketch slots.
'
' Postconditions: None
'--------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swPart As SldWorks.PartDoc
Dim longstatus As Long, longwarnings As Long
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketch As SldWorks.Sketch
Dim iSlotCount As Integer
Dim vSketchSlots As Variant
Dim vSketchSlot As Variant
Dim swSketchSlot As SldWorks.SketchSlot
Dim i As Integer
Dim swFeature As SldWorks.Feature
Dim swMathPoint As SldWorks.MathPoint
Dim vArray As Variant
Dim swSketchPoint As SldWorks.SketchPoint
Dim vSketchPtID As Variant

Sub main()

Set swApp = Application.SldWorks

Set swPart = swApp.OpenDoc6("C:\test\Slots.SLDPRT", 1, 0, "", longstatus, longwarnings)
Set swSketchMgr = swPart.SketchManager

Set swFeature = swPart.FeatureByName("Sketch3")
Set swSketch = swFeature.GetSpecificFeature2()
iSlotCount = swSketch.GetSketchSlotCount
Debug.Print "Number of slots: " & iSlotCount
Debug.Print " "
vSketchSlots = swSketch.GetSketchSlots

For Each vSketchSlot In vSketchSlots
    Set swSketchSlot = vSketchSlot
    Debug.Print "Length: " & swSketchSlot.Length
    Debug.Print "Width: " & swSketchSlot.Width
    Debug.Print "LengthType: " & swSketchSlot.LengthType
    Set swMathPoint = swSketchSlot.GetCenterPoint
    vArray = swMathPoint.ArrayData
    Debug.Print "CenterPoint (x,y,z): " & vArray(0) & "," & vArray(1) & "," & vArray(2)
    Set swSketchPoint = swSketchSlot.GetCenterPointHandle
    Debug.Print "CenterPointHandle ISketchPoint(x,y,z): " & swSketchPoint.X & "," & swSketchPoint.Y & "," & swSketchPoint.Z & vbCrLf
    vSketchPtID = swSketchPoint.GetID
    Debug.Print "  IDPt(" & i & ") = [" & vSketchPtID(0) & ", " & vSketchPtID(1) & "]" & vbCrLf
Next

End Sub
```
