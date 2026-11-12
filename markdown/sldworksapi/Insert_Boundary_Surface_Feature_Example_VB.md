---
title: "Insert Boundary Surface Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Boundary_Surface_Feature_Example_VB.htm"
---

# Insert Boundary Surface Feature Example (VBA)

This example shows how to insert a boundary surface feature.

```vb
'--------------------------------------------------------
 ' Preconditions: Open install_dir\samples\tutorial\cosmosxpress\aw_link.sldprt
 '
 ' Postconditions:
 ' 1. Inserts a boundary surface feature.
 ' 2. Examine the FeatureManager design tree and graphics area.
 '
 ' NOTE: Because the part is used elsewhere, do not save changes.
 '---------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatMgr As SldWorks.FeatureManager
Dim boolstatus As Boolean

Sub main()
```

```vb
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc

swModel.ClearSelection2 True

Set swSelMgr = swModel.SelectionManager
Set swModelDocExt = swModel.Extension

boolstatus = swModelDocExt.SelectByID2("", "EDGE", -9.640234260928E-04, 0.001963504230389, -0.006514073359085, False, 1, Nothing, 0)
boolstatus = swModelDocExt.SelectByID2("", "EDGE", -0.008533278872939, 0.001995620498424, -0.01250000018626, True, 2, Nothing, 0)

Set swFeatMgr = swModel.FeatureManager

swFeatMgr.SetNetBlendCurveData 0, 0, 0, 0, 1, True
swFeatMgr.SetNetBlendDirectionData 0, 32, 0, False, False
swFeatMgr.SetNetBlendCurveData 1, 0, 0, 0, 1, True
swFeatMgr.SetNetBlendDirectionData 1, 32, 0, False, False
swFeatMgr.InsertNetBlend 2, 1, 1, False, 0.0001, False, True, True, True, False, -1, -1, False, -1, False, False, -1, False, False, True
```

```vb
End Sub
```
