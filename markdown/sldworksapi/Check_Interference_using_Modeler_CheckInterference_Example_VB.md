---
title: "Check Interference Using IModeler::CheckInterference Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Check_Interference_using_Modeler_CheckInterference_Example_VB.htm"
---

# Check Interference Using IModeler::CheckInterference Example (VBA)

This example shows how to check interference in an assembly using IModeler::CheckInterference.

```
'---------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\assem20.sldasm.
'
' Postconditions:
' 1. Checks interference between the components is
'    in the context of the assembly.
' 2. Draws lines that outline the faces in block20
'    that are involved in the interference with
'    cylinder20.
' 3. Creates a 3D sketch of the lines.
' 4. Examine the graphics area and FeatureManager design tree.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'---------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
```

```
Sub main()
```

```
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart1 As SldWorks.PartDoc
    Dim swPart2 As SldWorks.PartDoc
    Dim swComponent1 As SldWorks.Component2
    Dim swComponent2 As SldWorks.Component2
    Dim bValue As Boolean
    Dim swBody1 As SldWorks.Body2
    Dim swBody2 As SldWorks.Body2
    Dim swBodyCopy1 As SldWorks.Body2
    Dim swBodyCopy2 As SldWorks.Body2
    Dim vBodies As Variant
    Dim swModeler As SldWorks.Modeler
    Dim vFaces1 As Variant
    Dim vFaces2 As Variant
    Dim vFace As Variant
    Dim swFace As SldWorks.Face2
    Dim vEdges As Variant
    Dim vEdge As Variant
    Dim swEdge As SldWorks.Edge
    Dim swVertex1 As SldWorks.Vertex
    Dim swVertex2 As SldWorks.Vertex
    Dim vPoint1 As Variant
    Dim vPoint2 As Variant
    Dim swTransform1 As SldWorks.MathTransform
    Dim swTransform2 As SldWorks.MathTransform
    Dim swInverseTransform As SldWorks.MathTransform
    Dim swRelativeTransform As SldWorks.MathTransform
    Dim swMathPoint As SldWorks.MathPoint
    Dim swMathPointTransformed As SldWorks.MathPoint
    Dim swMathUtility As SldWorks.MathUtility
    Dim lIdx As Long
    Dim lNumEdges As Long
    Dim lCoord As Long
    Dim lEpsilon As Double
```

```
    lEpsilon = 0.000000001
```

```
    ' Connect to SOLIDWORKS Design
    Set swApp = Application.SldWorks
```

```
    ' Get modeler
    Set swModeler = swApp.GetModeler
```

```
    ' Get Math utility
    Set swMathUtility = swApp.GetMathUtility
```

```
    ' Get active document
    Set swModel = swApp.ActiveDoc
```

```
    ' Select first component
    swModel.ClearSelection2 True
    bValue = swModel.Extension.SelectByID2("block20-1@assem20", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swComponent1 = swModel.SelectionManager.GetSelectedObject6(1, -1)
```

```
    ' Select second component
    swModel.ClearSelection2 True
    bValue = swModel.Extension.SelectByID2("cylinder20-1@assem20", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swComponent2 = swModel.SelectionManager.GetSelectedObject6(1, -1)
```

```
    ' Get transform for each component
    Set swTransform1 = swComponent1.Transform
    Set swTransform2 = swComponent2.Transform
```

```
    ' Get document for each component
    Set swPart1 = swComponent1.GetModelDoc
    Set swPart2 = swComponent2.GetModelDoc
```

```
    ' Get bodies for first component
    vBodies = swComponent1.GetBodies2(swBodyType_e.swSolidBody)
    Set swBody1 = vBodies(0)
```

```
    ' Make a copy for boolean operations
    Set swBodyCopy1 = swBody1.Copy
```

```
    ' Get bodies for second component
    vBodies = swComponent2.GetBodies2(swBodyType_e.swSolidBody)
    Set swBody2 = vBodies(0)
```

```
    ' Make a copy for boolean operations
    Set swBodyCopy2 = swBody2.Copy
```

```
    ' Move bodies to their correct position
```

```
    ' Apply transform
    bValue = swBodyCopy1.ApplyTransform(swTransform1)
    bValue = swBodyCopy2.ApplyTransform(swTransform2)
```

```
    swModel.EditRebuild3
```

```
    bValue = swModeler.CheckInterference(swBodyCopy1, swBodyCopy2, False, vFaces1, vFaces2, vBodies)
```

```
    ' Display edges of block20 that interfere with cylinder20
    If (Not IsEmpty(vFaces1)) Then
        swModel.SetAddToDB True
        swModel.Insert3DSketch2 False
        For Each vFace In vFaces1
            Set swFace = vFace
            vEdges = swFace.GetEdges
            lNumEdges = (UBound(vEdges) - LBound(vEdges) + 1)
            For lIdx = 0 To (lNumEdges - 1)
                Set swEdge = vEdges(lIdx)
                Set swVertex1 = swEdge.GetStartVertex
                Set swVertex2 = swEdge.GetEndVertex
                vPoint1 = swVertex1.GetPoint
                vPoint2 = swVertex2.GetPoint
                For lCoord = 0 To 2
                    If (Abs(vPoint1(lCoord)) < lEpsilon) Then
                        vPoint1(lCoord) = 0#
                    End If
                    If (Abs(vPoint2(lCoord)) < lEpsilon) Then
                        vPoint2(lCoord) = 0#
                    End If
                Next lCoord
                swModel.CreateLine2 vPoint1(0), vPoint1(1), vPoint1(2), vPoint2(0), vPoint2(1), vPoint2(2)
            Next lIdx
        Next vFace
        swModel.Insert3DSketch2 True
        swModel.SetAddToDB False
    End If
```

```
End Sub
```
