---
title: "Get Curves that Form Outline of Bodies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Curves_that_Form_Outline_of_Bodies_Example_VB.htm"
---

# Get Curves that Form Outline of Bodies Example (VBA)

This example shows how to get the curves that form the outline of a body and create a 3D sketch using those curves.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Copy and paste Main into your macro.
' 2. Click Insert > Class Module and copy and paste OutlineCurve
'    in the class module.
'    a. Click View > Project Explorer.
'    b. Click View > Properties Window.
'    c. Type OutlineCurve in (Name) in the Properties window.
' 3. Click Insert > Class Module and copy and paste Outline in
'    the class module.
'    a. Click View > Properties Window.
'    b. Type Outline in (Name) in the Properties window.
' 4. Add a reference to the Microsoft Scripting Runtime (click
'    Tools > References > Microsoft Scripting Runtime > OK).
' 5. Open a part document containing at least one body.
'
' Postconditions:
' 1. Creates a 3D sketch using the outlines of the curves
'    in the bodies.
' 2. Examine the graphics area, FeatureManager design tree,
'    and the graphics area.
'----------------------------------------------------------------
'Main
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
```

```
Sub main()
```

```
    Dim swModel               As SldWorks.ModelDoc2
    Dim swPart                As SldWorks.PartDoc
    Dim swModeler             As SldWorks.Modeler
    Dim swMathUtility         As SldWorks.MathUtility
    Dim vBodies               As Variant
    Dim swBody                As SldWorks.Body2
    Dim aVector(2)            As Double
    Dim vVector               As Variant
    Dim swVector              As SldWorks.MathVector
    Dim dTolerance            As Double
    Dim vCurves               As Variant
    Dim vTopologicalEntities  As Variant
    Dim vIndices              As Variant
    Dim lNumCurves            As Long
    Dim oOutlineCurve         As OutlineCurve
    Dim oOutline              As Outline
    Dim dictOutLines          As Dictionary
    Dim lOutLineIdx           As Long
    Dim lIdx                  As Long
    Dim vOutline              As Variant
    Dim vOutlineCurve         As Variant
    Dim swEntity              As SldWorks.Entity
    Dim swEdge                As SldWorks.Edge
    Dim swFace                As SldWorks.Face2
    Dim bValue                As Boolean
    Dim swCurve               As SldWorks.Curve
    Dim dStartParam           As Double
    Dim dEndParam             As Double
    Dim bIsClosed             As Boolean
    Dim bIsPeriodic           As Boolean
    Dim vStartPoint           As Variant
    Dim vEndPoint             As Variant
    Dim vCircleParams         As Variant
    Dim aCenterPoint(2)       As Double
    Dim vTessPts              As Variant
    Dim nChordTol             As Double
    Dim nLengthTol            As Double
    Dim swSketchSegment       As SldWorks.SketchSegment
    Dim swSketchManager       As SldWorks.SketchManager
    Dim aColours(5)           As Long
    Dim swObject              As Object
    Dim nbrTessPoints As Long
```

```
    nChordTol = 0.00000001
    nLengthTol = 0.0000000000001
    aColours(0) = RGB(255, 0, 0)
    aColours(1) = RGB(0, 255, 0)
    aColours(2) = RGB(0, 0, 255)
    aColours(3) = RGB(255, 255, 0)
    aColours(4) = RGB(255, 0, 255)
    aColours(5) = RGB(0, 255, 255)
```

```
    Set swApp = Application.SldWorks
    Set swModeler = swApp.GetModeler
    Set swMathUtility = swApp.GetMathUtility
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Set swSketchManager = swModel.SketchManager
```

```
    vBodies = swPart.GetBodies2(swBodyType_e.swSolidBody, False)
```

```
    ' Look along the z-axis in the negative direction;
    ' this corresponds to the Front view
    aVector(0) = 0#
    aVector(1) = 0#
    aVector(2) = -1#
    vVector = aVector
    Set swVector = swMathUtility.CreateVector((vVector))
```

```
    ' Default value
    dTolerance = 0.00001
```

```
    lNumCurves = swModeler.GetBodyOutline2((vBodies), swVector, dTolerance, False, vCurves, vTopologicalEntities, vIndices)
    If (lNumCurves > 0) Then
        Debug.Print "#curves = " & lNumCurves
        Set dictOutLines = New Dictionary
        lOutLineIdx = -1
        For lIdx = 0 To (lNumCurves - 1)
            If (vIndices(lIdx) <> lOutLineIdx) Then
                lOutLineIdx = vIndices(lIdx)
                Set oOutline = New Outline
                oOutline.lIndex = lOutLineIdx
                dictOutLines.Add lOutLineIdx, oOutline
            End If
            Set oOutlineCurve = New OutlineCurve
            Set oOutlineCurve.swCurve = vCurves(lIdx)
            Set oOutlineCurve.swEntity = vTopologicalEntities(lIdx)
            Set swObject = vTopologicalEntities(lIdx)
            If (TypeOf swObject Is SldWorks.Edge) Then
                ' HERE: real edge
                oOutlineCurve.nType = swSelEDGES
            End If
            Set swObject = vTopologicalEntities(lIdx)
            If (TypeOf swObject Is SldWorks.Face2) Then
                ' HERE: silhouette edge
                oOutlineCurve.nType = swSelFACES
            End If
            oOutline.dictCurves.Add oOutlineCurve, oOutlineCurve
        Next lIdx
```

```
        swModel.SetAddToDB True
        swModel.SetDisplayWhenAdded False
        swModel.Insert3DSketch2 False
```

```
        For Each vOutline In dictOutLines.Items
            swModel.ClearSelection2 True
            Set oOutline = vOutline
            Debug.Print "Outline " & oOutline.lIndex
            Debug.Print "  #curves = " & oOutline.dictCurves.Count
            For Each vOutlineCurve In oOutline.dictCurves.Items
                Set oOutlineCurve = vOutlineCurve
                Set swCurve = oOutlineCurve.swCurve
                Debug.Print "    type    = " & swCurve.Identity
                Debug.Print "    trimmed = " & swCurve.IsTrimmedCurve
                Set swEntity = oOutlineCurve.swEntity
                bValue = swEntity.Select4(True, Nothing)
```

```
                ' Draw some of the curves to show where they live in 3D space
                bValue = swCurve.GetEndParams(dStartParam, dEndParam, bIsClosed, bIsPeriodic)
                vStartPoint = swCurve.Evaluate(dStartParam)
                vEndPoint = swCurve.Evaluate(dEndParam)
                vTessPts = swCurve.GetTessPts(nChordTol, nLengthTol, (vStartPoint), (vEndPoint))
                For lIdx = 0 To nbrTessPoints Step 3
                    Set swSketchSegment = swSketchManager.CreateLine(vTessPts(lIdx + 0), vTessPts(lIdx + 1), vTessPts(lIdx + 2), vTessPts(lIdx + 3), vTessPts(lIdx + 4), vTessPts(lIdx + 5))
                    swSketchSegment.Color = aColours((oOutline.lIndex Mod UBound(aColours)))
                Next lIdx
            Next vOutlineCurve
        Next vOutline

        swModel.Insert3DSketch2 True
        swModel.SetAddToDB False
        swModel.SetDisplayWhenAdded True
    End If
```

```
End Sub
```

```
'OutlineCurve
Option Explicit
Public swCurve As SldWorks.Curve
Public nType As SwConst.swSelectType_e
Public swEntity As SldWorks.Entity
Private Sub Class_Initialize()
    Set swCurve = Nothing
    nType = SwConst.swSelectType_e.swSelNOTHING
    Set swEntity = Nothing
End Sub
```

```
'Outline
Option Explicit
Public lIndex As Long
Public dictCurves As Dictionary
Private Sub Class_Initialize()
    lIndex = -1
    Set dictCurves = New Dictionary
End Sub
```
