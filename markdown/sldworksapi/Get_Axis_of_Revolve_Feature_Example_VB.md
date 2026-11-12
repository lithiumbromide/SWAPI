---
title: "Get Axis of Revolve Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Axis_of_Revolve_Feature_Example_VB.htm"
---

# Get Axis of Revolve Feature Example (VBA)

This example shows how to get the type of axis of revolution and the axis of revolution for a revolve feature.

```vb
'------------------------------------------------
'
' Preconditions:
'         (1) Part document is open.
'         (2) Revolve feature exists and is selected.
'
' Postconditions: The axis of revolution is identified and
          selected, and then deselected.
'
'------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim featdata As SldWorks.RevolveFeatureData2
Dim feat As SldWorks.Feature
Dim skobj As SldWorks.SketchSegment
Dim edgeobj As SldWorks.entity
Dim axisobj As SldWorks.refAxis
Dim boolstatus As Boolean
Dim longstatus As Long

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set feat = swSelMgr.GetSelectedObject5(1)
Set featdata = feat.GetDefinition

boolstatus = featdata.AccessSelections(swModel, Nothing)
longstatus = featdata.GetAxisType
Set skobj = featdata.axis

Select Case longstatus
Case SwConst.swSelSKETCHSEGS
    Set skobj = featdata.axis
    boolstatus = skobj.Select4(False, Nothing)
Case SwConst.swSelDATUMAXES
    Set axisobj = featdata.axis
    Set feat = axisobj
    boolstatus = feat.Select2(False, 0)
Case SwConst.swSelEDGES
    Set edgeobj = featdata.axis
    boolstatus = edgeobj.Select4(False, Nothing)
End Select

featdata.ReleaseSelectionAccess
End Sub
```
