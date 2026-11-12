---
title: "Get Data for Surface Revolve Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Data_for_Surface_Revolve_Feature_Example_VBNET.htm"
---

# Get Data for Surface Revolve Feature Example (VB.NET)

This example shows how to get the data for the selected surface revolve feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document with a surface revolve feature.
 ' 2. Select the surface revolve feature.
 '
 ' Postconditions: Inspect the Immediate window.
 '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swFeat As Feature
         Dim swSurfRevolve As SurfRevolveFeatureData

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swSurfRevolve = swFeat.GetDefinition

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("Feature = " & swFeat.Name)
         Debug.Print("   Reverse direction?  " & swSurfRevolve.ReverseDirection)
         Debug.Print("   Type of surface revolve =  " & swSurfRevolve.Type)

     End Sub

     Public swApp As SldWorks

 End  Class
```
