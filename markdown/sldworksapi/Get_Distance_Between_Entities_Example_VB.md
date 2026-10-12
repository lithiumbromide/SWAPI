---
title: "Get Distance Between Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Distance_Between_Entities_Example_VB.htm"
---

# Get Distance Between Entities Example (VBA)

This example shows how to get the minimum and maximum distances between face and edge entities.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\multibody\multi_inter.sldprt.
' 2. Open the Immediate window.
' 3. Put your cursor anywhere in the main module in the IDE and press F5.
'
' Postconditions:
' 1. Creates a sketch line that depicts the maximum distance between
'    the face and edge entities.
' 2. Put your cursor over Sketch4 in the FeatureManager design tree and
'    examine the graphics area.
' 3. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-----------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swDoc As SldWorks.ModelDoc2
Dim swSM As SldWorks.SelectionMgr
Dim swFace As SldWorks.Face2
Dim swEdge As SldWorks.Edge
Dim swTop1 As SldWorks.Entity
Dim swTop2 As SldWorks.Entity
Dim bMin As Boolean
Dim retval As Long
Dim dist As Double
Dim varParam As Variant
Dim varPos1 As Variant
Dim varPos2 As Variant
Dim caseType As Integer
Dim boolstatus As Boolean
```

```
Sub main()
    varParam = Empty
```

```
    Set swApp = Application.SldWorks
    Set swDoc = swApp.ActiveDoc
    Set swSM = swDoc.SelectionManager
```

```
    For caseType = 1 To 2
        Select Case caseType
            Case 1
                FaceFaceMinDistance
            Case 2
                FaceEdgeMaxDistance
            Case Else
                Exit Sub
        End Select
    Next
```

```
        Set swTop1 = Nothing
        Set swTop2 = Nothing
        Set swFace = Nothing
        Set swEdge = Nothing
        Set swSM = Nothing
        Set swDoc = Nothing
        Set swApp = Nothing
End Sub
```

```
Sub SetParameterForEdge()
    Dim startPt As Variant
    Dim startVertex As Variant
    Dim endPt As Variant
    Dim endVertex As Variant
    Dim startPara As Variant
    Dim endPara As Variant
```

```
    Set swEdge = swSM.GetSelectedObject6(2, -1)
    Set startVertex = swEdge.GetStartVertex
    startPt = startVertex.GetPoint
    endPt = swEdge.GetEndVertex.GetPoint
    startPara = swEdge.GetParameter(startPt(0), startPt(1), startPt(2))
    endPara = swEdge.GetParameter(endPt(0), endPt(1), endPt(2))
```

```
    Dim paramDl(1) As Double
    paramDl(0) = startPara(0)
    paramDl(1) = endPara(0)
    varParam = paramDl
End Sub
```

```
Sub SetParameterForFace()
    Set swFace = swSM.GetSelectedObject6(2, -1)
    Dim swSurface As SldWorks.Surface
    Set swSurface = swFace.GetSurface
    Dim varBox As Variant
    varBox = swFace.GetBox
    Dim varLowParam As Variant, varHighParam As Variant
    varLowParam = swSurface.ReverseEvaluate(varBox(0), varBox(1), varBox(2))
    varHighParam = swSurface.ReverseEvaluate(varBox(3), varBox(4), varBox(5))
```

```
    Dim paramD2(3) As Double
    paramD2(0) = varLowParam(0)
    paramD2(1) = varLowParam(1)
    paramD2(2) = varHighParam(0)
    paramD2(3) = varHighParam(1)
    varParam = paramD2
End Sub
```

```
Sub CreateLine()
    Dim swSkM As SldWorks.SketchManager
    Dim skSegment As SldWorks.SketchSegment
    Set swSkM = swDoc.SketchManager
    swDoc.Extension.SelectByID2 "Front", "PLANE", 0, 0, 0, False, 0, Nothing, 0
    swSkM.InsertSketch True
    Set skSegment = swSkM.CreateLine(varPos1(0), varPos1(1), varPos1(2), varPos2(0), varPos2(1), varPos2(2))
    swDoc.ClearSelection2 True
    swSkM.InsertSketch True
End Sub
```

```
Sub FaceFaceMinDistance()
    swDoc.ClearSelection
    boolstatus = swDoc.Extension.SelectByID2("", "FACE", -0.07448317477082, -0.04390354307787, 0.08443247713632, False, 0, Nothing, 0)
    boolstatus = swDoc.Extension.SelectByID2("", "FACE", -0.05640517674067, -0.005486808589922, 0.06500000000005, True, 0, Nothing, 0)
    SetParameterForFace
    If (swSM.GetSelectedObjectCount = 2) Then
        Set swTop1 = swSM.GetSelectedObject6(1, -1)
        Set swTop2 = swSM.GetSelectedObject6(2, -1)
        bMin = True
        retval = swTop1.GetDistance(swTop2, bMin, varParam, varPos1, varPos2, dist)
        Debug.Print ("IEntity::GetDistance return value (0 = success; 1 = failure): " & retval)
        Debug.Print ("Face1 coordinate: " & varPos1(0) & "," & varPos1(1) & "," & varPos1(2))
        Debug.Print ("Face2 coordinate: " & varPos2(0) & "," & varPos2(1) & "," & varPos2(2))
        Debug.Print ("Minimum distance between two faces = " & dist * 1000 & " mm")
        CreateLine
    End If
End Sub
```

```
Sub FaceEdgeMaxDistance()
    swDoc.ClearSelection
    boolstatus = swDoc.Extension.SelectByID2("", "FACE", -0.0712080569869, -0.04996892464504, 0.08163440548356, False, 0, Nothing, 0)
    boolstatus = swDoc.Extension.SelectByID2("", "EDGE", -0.04898677039967, 4.196506486664E-04, 0.06476403488529, True, 0, Nothing, 0)
    SetParameterForEdge
    If (swSM.GetSelectedObjectCount = 2) Then
        Set swTop1 = swSM.GetSelectedObject6(1, -1)
        Set swTop2 = swSM.GetSelectedObject6(2, -1)
        bMin = False
        retval = swTop1.GetDistance(swTop2, bMin, varParam, varPos1, varPos2, dist)
        Debug.Print ("IEntity::GetDistance return value (0 = success; 1 = failure): " & retval)
        Debug.Print ("Face coordinate: " & varPos1(0) & "," & varPos1(1) & "," & varPos1(2))
        Debug.Print ("Edge coordinate: " & varPos2(0) & "," & varPos2(1) & "," & varPos2(2))
        Debug.Print ("Maximum distance between face and edge = " & dist * 1000 & " mm")
        CreateLine
    End If
End Sub
```
