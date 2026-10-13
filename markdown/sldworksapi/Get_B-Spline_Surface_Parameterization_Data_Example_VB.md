---
title: "Get B-Spline Surface Parameterization Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm"
---

# Get B-Spline Surface Parameterization Data Example (VBA)

This example shows how to get B-spline parameterization data for a selected face or surface.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1.  Open public_documents\samples\tutorial\molds\telephone.sldprt.
' 2.  Select a face.
' 3.  Open the Immediate Window.
'
' Postconditions: Examine the Immediate window.
'----------------------------------------------------------------------------

Option Explicit

Sub main()
```

```vb
    Dim swApp                       As SldWorks.SldWorks
     Dim swModel                     As SldWorks.ModelDoc2
     Dim swSelMgr                    As SldWorks.SelectionMgr
     Dim swFace                      As SldWorks.Face2
     Dim swSurf                      As SldWorks.Surface
     Dim swSurfParam                 As SldWorks.SurfaceParameterizationData
     Dim swBSurfParam                As SldWorks.BSurfParamData
     Dim sense                       As Boolean
     Dim UKnots                      As Variant
     Dim VKnots                      As Variant
     Dim vCtrlPts                    As Variant
     Dim i                           As Integer

    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFace = swSelMgr.GetSelectedObject5(1)
     Set swSurf = swFace.GetSurface
     Set swSurfParam = swSurf.Parameterization2
     Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  Surface:"
     Debug.Print " U minimum is: " & swSurfParam.UMin
     Debug.Print " U minimum bound type is: " & swSurfParam.UMinBoundType
     Debug.Print " U maximum is: " & swSurfParam.UMax
     Debug.Print " U maximum bound type is: " & swSurfParam.UMaxBoundType
     Debug.Print " U property count is: " & swSurfParam.UPropertyNumber
     Dim varUProperties As Variant
     varUProperties = swSurfParam.UProperties
     Debug.Print " U properties: "
     For i = 0 To UBound(varUProperties)
         Debug.Print "    " & varUProperties(i)
     Next i

    Debug.Print " V minimum is: " & swSurfParam.VMin
     Debug.Print " V minimum bound type is: " & swSurfParam.VMinBoundType
     Debug.Print " V maximum is: " & swSurfParam.VMax
     Debug.Print " V maximum bound type is: " & swSurfParam.VMaxBoundType
     Debug.Print " V property count is: " & swSurfParam.VPropertyNumber
     Dim varVProperties As Variant
     varVProperties = swSurfParam.VProperties
     Debug.Print " V properties: "
     For i = 0 To UBound(varVProperties)
         Debug.Print "    " & varVProperties(i)
     Next i

    Set swBSurfParam = swSurf.GetBSurfParams3(False, False, swSurfParam, 0.01, sense)

    Debug.Print "U order is: " & swBSurfParam.UOrder
     Debug.Print "V order is: " & swBSurfParam.VOrder
     Debug.Print " Control point column count is: " & swBSurfParam.ControlPointColumnCount
     Debug.Print " Control point row count is: " & swBSurfParam.ControlPointRowCount
     Debug.Print " Control point dimension is: " & swBSurfParam.ControlPointDimension
     Debug.Print " U periodicity is: " & swBSurfParam.UPeriodicity
     Debug.Print " V periodicity is: " & swBSurfParam.VPeriodicity

    UKnots = swBSurfParam.UKnots
     Debug.Print "Knot vector in the U direction: "
     For i = 0 To UBound(UKnots)
         Debug.Print UKnots(i)
     Next i
     VKnots = swBSurfParam.VKnots
     Debug.Print "Knot vector in the V direction: "
     For i = 0 To UBound(VKnots)
         Debug.Print VKnots(i)
     Next i

    ' Get control points in row = 2, column = 3 of the control point matrix
     vCtrlPts = swBSurfParam.GetControlPoints(2, 3)
     Debug.Print "Control point at row=2 and column=3: "
     For i = 0 To UBound(vCtrlPts)
         Debug.Print vCtrlPts(i)
     Next i

 End Sub
```
