---
title: "Get Data for Surface-extend Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Data_for_Surface_Extend_Feature_Example_VB.htm"
---

# Get Data for Surface-extend Feature Example (VBA)

This example shows how to get the data for the selected surface-extend feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document with a surface-extend feature.
 ' 2. Select the surface-extend feature.
 '
 ' Postconditions: Inspect the Immediate window.
 '---------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swFeat                  As SldWorks.Feature
     Dim swSurfExtend            As SldWorks.SurfaceExtendFeatureData

    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swSurfExtend = swFeat.GetDefinition
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "Feature = " & swFeat.Name
     Debug.Print "   Extended distance =  " & swSurfExtend.Distance
     Debug.Print "   Type of surface-extend feature =  " & swSurfExtend.Type
End Sub
```
