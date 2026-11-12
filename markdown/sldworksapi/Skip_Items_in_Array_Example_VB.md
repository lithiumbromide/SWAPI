---
title: "Skip Items in Array Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Skip_Items_in_Array_Example_VB.htm"
---

# Skip Items in Array Example (VBA)

This example shows how to skip items in an array.

```vb
'------------------------------------------------------------
Private Sub CommandButton1_Click()
    Set pSwApp = GetObject("", "SldWorks.Application")
    Set pPart = pSwApp.ActiveDoc
    pPart.SelectByID "LPattern1", "BODYFEATURE", 0, 0, 0
    Set pSelMan = pPart.SelectionManager
    Set pFeature = pSelMan.GetSelectedObject5(1)
    Set pFeatureData = pFeature.GetDefinition
    Dim skip As Variant
    Dim skip2(0 To 3) As Long
    skip = pFeatureData.SkippedItemArray
    skip2(0) = 1
    skip2(1) = 2
    skip2(2) = 3
    skip2(3) = 4
    skip = skip2
    pFeatureData.SkippedItemArray = (skip)
    pFeature.ModifyDefinition pFeatureData, pPart, Nothing
    pFeatureData.ReleaseSelectionAccess
End Sub
```
