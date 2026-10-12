---
title: "Get Data for Surface Revolve Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Data_for_Surface_Revolve_Feature_Example_VB.htm"
---

# Get Data for Surface Revolve Feature Example (VBA)

This example shows how to get the data for the selected surface revolve feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document with a surface revolve feature.
 ' 2. Select the surface revolve feature.
 '
 ' Postconditions: Inspect the Immediate window.
 '---------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swFeat                  As SldWorks.Feature
     Dim swSurfRevolve            As SldWorks.SurfRevolveFeatureData

    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swSurfRevolve = swFeat.GetDefinition
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "Feature = " & swFeat.Name
     Debug.Print "   Reverse direction?  " & swSurfRevolve.ReverseDirection
     Debug.Print "   Type of surface revolve =  " & swSurfRevolve.Type
End Sub
```
