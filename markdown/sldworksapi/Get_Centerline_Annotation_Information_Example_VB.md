---
title: "Get Centerline Annotation Information Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Centerline_Annotation_Information_Example_VB.htm"
---

# Get Centerline Annotation Information Example (VBA)

This example shows how to get information about a centerline annotation, which is stored in its IDisplayData object. You get it using:

- ISelectionManager::GetSelectedObject6
- ICenterline::GetAnnotation
- IAnnotation::GetDisplayData
- IDisplayData::GetLineAtIndex3

```vb
'---------------------------
'
' Preconditions: Drawing document is open
'                and a centerline is selected.
'
'
' Postconditions: None
'
'-----------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swSelAnn As SldWorks.Annotation
Dim swDisplayData As SldWorks.DisplayData
Dim swSelCenterLine As SldWorks.CenterLine
Dim params As Variant
Dim i As Long

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set swSelCenterLine = swSelMgr.GetSelectedObject6(1, 0)

Set swSelAnn = swSelCenterLine.GetAnnotation
Set swDisplayData = swSelAnn.GetDisplayData
Debug.Print "Centerline annotation information: "
For i = 0 To 9
      params = swDisplayData.GetLineAtIndex3(0)
      Debug.Print params(i)
Next i
End Sub
```
