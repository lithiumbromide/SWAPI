---
title: "Get UV Parameters for XYZ Location Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_UV_Parameters_For_XYZ_Location_Example_VB.htm"
---

# Get UV Parameters for XYZ Location Example (VBA)

This example shows how to use IFace2 and ICurve interfaces to get the UV parameters from the XYZ location.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open  public_documents\samples\tutorial\cosmosxpress\aw_hook.sldprt.
 ' 2. Verify that Tools > System Options > Options ? FeatureManager > Solid Bodies
 '    drop-down selection is Show.
 ' 3. Expand the Solid Bodies folder and select Split Line1.
 ' 4. Open the Immediate window or modify the macro to write the output to a file.
 '
 ' Postconditions: Observe the output in the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFace As SldWorks.Face2
Dim vFaceSelPt As Variant

Sub main()
```

```vb
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Dim pntData(2) As Double
Dim swBody As Body2, procBody As Body2
Set swBody = swSelMgr.GetSelectedObject6(1, -1)
Dim skPnt As SketchPoint
Dim swFeat As Feature

'Set skPnt = swSelMgr.GetSelectedObject6(2, -1)
Set procBody = swBody.GetProcessedBody2(0.5, 0.5)
'Bypass surface split
Set swFace = procBody.GetFirstFace
'Set swFace = swBody.GetFirstFace
While Not swFace Is Nothing
    Dim uvBnds As Variant
    uvBnds = swFace.GetUVBounds()

    Dim UminFace As Double, UmaxFace As Double, VminFace As Double, VmaxFace As Double
    UminFace = uvBnds(0): UmaxFace = uvBnds(1): VminFace = uvBnds(2): VmaxFace = uvBnds(3)

    Dim swSurf As Surface
    Set swSurf = swFace.GetSurface

    uvBnds = swSurf.Parameterization
    Dim UminSurf As Double, UmaxSurf As Double, VminSurf As Double, VmaxSurf As Double
    UminSurf = uvBnds(0): UmaxSurf = uvBnds(1): VminSurf = uvBnds(2): VmaxSurf = uvBnds(3)

    Dim vEdges As Variant
    vEdges = swFace.GetEdges

    Dim i As Integer

    For i = 0 To UBound(vEdges)

        Dim swEdge As Edge
        Set swEdge = vEdges(i)

        Dim swCurve As SldWorks.Curve
        Set swCurve = swEdge.GetCurve()

        Dim vCurveParams As Variant
        vCurveParams = swEdge.GetCurveParams2()

        Dim startParam As Double, endParam As Double, incParam As Double, curParam As Double
        startParam = vCurveParams(6)
        endParam = vCurveParams(7)

        incParam = (endParam - startParam) / 10#
        curParam = startParam

        While curParam < endParam

            Dim vEdgePnt As Variant
            vEdgePnt = swEdge.Evaluate(curParam)

            Dim vSurfRevEval As Variant
            Dim vUVSurfParams As Variant
            Dim UEdge As Double, VEdge As Double

            ' Get the UV parameters for the point using IFace2::ReverseEvaluate
            vUVSurfParams = swFace.ReverseEvaluate(vEdgePnt(0), vEdgePnt(1), vEdgePnt(2))

            If Not IsEmpty(vUVSurfParams) Then
                UEdge = vUVSurfParams(0): VEdge = vUVSurfParams(1)

                Debug.Print "Edge point: " & vbCrLf & "  x: " & vEdgePnt(0) & vbCrLf & "  y: " & vEdgePnt(1) & vbCrLf & "  z: " & vEdgePnt(2)
                Debug.Print "U parameter returned from IFace2::ReverseEvaluate is " & UEdge
                If UEdge > UmaxFace Or UEdge < UminFace Then
                    Debug.Print "U param error face"
                    'Stop
                End If

                Debug.Print "V parameter returned from IFace2::ReverseEvalute is " & VEdge
                If VEdge > VmaxFace Or VEdge < VminFace Then
                    Debug.Print "V param error face"
                    'Stop
                End If
            Else
                Debug.Print "Face reverse evaluate fails - empty data"
            End If

            ' Get the UV parameters for the point using ICurve::ReverseEvaluate
            vUVSurfParams = swSurf.ReverseEvaluate(vEdgePnt(0), vEdgePnt(1), vEdgePnt(2))
            If Not IsEmpty(vUVSurfParams) Then
                UEdge = vUVSurfParams(0): VEdge = vUVSurfParams(1)

                Debug.Print "U parameter returned from ICurve::ReverseEvaluate is " & UEdge
                If UEdge > UmaxFace Or UEdge < UminFace Then
                    Debug.Print "U param error surface"
                    'Stop
                End If

                Debug.Print "V parameter returned from ICurve::ReverseEvaluate is " & VEdge & vbCrLf
                 If VEdge > VmaxFace Or VEdge < VminFace Then
                    Debug.Print "V param error surface"
                    'Stop
                End If

            End If
            curParam = curParam + incParam
        Wend

    Next

    Set swFace = swFace.GetNextFace
Wend
Debug.Print "Complete"
End Sub
```
